<template>
    <span class="main-entry-title" style="display: block">
      <span class="lemma" style="display: inline;"><router-link :to="entry.url" >{{entry.head_lemma}}</router-link></span>
      <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="entry.part_of_speech.full">
        {{entry.part_of_speech.abbrev}}
      </span>
      <span v-for="r in entry.region" class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="r.full">{{r.abbrev}}</span>
      <div v-if="entry.gloss" v-html="entry.gloss" style="display: inline-block;"></div>
    </span>
</template>
<script>
export default {props:['entry']}
</script>
