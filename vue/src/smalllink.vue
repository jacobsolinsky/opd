<template>
  <span class="main-entry-title">
      <span class="lemma"><router-link :to="`/vue${entry.url}`" >{{entry.head_lemma}}</router-link></span>
      <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="entry.part_of_speech.full">
        {{entry.part_of_speech.abbrev}}
      </span>
      <span v-for="r in entry.region" class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="r.full">
        {{r.abbrev}}
      </span>
  </span>
</template>
<script>
import { EventBus } from './event-bus.js';
export default {props:['entry'],
methods: {
  loadMainEntry(){
    var self=this
    fetch(`/vue${self.entry.url}`).
    then(response => response.json()).
    then(data => EventBus.$emit('mainentry', data))
  }}}
</script>
