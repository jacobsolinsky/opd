<template>
<form>
  <div class="panel panel-oj">
    <div class="panel-heading">
      <h4 class="panel-title">Inflectional Forms</h4>
    </div>
    <div class="panel-collapse">
      <div class="panel-body">
        <table class="table table-hover audio-table">
          <inflectionalformrow v-for="(form, index) in formlist" v-bind:form.sync="form.form" :poss.sync="form.poss" :key="index" @formDelete="formDelete">
          </inflectionalformrow>
        </table>
        <button v-on:click.stop.prevent="add">Add</button>
      </div>
    </div>
  </div>
</form>
</template>
<script>
import inflectionalformrow from "./inflectionalformrow.vue"
export default {
  components: {inflectionalformrow},
  props: ['formlist'],
  methods: {
    add(event){
      this.formlist.push({
        form:"",
        poss:[]
      })
    },
    formDelete(index){
      console.log(index)
      this.formlist.splice(index, 1)
    }
  }
}
</script>
