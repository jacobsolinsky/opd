<template>
    <a style="display:inline;">
    <multiselect v-model="entry"
     :options="options"  label="head_lemma"
     :custom-label="lemmaPart_of_speech" :optionsLimit="8"
     @input="updateEntry">
   </multiselect>
   <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
    </a>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  components: {Multiselect},
  props:['entry'],
  data () {
    return {
      options: []
    }
  },
  created(){
    var self = this
    this.$store.dispatch('allEntries')
    this.$store.state._allEntries.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    lemmaPart_of_speech({head_lemma, part_of_speech}){
      return `${head_lemma} : ${part_of_speech}`
    },
    updateEntry(){
      this.$emit('updateEntry', {entry: this.entry, index: this.$vnode.key})
    },
    deleteThis(){
      this.$emit('entryDelete', this.$vnode.key)
    }
  }
}
</script>
