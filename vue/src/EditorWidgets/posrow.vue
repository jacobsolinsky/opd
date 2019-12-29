<template>
  <div class="posrow">
<span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title=""  aria-describedby="tooltip891502">
    <multiselect class="posselect"
    v-if="showOptions"
     :options="options" v-model="pos" :optionsLimit="8" :custom-label="abbrevFull"
     @input="updatePos">
       <template slot="singleLabel" slot-scope="props">
          {{props.option.abbrev}} 
      </template>
      <template slot="option" slot-scope="props">
         {{props.option.abbrev}} : <i>{{props.option.full}}</i>
     </template>
     <slot :pos="pos"></slot>
   </multiselect>
   </span>
    <span v-on:click.stop.prevent="deleteThis" >ⓧ</span>
  </div>
</template>
<script>
import {Multiselect} from 'vue-multiselect'
export default {
  components: {Multiselect},
  props: ['pos'],
  data(){
    return {
      options: null,
      showOptions: false}
  },
  created(){
    var self = this
    this.$store.dispatch('allPos')
    this.$store.state._allPos.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods:{
    deleteThis(){
      this.$emit("posDelete", this.$vnode.key)
    },
    updatePos(){
      this.$emit('updatePos', {pos:this.pos, index:this.$vnode.key})
    },
    abbrevFull(pos){
      return `${pos.abbrev}: ${pos.full}`
    }
  }
}
</script>
<style>
.posrow {
  display: inline;
}
.multiselect__input {
  z-index:-1
}
</style>
