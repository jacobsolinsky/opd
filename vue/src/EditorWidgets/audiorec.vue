<template>
  <div style="display: inline-block; border: solid; border-width:  0.2em 0.2em; border-color: #ece5dd;">
    <div style="display: inline;">
      <label style="display: block;">Regular audio recording URL</label>
      <input style="display: block;" type="text" v-model="audiorec.audio.regular" @input="updateAudiorec">
    </div>
    <div style="display: inline-block;">
      <label style="display: block;">Mobile audio recording URL</label>
      <input style="display: block;" type="text" v-model="audiorec.audio.mobile" @input="updateAudiorec">
    </div>
    <speakerwidget :speaker="audiorec.speaker" @updateSpeaker="updateSpeaker"></speakerwidget>
    <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
  </div>
</template>
<script>
import speakerwidget from './speakerwidget.vue'
export default {
  components: {speakerwidget},
  props: ['audiorec'],
  methods:{
    deleteThis(){
      this.$emit("audiorecDelete", this.$vnode.key)
    },
    updateAudiorec(){
      this.$emit('updateAudiorec', {audiorec:this.audiorec, index:this.$vnode.key})
    },
    updateSpeaker(e){
      this.audiorec.speaker = e
      this.$emit('updateAudiorec', {audiorec:this.audiorec, index:this.$vnode.key})
    }
  }
}
</script>
<style>
.posrow {
  display: inline;
}

</style>
