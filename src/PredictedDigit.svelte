<script lang="ts">
	import Canvas from './Canvas.svelte';
	import { predictionPercentage, toggleGraph } from './store/stores.ts';
  $: predictedAnswer = Object.keys($predictionPercentage).reduce((a, b) => $predictionPercentage[a] > $predictionPercentage[b] ? a : b, {});
  function onGraphBtnClick() {
    toggleGraph.update(value => !value)
  }
  
</script>
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Patrick+Hand&family=Playfair+Display:wght@900&display=swap" rel="stylesheet">
<main>
  <div id="box">
  <h1 id="predictProduct">{predictedAnswer}</h1></div>
  <button on:click={onGraphBtnClick} id="ButtonGraph">Graph</button>
</main>

<style>
  #box{
    position:relative;
  }
  #ButtonGraph{
    position: fixed;
    width: 200px;
    height: 80px;
    left: 70%;
    top: 75%;
    background: #B1C319;
    border-radius: 20px 20px 20px 20px;
    color: #FFFDFD;
    font-size: 25px;
  }
  #predictProduct{
    position: fixed;
    left: 75%;
    top: 40%;
    font-family: 'Patrick Hand', cursive;
    font-style: normal;
    font-weight: normal;
    font-size: 400%;
    line-height: 171px;
    text-align: center;
    color: #FFFFFF;
  }
</style>