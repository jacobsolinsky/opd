<template>
  <table class="conjugation-table">
      <tr><th>Subject</th><th>Form</th></tr>
      <template v-if="details.imperative">
        <template v-for='s in imperativeSubjects'>
              <tr><th>{{actorOjibweNames[s]}}</th><td>{{forms[s]}}</td></tr>
        </template>
      </template>
      <template v-else>
        <template  v-for='s in subjects'>
              <tr><th>{{actorOjibweNames[s]}}</th><td>{{forms[s]}}</td></tr>
        </template>
      </template>
  </table>
</template>
<script>
import { mapState } from 'vuex'
  export default {
    props: ['forms', 'details'],
    computed: {
      ...mapState('actors', ['animateActors', 'inanimateActors', 'singularActors', 'pluralActors', 'actorOjibweNames', 'actorEnglishNames', 'imperativeActors']),
      subjects() {
        return this.details.plural_only ? this.pluralActors.filter(v => this.animateActors.includes(v)) : this.animateActors
      },
      imperativeSubjects(){
        return this.details.plural_only ? this.pluralActors.filter(v => this.imperativeActors.includes(v)) : this.imperativeActors
      },
    },
  }
</script>
<style scoped>
</style>
