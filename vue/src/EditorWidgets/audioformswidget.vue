<template>
  <form>
    <div class="panel panel-oj">
      <div class="panel-heading">
        <h4 class="panel-title">{{title}}</h4>
      </div>
      <div class="panel-collapse">
        <div class="panel-body">
          <table class="table table-hover audio-table">
            <audiorow v-for="(audioform, index) in audioforms" :key="index" @audioformDelete="audioformDelete"
            @updateAudioform="updateAudioform" :audioform="audioform">
            </audiorow>
          </table>
          <button v-on:click.stop.prevent="add">Add</button>
        </div>
      </div>
    </div>
  </form>
</template>
<script>
import audiorow from './audiorow.vue'
export default {
  components: {audiorow},
  props: ['audioforms', 'title'],
  methods: {
    add(){
      this.audioforms.push({
        ojibwe:"",
        poss:[],
        audio_rec:[]
      })
    },
    audioformDelete(index){
      this.audioforms.splice(index, 1)
    },
    updateAudioform(e){
      this.audioforms[e.index] = e.audioform
      this.$emit("updateAudioforms", this.audioforms)
    }
  }


}
</script>
