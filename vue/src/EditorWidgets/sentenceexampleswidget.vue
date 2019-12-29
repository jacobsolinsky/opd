<template>
  <form>
    <div class="panel panel-oj">
      <div class="panel-heading">
        <h4 class="panel-title">Sentence Examples</h4>
      </div>
      <div class="panel-collapse">
        <div class="panel-body">
          <table class="table table-hover audio-table">
            <sentenceexamplerow v-for="(sentenceexample, index) in sentenceexamples" :key="index" @sentenceexampleDelete="sentenceexampleDelete"
            @updateSentenceexample="updateSentenceexample" :sentenceexample="sentenceexample">
            </sentenceexamplerow>
          </table>
          <button v-on:click.stop.prevent="add">Add</button>
        </div>
      </div>
    </div>
  </form>
</template>
<script>
import sentenceexamplerow from "./sentenceexamplerow.vue"
export default {
  components: {sentenceexamplerow},
  props:["sentenceexamples"],
  methods: {
    add(){
      this.sentenceexamples.push({
        ojibwe:"",
        english:"",
        audio_rec:[]
      })
    },
    sentenceexampleDelete(index){
      this.sentenceexamples.splice(index, 1)
    },
    updateSentenceexample(e){
      this.sentenceexamples[e.index] = e.sentenceexample
      this.$emit("updateSentenceexamples", this.sentenceexamples)
    }
  }
}
</script>
