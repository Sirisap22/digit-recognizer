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

<main>
	<select bind:value={selected} on:change={onSelectModel}>
   {#each models as model} 
     <option value={model}>
      {model.text}
     </option> 
    {/each}
  </select>
</main>

<style>
</style>