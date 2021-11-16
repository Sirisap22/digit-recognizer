<script lang="ts">
  import { onMount } from 'svelte'
  import {
    predictionPercentage,
    toggleGraph,
    togglePredicted,
    selectedModel,
  } from './store/stores.ts'


  $: predictedAnswer = Object.keys($predictionPercentage).reduce(
    (a, b) => ($predictionPercentage[a] > $predictionPercentage[b] ? a : b),
    {},
  )
  let canvas
  let clearBtn
  let predictBtn
  let flag = false
  let prevX = 0
  let currX = 0
  let prevY = 0
  let currY = 0
  let dot_flag = false
  let x = 'white'
  let y = 30
  onMount(() => {


    const ctx = canvas.getContext('2d')
    const width = ctx.canvas.clientWidth
    const height = ctx.canvas.clientHeight
    ctx.fillStyle = 'black'
    ctx.fillRect(0, 0, width, height)
    ctx.fillStyle = 'white'
    ctx.lineCap = 'round'
    canvas.addEventListener(
      'mousemove',
      function (e) {
        findxy('move', e)
      },
      false,
    )
    canvas.addEventListener(
      'mousedown',
      function (e) {
        findxy('down', e)
      },
      false,
    )
    canvas.addEventListener(
      'mouseup',
      function (e) {
        findxy('up', e)
      },
      false,
    )
    canvas.addEventListener(
      'mouseout',
      function (e) {
        findxy('out', e)
      },
      false,
    )
    function draw() {
      ctx.beginPath()
      ctx.moveTo(prevX, prevY)
      ctx.lineTo(currX, currY)
      ctx.strokeStyle = x
      ctx.lineWidth = y
      ctx.stroke()
      ctx.closePath()
    }
    function findxy(res, e) {
      if (res == 'down') {
        prevX = currX
        prevY = currY
        currX = e.clientX - canvas.offsetLeft
        currY = e.clientY - canvas.offsetTop
        flag = true
        dot_flag = true
        if (dot_flag) {
          ctx.beginPath()
          ctx.fillStyle = x
          ctx.fillRect(currX, currY, 2, 2)
          ctx.closePath()
          dot_flag = false
        }
      }
      if (res == 'up' || res == 'out') {
        flag = false
      }
      if (res == 'move') {
        if (flag) {
          prevX = currX
          prevY = currY
          currX = e.clientX - canvas.offsetLeft
          currY = e.clientY - canvas.offsetTop
          draw()
        }
      }
    }
    clearBtn.addEventListener(
      'click',
      function (e) {
        erase()
      },
      false,
    )
    function erase() {
      ctx.clearRect(0, 0, width, height)
      ctx.fillStyle = 'black'
      ctx.fillRect(0, 0, width, height)
      ctx.fillStyle = 'white'
      predictionPercentage.set({})
      toggleGraph.set(false)
      togglePredicted.set(false)
    }
    predictBtn.addEventListener(
      'click',
      function (e) {
        predict()
      },
      false,
    )
    function predict() {
      canvas.toBlob(function (blob) {
        const formData = new FormData()
        formData.append('file', blob)
        const res = fetch(
          `${API_DOMAIN}/model_v1/predict/` + $selectedModel,
          {
            method: 'POST',
            body: formData,
          },
        )
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            const predictions = JSON.parse(data)
            for (let key in predictions) {
              if (predictions.hasOwnProperty(key)) {
                predictions[key] = parseFloat(predictions[key])
              }
            }
            predictionPercentage.update((value) => predictions)
            togglePredicted.set(true)
          })
      })
    }
  })
</script>

<style>
  .btn-canvas {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }

  .btn-predict {
    width: 200px;
    height: 80px;
    background: #b1c319;
    border-radius: 20px 20px 20px 20px;
    color: #fffdfd;
    font-size: 25px;
  }

  .btn-clear {
    width: 200px;
    height: 80px;
    background: #b1c319;
    border-radius: 20px 20px 20px 20px;
    color: #fffdfd;
    font-size: 25px;
  }
 
</style>

<main>
  <div>
    <canvas bind:this={canvas} width="500" height="400" id="canvasW" />
  </div>
  <div class="btn-canvas">
    <button bind:this={clearBtn} class="btn-clear">Clear</button>
    <button bind:this={predictBtn} class="btn-predict">Predict</button>
  </div>
</main>
