<template>
  <div>
    <multiselect v-model="partofspeech"
     :options="options" track-by="abbrev" label="abbrev"
     :custom-label="abbrevFull" :optionsLimit="8"></multiselect>
    <button v-on:click="updatePartofspeech">Change Part Of Speech</button>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  components: {Multiselect},
  props: ["partofspeech"],
  data () {
    return {
      options: []
    }
  },
  created(){
    var self = this
    fetch("json/all-parts-of-speech")
    .then(response => response.json())
    .then(data => {self.options = data})
  },
  methods:{
    abbrevFull({abbrev, full}){
      return `${abbrev} : ${full}`
    },
    updatePartofspeech(){
      this.$emit("updatePartofspeech", this.partofspeech)
    }
  }
}
</script>
<style scoped>
.multiselect__input {
  width:100px;
}
</style>
