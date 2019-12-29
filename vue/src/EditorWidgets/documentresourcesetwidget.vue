<template>
  <tr>
    <documentresourcerow v-for="(documentresource, index) in documentresourceset"  :key="index"
    @documentresourceDelete="documentresourceDelete"  @updateDocumentresource="updateDocumentresource"
    :documentresource="documentresource" v-slot="slotProps">
    {{slotProps.documentresource}}
  </documentresourcerow>
    <button v-on:click.stop.prevent="add">Add document resource</button>
  </tr>
</template>
<script>
import documentresourcerow from "./documentresourcerow.vue"
export default{
  props: ["documentresourceset"],
  components: {documentresourcerow},
  methods: {
    add(){
      this.documentresourceset.push({
        righthref:"",
        righttext:"Click here"
      })
    },
    updateDocumentresource(e){
      this.documentresourceset[e.index] = e.pos;
    },
    documentresourceDelete(index){
      this.documentresourceset.splice(index, 1)
    }
  }
}
</script>
