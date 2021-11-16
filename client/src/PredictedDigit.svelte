<script lang="ts">
  import Canvas from './Canvas.svelte'
  import { predictionPercentage, toggleGraph } from './store/stores.ts'
  $: predictedAnswer = Object.keys($predictionPercentage).reduce(
    (a, b) => ($predictionPercentage[a] > $predictionPercentage[b] ? a : b),
    {},
  )
  function onGraphBtnClick() {
    toggleGraph.update((value) => !value)
  }
</script>

<style>
  .btn-graph {
    width: 200px;
    height: 80px;
    background: #b1c319;
    border-radius: 20px 20px 20px 20px;
    color: #fffdfd;
    font-size: 25px;
  }

  .predict-product {
    font-family: 'Patrick Hand', cursive;
    font-style: normal;
    font-weight: normal;
    font-size: 400%;
    line-height: 171px;
    color: #ffffff;
  }

  .accuracy {
    font-display: inherit;
    font-family: 'Patrick Hand', cursive;
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 42px;
    color: #ffffff;
  }

  .prediction-digit {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
  }
</style>

<link
  href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Patrick+Hand&family=Playfair+Display:wght@900&display=swap"
  rel="stylesheet" />
<main>
  <div class="prediction-digit accuracy">
    <h1 class="predict-product">{predictedAnswer}</h1>
    <p>{$predictionPercentage[predictedAnswer] ? `Probability: ${$predictionPercentage[predictedAnswer]}%` : ''}<p>
    <button on:click={onGraphBtnClick} class="btn-graph">Graph</button>
  </div>
</main>
