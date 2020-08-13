<template>
  <table class="conjugation-table">
    <tr><th>Subject > Object</th><th>0</th><th>0p</th></tr>
    <template v-if="details.independent">
      <template v-for='s in subjects'>
            <tr><th>{{actorOjibweNames[s]}}</th><td>{{forms[s]['0'].actor}}</td><td>{{forms[s]['0p'].actor}}</td></tr>
      </template>
    </template>
    <template v-else-if="details.conjunct">
      <template v-for='s in subjects'>
            <tr><th>{{actorOjibweNames[s]}}</th><td colspan="2">{{forms[s]['0'].actor}}</td></tr>
      </template>
    </template>
    <template v-else-if="details.imperative">
      <template v-for='s in imperativeSubjects'>
            <tr><th>{{actorOjibweNames[s]}}</th><td colspan="2">{{forms[s]['0'].actor}}</td></tr>
      </template>
    </template>
  </table>
</template>
<script>
import {mapState} from 'vuex'
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
