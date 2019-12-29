<template>
    <div class="speaker-initials" style="display: inline-block;">
    <multiselect v-model="speaker"
     :options="options" track-by="initials" label="initials"
     :custom-label="initialsName" :optionsLimit="8"
     @input="updateSpeaker">
     <template slot="singleLabel" slot-scope="props">
        {{props.option.initials}}
    </template>
    <template slot="option" slot-scope="props">
       {{props.option.intitials}} : <i>{{props.option.primary_name}}</i>
   </template>
   </multiselect>
 </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  components: {Multiselect},
  props:['speaker'],
  data () {
    return {
      options: []
    }
  },
  created(){
    var self = this
    this.$store.dispatch('allSpeakers')
    this.$store.state._allSpeakers.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    initialsName({initials, primary_name}){
      return `${initials} : ${primary_name}`
    },
    updateSpeaker(){
      this.$emit('updateSpeaker', this.speaker)
    },
  }
}
</script>
