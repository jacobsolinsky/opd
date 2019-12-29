<template>
  <tr>
    <label>Inflectional Form</label>
    <input type="text" :value="form"  @input="$emit('update:form', $event.target.value)">
    <label>Attributes</label>
    <posrow v-for="(pos, index) in poss" :pos.sync="pos" :key="index"
    @posDelete="posDelete" v-slot="slotProps" @updatePos="updatePos">
    {{slotProps.pos}}
    </posrow>
    <button v-on:click.stop.prevent="add">Add Attribute</button>
    <button v-on:click.stop.prevent="deleteThis">Delete Form</button>
  </tr>
</template>
<script>
import posrow from "./posrow.vue"
export default{
  props: ["form", "poss"],
  components: {posrow},
  methods: {
    deleteThis(){
      console.log(this.$vnode.key)
      this.$emit("formDelete", this.$vnode.key)
    },
    add(){
      this.poss.push({
        abbrev:"Select attribute",
        full:""
      })
    },
    updatePos(e){
      this.poss[e.index] = e.pos;
    },
    posDelete(index){
      console.log(index)
      this.poss.splice(index, 1)
    }
  }
}
</script>
