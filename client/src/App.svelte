<script lang="ts">
  import Canvas from './Canvas.svelte'
  import ModelSelector from './ModelSelector.svelte'
  import PercentageGraph from './PercentageGraph.svelte'
  import PredictedDigit from './PredictedDigit.svelte'
  import { toggleGraph, togglePredicted } from './store/stores.ts'
</script>

<style>
  #bg {
    height: 100vh;
		width: 100%;
    background: #606060;
  }

  @media only screen and (max-width: 1100px) {
		#bg {
			width: 100%;
			height: 150vh;
			background: #606060;
		}
	}

	@media only screen and (max-width: 768px) {
		#bg {
			width: 100%;
			height: 180vh;
			background: #606060;
		}
	}


  .tabbar {
    /* position: absolute; */
    width: 100%;
    height: 80px;
    left: 0;
    top: 0;
    left: 0;
    background: #b1c319;
    box-shadow: 3px 4px 0px 0px rgba(0, 0, 0, 1);
  }
  .hand-write {
    text-align: center;
    /* position: relative; */
    font-family: 'Indie Flower', cursive;
    font-style: normal;
    font-weight: bold;
    line-height: 75px;
    text-align: center;
    color: #ffffff;
  }

  .write-num {
    font-family: 'Indie Flower', cursive;
    font-style: normal;
    font-weight: normal;
    line-height: 95%;
    /* text-align: center; */
    color: #ffffff;
    font-weight: bold;
  }

  .prediction-result {
    height: 60px;
    font-family: 'IM Fell English SC', serif;
    font-style: normal;
    font-weight: bold;
    font-size: 48px;
    line-height: 56px;
    color: #ffffff;
  }

	.application {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
		align-items: center;
		height: 70%;
	}

	.canvas {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.mode-selector {
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
		height: 30%;
	}

	.prediction-board {
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
		/* height: 70%; */
	}

	.arrow-img {
		width: 200px;
	}

</style>

<head>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" />
</head>

<main id="bg">
  <div class="tabbar">
    <h1 class="hand-write">Handwritten Digit Recognition Web App</h1>
  </div>

  <div class="application">
    <div class="canvas">
			<h1>
				<p class="write-num">Write your number!</p>
			</h1>
      <Canvas />
    </div>
	
		<div class="mode-selector">
			<img class="arrow-img" src="arrow-right.png" alt="arrow-right" />
			<ModelSelector />
		</div>

    <div class="prediction-board">
			<p class="prediction-result">Prediction Result</p>
      {#if $togglePredicted}
        <PredictedDigit />
			{:else}
			<div style="height: 331.076px">
			</div>
      {/if}
    </div>

  </div>
		<div class="prediction-graph">
			{#if $toggleGraph}
				<PercentageGraph />
			{/if}
		</div>
</main>
