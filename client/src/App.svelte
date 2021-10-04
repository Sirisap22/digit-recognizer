<script lang="ts">
	import Canvas from './Canvas.svelte';
	import PercentageGraph from './PercentageGraph.svelte';
	import { predictionPercentage, toggleGraph } from './store/stores.ts';
</script>

<main>
	<Canvas/>
	{#if $toggleGraph}
		<PercentageGraph/>
	{/if}
</main>

<style>

</style>