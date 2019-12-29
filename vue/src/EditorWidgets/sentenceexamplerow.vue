<template>
  <tr>
    <label>Sentence Example</label>
    <textarea v-model="sentenceexample.ojibwe"  @input="updateSentenceexample"></textarea>
    <textarea v-model="sentenceexample.english"  @input="updateSentenceexample"></textarea>
    <audiorec v-for="(audiorec, index) in sentenceexample.audio_rec" :audiorec.sync = "audiorec" :key="index + 'audiorec'"
    @audiorecDelete="audiorecDelete" v-slot="slotProps" @updateAudiorec="updateAudiorec">
    </audiorec>
    <button v-on:click.stop.prevent="addAudiorec">Add audio recording</button>
    <button v-on:click.stop.prevent="deleteThis">Delete sentence example</button>
  </tr>
</template>
<script>
import audiorec from "./audiorec.vue"
export default{
  props: ["sentenceexample"],
  components: {audiorec},
  methods: {
    deleteThis(){
      this.$emit("sentenceexampleDelete", this.$vnode.key)
    },
    addAudiorec(){
      this.audioform.audio_rec.push({
        speaker:{},
        audio:{},
      })
    },
    updateAudiorec(e){
      this.sentenceexample.audio_rec[e.index] = e.audiorec;
    },
    audiorecDelete(index){
      this.sentenceexample.audio_rec.splice(e.index, 1)
    },
    updateSentenceexample(){
      this.$emit(
      'updateSentenceexample',
      {sentenceexample: this.sentenceexample,
       index: this.$vnode.key
      })
    }
  }
}
</script>
