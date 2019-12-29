<template>
  <div >
  <multiselect
    v-if="showOptions"
     :options="options" v-model="imageresource" :optionsLimit="3"
     @input="updateImageresource" label="righttext" track-by="righttext" :custom-label="customLabel" :show-labels="false">
       <template slot="singleLabel" slot-scope="props">
          <img :src="props.option.image.src" :alt="props.option.image.alt">
          <a :src="props.option.righthref">{{props.option.righttext}}</a>
      </template>
      <template slot="option" slot-scope="props">
        <img :src="props.option.image.src" :alt="props.option.image.alt">
        <a :src="props.option.righthref">{{props.option.righttext}}</a>
     </template>
     <slot :imageresource="imageresource"></slot>
   </multiselect>
    <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
  </div>
</template>
<script>
import {Multiselect} from 'vue-multiselect'
export default {
  components: {Multiselect},
  props: ['imageresource'],
  data(){
    return {
      options: null,
      showOptions: false}
  },
  created(){
    var self = this
    this.$store.dispatch('allImageresource_set')
    this.$store.state._allImageresource_set.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    deleteThis(){
      this.$emit("imageresourceDelete", this.$vnode.key)
    },
    updateImageresource(){
      this.$emit('updateImageresource', {imageresource:this.imageresource, index:this.$vnode.key})
    },
  customLabel(resource){
    return resource.righttext
    }
  }
}
</script>
