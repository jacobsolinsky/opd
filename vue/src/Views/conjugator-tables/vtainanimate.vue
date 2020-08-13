<template>
  <table class="conjugation-table">
    <tr><th>Subject > Object</th><th>0</th><th>0p</th></tr>
    <template v-if="details.independent">
      <template v-for='s in subjects'>
            <tr><th>{{actorOjibweNames[s]}}</th><td>{{forms['0'][s].actor}}</td><td>{{forms['0p'][s].actor}}</td></tr>
      </template>
    </template>
    <template v-else-if="details.conjunct">
      <template v-for='s in subjects'>
            <tr><th>{{actorOjibweNames[s]}}</th><td colspan="2">{{forms['0'][s].actor}}</td></tr>
      </template>
    </template>
  </table>
</template>
<script>
import {mapState} from 'vuex'
  export default {
    props: ['forms', 'details'],
    computed: {
      ...mapState('actors', ['animateActors', 'actorOjibweNames', 'actorEnglishNames']),
      subjects() {
        return this.animateActors.filter(v => v != 'X')
      },
    },
  }
</script>
