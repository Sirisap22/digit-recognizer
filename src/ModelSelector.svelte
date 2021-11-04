<script lang="ts">
	import { selectedModel } from './store/stores.ts';

  let selected;

  let models = [
    {endpoint: 'svm', text: 'Support Vector Machine'},
    {endpoint: 'sfm', text: 'Softmax Regression'}
  ]

  function onSelectModel() {
    console.log(selected)
    selectedModel.set(selected.endpoint)
    // console.log($selectedModel)
  }
</script>

<main><div id="select">
	<select bind:value={selected} on:change={onSelectModel}>
   {#each models as model} 
     <option value={model}>
      {model.text}
     </option> 
    {/each}
  </select></div>
</main>

<style>
  #select{
    position: fixed;
    width: 180px;
    height: 0px;
    left: 45%;
    top: 50%;

  }
</style>