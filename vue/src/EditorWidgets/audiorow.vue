<template>
  <tr>
    <div style="border: solid; border-width: 1em 0.5em; border-color: #ece5dd;">
      <label>Audio Form</label>
      <input type="text" v-model="audioform.ojibwe"  @input="updateAudioform">
      <label>Attributes</label>
      <posrow v-for="(pos, index) in audioform.poss" :pos.sync="pos" :key="index + 'poss'"
      @posDelete="posDelete" v-slot="slotProps" @updatePos="updatePos">
      {{slotProps.pos}}
      </posrow>
      <button v-on:click.stop.prevent="addPos">Add Attribute</button>
    </div>
    <audiorec v-for="(audiorec, index) in audioform.audio_rec" :audiorec.sync = "audiorec" :key="index + 'audiorec'"
    @audiorecDelete="audiorecDelete" v-slot="slotProps" @updateAudiorec="updateAudiorec">
    </audiorec>
    <button v-on:click.stop.prevent="addAudiorec">Add Audio Recording</button>
    <button v-on:click.stop.prevent="deleteThis">Delete Audio Form</button>
  </tr>
</template>
<script>
import posrow from "./posrow.vue"
import audiorec from "./audiorec.vue"
export default{
  props: ["audioform"],
  components: {posrow, audiorec},
  methods: {
    deleteThis(){
      this.$emit("audioformDelete", this.$vnode.key)
    },
    addPos(){
      this.audioform.poss.push({
        abbrev:"Select attribute",
        full:""
      })
    },
    addAudiorec(){
      this.audioform.audio_rec.push({
        speaker:{},
        audio:{},
      })
    },
    updatePos(e){
      var index = e.index.slice(0, -4)
      this.audioform.poss[index] = e.pos
    },
    posDelete(index){
      var index = Number(index.slice(0, -4))
      this.audioform.poss.splice(index, 1)
    },
    updateAudiorec(e){
      var index = e.index.slice(0, -8)
      this.audioform.audio_rec[index] = e.audiorec;
    },
    audiorecDelete(index){
      var index = index.slice(0, -8)
      this.audioform.audio_rec.splice(index, 1)
    },
    updateAudioform(){
      this.$emit(
      'updateAudioform',
      {audioform: this.audioform,
       index: this.$vnode.key
      })
    }
  }
}
</script>
