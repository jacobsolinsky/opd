<template>
  <div >
  <multiselect
    v-if="showOptions"
     :options="options" v-model="videoresource" :optionsLimit="3"
     @input="updateVideoresource" label="righttext" track-by="righttext" :custom-label="customLabel" :show-labels="false">
       <template slot="singleLabel" slot-scope="props">
          <img :src="props.option.image.src" :alt="props.option.image.alt">
          <a :src="props.option.righthref">{{props.option.righttext}}</a>
      </template>
      <template slot="option" slot-scope="props">
        <img :src="props.option.image.src" :alt="props.option.image.alt">
        <a :src="props.option.righthref">{{props.option.righttext}}</a>
     </template>
     <slot :videoresource="videoresource"></slot>
   </multiselect>
    <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
  </div>
</template>
<script>
import {Multiselect} from 'vue-multiselect'
export default {
  components: {Multiselect},
  props: ['videoresource'],
  data(){
    return {
      options: null,
      showOptions: false}
  },
  created(){
    var self = this
    this.$store.dispatch('allVideoresource_set')
    this.$store.state._allVideoresource_set.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    deleteThis(){
      this.$emit("videoresourceDelete", this.$vnode.key)
    },
    updatePos(){
      this.$emit('updateVideoresource', {videoresource:this.videoresource, index:this.$vnode.key})
    },
    customLabel(resource){
      return resource.righttext
    }
  }
}
</script>
