<template>
  <div>
    <multiselect v-model="value"
     :options="options" track-by="abbrev" label="abbrev"
     :custom-label="abbrevFull" :optionsLimit="8"></multiselect>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  components: {Multiselect},
  data () {
    return {
      value: null,
      options: []
    }
  },
  created(){
    var self = this
    fetch("/vue/json/all-parts-of-speech")
    .then(response => response.json())
    .then(data => {self.options = data})
  },
  methods:{
    abbrevFull({abbrev, full}){
      return `${abbrev} : ${full}`
    }
  }
}
</script>
<style scoped>
.multiselect__input {
  width:100px;
}
</style>
