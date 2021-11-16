<script lang="ts">
  import { selectedModel } from './store/stores.ts'
  let selected
  let models = [
    { endpoint: 'svm', text: 'Support Vector Machine' },
    { endpoint: 'sfm', text: 'Softmax Regression' },
  ]
  function onSelectModel() {
    selectedModel.set(selected.endpoint)
  }
</script>

<main>
  <div>
    <select bind:value={selected} on:change={onSelectModel}>
      {#each models as model}
        <option value={model}>{model.text}</option>
      {/each}
    </select>
  </div>
</main>
