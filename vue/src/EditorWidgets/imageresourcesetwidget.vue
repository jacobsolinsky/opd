<template>
  <tr>
    <imageresourcerow v-for="(imageresource, index) in imageresourceset"  :key="index"
    @imageresourceDelete="imageresourceDelete"  @updateImageresource="updateImageresource"
    :imageresource="imageresource" v-slot="slotProps">
    {{slotProps.imageresource}}
    </imageresourcerow>
    <button v-on:click.stop.prevent="add">Add image resource</button>
  </tr>
</template>
<script>
import imageresourcerow from "./imageresourcerow.vue"
export default{
  props: ["imageresourceset"],
  components: {imageresourcerow},
  methods: {
    add(){
      this.imageresourceset.push({
        image:{
          src:"",
          alt:""
        },
        righthref:"",
        righttext:"Click here"
      })
    },
    updateImageresource(e){
      this.imageresourceset[e.index] = e.pos;
    },
    imageresourceDelete(index){
      this.imageresourceset.splice(index, 1)
    }
  }
}
</script>
