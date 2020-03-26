<template>
    <b-card>
      <span v-if='loading'>Loading...</span>
      <b-tabs v-if='!loading' card>
        <b-tab title="Independent (A form)">
          <regularmodes :forms='forms.independent' :details='details'></regularmodes>
        </b-tab>
        <b-tab title="Conjunct (B form)">
          <regularmodes :forms='forms.conjunct' :details='details'></regularmodes>
        </b-tab>
        <b-tab title="Changed Conjunct (C form)">
          <regularmodes :forms='forms["changed-conjunct"]' :details='details'></regularmodes>
        </b-tab>
        <b-tab title="Imperative">
          <imperativemodes :forms='forms.imperative' :details='details' v-if='details.type!=="vii"'></imperativemodes>
        </b-tab>
      </b-tabs>
    </b-card>
</template>
<script>
import regularmodes from './regularmodes.vue'
import imperativemodes from './imperativemodes.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['details', 'entryurl'],
  components: {regularmodes, imperativemodes, BTab, BTabs, BCard},
  data(){
    return {
    forms:{},
    loading: true,
    }
  },
  mounted() {
    fetch(`/json/conjugation/main-entry/${this.entryurl}`)
    .then(response => response.json())
    .then(data => {
      this.forms = data;
      this.loading = false;
      })
  },
  watch: {
    entryurl() {
      fetch(`/json/conjugation/main-entry/${this.entryurl}`)
      .then(response => response.json())
      .then(data => {this.forms = data})
    }
  },
}
</script>
<style>
  .conjugation-table {
    background-color: #FFFFFF;
    color: #222;
    margin: 1em 0;
    border: 1px solid #EEEEEE;
    border-collapse: collapse;
}
.conjugation-table td, .conjugation-table th {
    padding: 5px;
}
a.nav-link {
  color: black;
}
a.nav-link.active {
  font-weight: bold;
  color: blue;
}

</style>
