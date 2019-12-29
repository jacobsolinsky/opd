<template>
  <tr>
    <videoresourcerow v-for="(videoresource, index) in videoresourceset"  :key="index"
    @videoresourceDelete="videoresourceDelete"  @updateVideoresource="updateVideoresource"
    :videoresource="videoresource" v-slot="slotProps">
    {{slotProps.videoresource}}
  </videoresourcerow>
    <button v-on:click.stop.prevent="add">Add video resource</button>
  </tr>
</template>
<script>
import videoresourcerow from "./videoresourcerow.vue"
export default{
  props: ["videoresourceset"],
  components: {videoresourcerow},
  methods: {
    add(){
      this.videoresourceset.push({
        image:{
          src:"",
          alt:""
        },
        righthref:"",
        righttext:"Click here"
      })
    },
    updateVideoresource(e){
      this.videoresourceset[e.index] = e.pos;
    },
    VideoresourceDelete(index){
      this.videoresourceset.splice(index, 1)
    }
  }
}
</script>
