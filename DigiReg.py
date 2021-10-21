import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm as tqdm
import os

for dirname, _, filenames in os.walk('D:/work/3DS1/Linear/DigiReg/kaggle/input/digit-recognizer'): #database check
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_data = pd.read_csv('D:/work/3DS1/Linear/DigiReg/kaggle/input/digit-recognizer/train.csv')
train_data.head() #first column

x_train = train_data.iloc[:,1:].values/255 #train_data(x)
y_train = train_data.label.values #train_data(y)

#split train_data(x)&(y) into train_x, valid_x, train_y, valid_y
train_x, train_valid_x, train_y, train_valid_y = train_test_split(x_train, y_train, test_size = 0.2, random_state = 42)

train_x_torch = torch.from_numpy(train_x).type(torch.FloatTensor)
valid_x_torch = torch.from_numpy(train_valid_x).type(torch.FloatTensor)
train_y_torch = torch.from_numpy(train_y).type(torch.LongTensor)
valid_y_torch = torch.from_numpy(train_valid_y).type(torch.LongTensor)

#dimension
train_x_torch = train_x_torch.view(-1, 1,28,28).float()
valid_x_torch = valid_x_torch.view(-1, 1,28,28).float()

#TensorDataset
train_set = torch.utils.data.TensorDataset(train_x_torch, train_y_torch)
valid_set = torch.utils.data.TensorDataset(valid_x_torch, valid_y_torch)

#preparing Data Loaders
batch_size = 128
train_loader = torch.utils.data.DataLoader(train_set, shuffle = True, batch_size = 128)
valid_loader = torch.utils.data.DataLoader(valid_set, shuffle = True, batch_size = 128)

#image of digit recognizer
#plt.figure(figsize=(30,30))
#for i in range(10):
#    plt.subplot(20, 20, i+1)
#    plt.title("No." + str(i))
#    plt.imshow(train_data.iloc[:,1:].iloc[i].values.reshape(28,28),cmap='Greys')
    
#plt.show()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") 

list_process=[]
#send data to GPU and reset optimaizer and define loss calculation,loss backward
def train(model,epoch):
    model.train()
    train_loss = 0
    correct = 0 
    for data, label in train_loader:
        data,label = data.to(device), label.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output,label)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        pred = output.argmax(dim=1, keepdim=True)
        correct+=pred.eq(label.view_as(pred)).sum().item()
    print('epoch for train: {}, accuracy: ({:.2f}%)'.format(epoch,correct*100 / len(train_loader.dataset)))
    list_process.append(correct*100 / len(train_loader.dataset))

def valid(model, epoch):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, label in valid_loader:
            data, label = data.to(device), label.to(device)
            output = model(data)
            test_loss += criterion(output, label).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(label.view_as(pred)).sum().item()
    print('epoch for test: {}, accuracy: ({:.2f}%)'.format(epoch,correct*100 / len(valid_loader.dataset)))

class cnn_layers(nn.Module):
    def __init__(self):
        super(cnn_layers,self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

model = cnn_layers()
model.to(device)
optimizer = optim.Adam(model.parameters(), lr=0.0001)
criterion = nn.CrossEntropyLoss() 

print(model)
for epoch in tqdm(range(3)): #accuracy
    train(model,epoch)

test_data = pd.read_csv('D:/work/3DS1/Linear/DigiReg/kaggle/input/digit-recognizer/test.csv')
x_test = test_data.values/255
x_test_torch = torch.from_numpy(x_test).type(torch.FloatTensor)
d_labels = np.zeros(x_test.shape)
d_labels = torch.from_numpy(d_labels)
#Think about dimentions of data. Without this "an shapes doesn't fit error", will occur.
x_test_torch = x_test_torch.view(-1, 1, 28, 28)
#Make a tensordataset and a testloader
testset = torch.utils.data.TensorDataset(x_test_torch, d_labels)
testloader = torch.utils.data.DataLoader(testset, batch_size = 1, shuffle = False)

submit_list = [['ImageId', 'Label']]
with torch.no_grad():
    model.eval()
    image_id = 1
    for images,label in testloader:
        images,label = images.to(device), label.to(device)
        outputs = model(images)
        probs = torch.exp(outputs)
        top_p, top_class = probs.topk(1, dim = 1)
        for preds in top_class:
            submit_list.append([image_id,preds.item()])
            image_id += 1

df = pd.DataFrame(submit_list)
df.columns = df.iloc[0]
df = df.drop(0, axis = 0)
df.to_csv('submit.csv', index = False)
print("submit.csv saved")

plt.figure(figsize=(30,30))
for i in range(5,10):
    plt.subplot(20, 20, i+1)
    plt.imshow(test_data.iloc[i].values.reshape(28,28),cmap='Greys')

plt.show()
df.iloc[5:10,[1]].T