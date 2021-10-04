<script lang="ts">
	import Canvas from './Canvas.svelte';
	import PercentageGraph from './PercentageGraph.svelte';
	import PredictedDigit from './PredictedDigit.svelte';
	import { predictionPercentage, toggleGraph, togglePredicted } from './store/stores.ts';
</script>

<main>
	<Canvas/>
	{#if $togglePredicted}
		<PredictedDigit/>
	{/if}
	{#if $toggleGraph}
		<PercentageGraph/>
	{/if}
</main>

<style>

</style>