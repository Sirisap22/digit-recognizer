<script lang="ts">
  import { predictionPercentage, toggleGraph } from './store/stores.ts'
  function onBackBtn() {
    toggleGraph.update((value) => !value)
  }
</script>

<style>
  .color-font {
    color: #fffdfd;
    font-size: 35px;
    text-align: center;
    font-family: 'Bebas Neue', cursive;
    z-index: 10;
  }
  #font {
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
    text-align: center;
    line-height: 10px;
    font-size: 20px;
    color: #fffdfd;
  }

  .graph-overlay {
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 1;
  }

  .graph-container {
    position: absolute;
    top: 50%;
    left: 50%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 600px;
    background: #606060;
    box-shadow: 7px 5px 7px 3px rgba(0, 0, 0, 0.79),
      -7px -5px 7px 3px rgba(0, 0, 0, 0.79);
  }



  .graph-page {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #606060;
  }
  .back-btn {
    text-decoration: none;
    display: inline-block;
    width: 120px;
    height: 30px;
    background: #b1c319;
    border-radius: 20px 20px 20px 20px;
  }
  .graph {
    margin-bottom: 1em;
    font: normal 100%/150% arial, helvetica, sans-serif;
  }
  .graph caption {
    font: bold 150%/120% arial, helvetica, sans-serif;
    padding-bottom: 0.33em;
  }
  .graph tbody th {
    text-align: right;
  }
  @supports (display: grid) {
    @media (min-width: 32em) {
      .graph {
        display: block;
        width: 700px;
        height: 400px;
      }
      .graph caption {
        display: block;
      }
      .graph thead {
        display: none;
      }
      .graph tbody {
        position: relative;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(2em, 1fr));
        column-gap: 2.5%;
        align-items: end;
        height: 100%;
        /* margin: 3em 0 1em 2.8em; */
        padding: 0 1em;
        border-bottom: 2px solid rgba(0, 0, 0, 0.5);
        background: repeating-linear-gradient(
          180deg,
          rgba(0, 0, 0, 0.7) 0,
          rgba(0, 0, 0, 0.7) 1px,
          transparent 1px,
          transparent 20%
        );
      }
      .graph tbody:before,
      .graph tbody:after {
        position: absolute;
        left: -3.2em;
        width: 2.8em;
        text-align: right;
        font: bold 100%/140% arial, helvetica, sans-serif;
        font-family: 'Patrick Hand', cursive;
        color: white;
      }
      .graph tbody:before {
        content: '100%';
        top: -0.6em;
      }
      .graph tbody:after {
        content: '0%';
        bottom: -0.6em;
      }
      .graph tr {
        position: relative;
        display: block;
      }
      .graph tr:hover {
        z-index: 999;
      }
      .graph th,
      .graph td {
        display: block;
        text-align: center;
      }
      .graph tbody th {
        position: absolute;
        top: -3em;
        left: -2em;
        width: 100%;
        font-family: 'Patrick Hand', cursive;
        color: white;
        font-weight: normal;
        white-space: nowrap;
        text-indent: 0;
        /* transform:rotate(-45deg); */
      }
      .graph tbody th:after {
        content: '';
      }
      .graph td {
        width: 100%;
        height: 100%;
        background: #b1c319;
        border-radius: 0.5em 0.5em 0 0;
        transition: background 0.5s;
      }
      .graph tr:hover td {
        opacity: 0.7;
      }
      .graph td span {
        overflow: hidden;
        position: absolute;
        left: 50%;
        top: 50%;
        width: 0;
        padding: 0.5em 0;
        margin: -1em 0 0;
        font: normal 85%/120% arial, helvetica, sans-serif;
        /* 			background:white; */
        /* 			box-shadow:0 0 0.25em rgba(0,0,0,0.6); */
        font-weight: bold;
        opacity: 0;
        transition: opacity 0.5s;
        color: white;
      }
      .toggleGraph:checked + table td span,
      .graph tr:hover td span {
        width: 4em;
        margin-left: -2em; /* 1/2 the declared width */
        opacity: 1;
      }
    } /* min-width:32em */
  } /* grid only */
</style>

<link
  href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC&family=Patrick+Hand&family=Playfair+Display:wght@900&display=swap"
  rel="stylesheet" />
<link
  href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap"
  rel="stylesheet" />
<main>
<div class="graph-overlay">
  <div class="graph-container">
    <table class="graph">
      <caption class="color-font">Digit Probability Percentage</caption>
      <thead>
        <tr>
          <th scope="col">Item</th>
          <th scope="col">Percent</th>
        </tr>
      </thead>
      <tbody class="horizontal graph-page">
        {#each Object.entries($predictionPercentage) as [number, percentage]}
          <tr style="height:{percentage}%">
            <th scope="row">{number}</th>
            <td>
              <span>{percentage}</span>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
    <button on:click={onBackBtn} class="back-btn">
      <h1 id="font">Back</h1>
    </button>
    </div>
</div>
</main>
