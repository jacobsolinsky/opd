<template>
  <div >
  <multiselect
    v-if="showOptions"
     :options="options" v-model="documentresource" :optionsLimit="5"
     @input="updateDocumentresource" label="righttext" track-by="righttext" :custom-label="customLabel" :show-labels="false">
       <template slot="singleLabel" slot-scope="props">
          <span class="glyphicon glyphicon-duplicate document-icon"></span>
          <a :src="props.option.righthref">{{props.option.righttext}}</a>
      </template>
      <template slot="option" slot-scope="props">
        <span class="glyphicon glyphicon-duplicate document-icon"></span>
        <a :src="props.option.righthref">{{props.option.righttext}}</a>
     </template>
     <slot :documentresource="documentresource"></slot>
   </multiselect>
    <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
  </div>
</template>
<script>
import {Multiselect} from 'vue-multiselect'
export default {
  components: {Multiselect},
  props: ['documentresource'],
  data(){
    return {
      options: null,
      showOptions: false}
  },
  created(){
    var self = this
    this.$store.dispatch('allDocumentresource_set')
    this.$store.state._allDocumentresource_set.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    deleteThis(){
      this.$emit("documentresourceDelete", this.$vnode.key)
    },
    updateDocumentresource(){
      this.$emit('updateDocumentresource', {documentresource:this.documentresource, index:this.$vnode.key})
    },
    customLabel(resource){
      return resource.righttext
    }
  }
}
</script>
