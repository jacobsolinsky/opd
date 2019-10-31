<template>
<div class="main-entry-search">
  <div class="english-search-main-entry">
  <span class="main-entry-title">

      <span class="lemma"><router-link :to="`/vue${entry.url}`" >{{entry.head_lemma}}</router-link></span>
      <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="entry.part_of_speech.full">
        {{entry.part_of_speech.abbrev}}
      </span>
      <span v-for="r in entry.region" class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="r.full">{{r.abbrev}}</span>
    </span>
    <div v-if="entry.gloss" v-html='entry.gloss' style="display: inline;"></div>
    <span class="badges" v-if="entry.head_audio || entry.imageresource_set.length>0 || entry.videoresource_set.length>0 || entry.documentresource_set.length>0">
      <span v-if="entry.head_audio" class="glyphicon glyphicon-volume-up"></span>
      <span v-if="entry.imageresource_set.length>0" class="glyphicon glyphicon-camera"></span>
      <span v-if="entry.videoresource_set.length>0" class="glyphicon glyphicon-facetime-video"></span>
      <span v-if="entry.documentresource_set.length>0" class="glyphicon glyphicon-paperclip"></span>
    </span>
    </span>
  <div v-if="entry.species"><p></p>
  [<div v-html="entry.species" style="display: inline;"></div>]
  </div>

</div>
  <p class="relations" v-if="entry.paired_with_inv.length>0 || entry.see_also_inv.length>0 || entry.redirect_inv.length>0">
    <div v-if="entry.paired_with_inv.length>0">
      <em>Paired with:</em>
      <smalllink v-for="e in entry.paired_with_inv" :entry="e" :key="e.url"></smalllink>;
    </div>
    <div v-if="entry.see_also_inv.length>0">
      <em>See also:</em>
      <smalllink v-for="e in entry.see_also_inv" :entry="e" :key="e.url"></smalllink>;
    </div>
    <div v-if="entry.redirect_inv.length>0">
      ►
      <smalllink v-for="e in entry.redirect_inv" :entry="e" :key="e.url"></smalllink>;
    </div>
  </p>
</div>
</template>
<script>
import smalllink from './smalllink.vue'
import mediumlink from './mediumlink.vue'
import { EventBus } from './event-bus.js';
export default{
  props: ['entry'],
  components: {smalllink, mediumlink},
  methods: {
    loadMainEntry(){
      var self=this
      fetch(`/vue${self.entry.url}`).
      then(response => response.json()).
      then(data => EventBus.$emit('mainentry', data))
    }
  }
}
</script>
