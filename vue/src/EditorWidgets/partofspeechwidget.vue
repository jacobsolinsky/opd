<template>
  <div>
    <span class="badge badge-oj">
    <multiselect v-if="showOptions" v-model="partofspeech"
    @input="updatePartofspeech"
     :options="options"
     :custom-label="abbrevFull" :optionsLimit="8"></multiselect>
     </span>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  components: {Multiselect},
  props:['partofspeech'],
  data () {
    return {
      options: [],
      showOptions: false
    }
  },
  created(){
    var self = this
    this.$store.dispatch('allPartsOfSpeech')
    this.$store.state._allPartsOfSpeech.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    abbrevFull({abbrev, full}){
      return `${abbrev} : ${full}`
    },
    updatePartofspeech(){
      this.$emit('updatePartofspeech', this.partofspeech)
    }
  }
}
</script>
