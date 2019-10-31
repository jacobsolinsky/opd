<template>
  <div class="col-md-3 col-sm-3 sidebar">
          <p>
    Created and maintained by the University of Minnesota's <a href="http://amin.umn.edu/">Department of American Indian Studies</a>,
    <a href="https://www.lib.umn.edu/">University Libraries</a>,
    <br>and editor John D. Nichols.
  </p>
  <h3>Additional Resources</h3>
  <p>
    Many of the words in the Ojibwe People's Dictionary have related resources. Click through to the full dictionary entry to hear audio recordings, see images, read documents and watch videos. Here's a key to resource icons.
    </p><ul class="list-unstyled">
      <li><span class="glyphicon glyphicon-volume-up"></span> Audio recordings</li>
      <li><span class="glyphicon glyphicon-camera"></span> Images</li>
      <li><span class="glyphicon glyphicon-facetime-video"></span> Video</li>
      <li><span class="glyphicon glyphicon-paperclip"></span> Documents</li>
    </ul>
  <p></p>
  <component :is="wordfamily" v-bind="currentWordfamily"></component>
  <component :is="relatedwords" v-bind="currentRelatedwords"></component>
  <h3>Speakers &amp; Regions Key</h3>
  <p>
  Individual speakers and speakers from different regions use different words when speaking. Each audio recording is marked with the initials of the Ojibwe speaker. Click on a speaker's initials to <a href="/about/voices">go to the speaker's bio page</a>. If an Ojibwe word is particular to a certain region, it will be marked with a region code. Click on the region code to go to the <a href="/help/regions">Regions</a> page.
  </p>

</div>
</template>
<script>
import { EventBus } from './event-bus.js'
import wordfamily from './wordfamily.vue'
import relatedwords from './relatedwords.vue'
export default {
  components: {wordfamily, relatedwords},
  data() {
  return  {
    currentWordfamily: null,
    wordfamily: null,
    currentRelatedwords: null,
    relatedwords: null
          }
        },
  methods:{
    swapWordfamily(payload){
      this.currentWordfamily = {word_family: payload.word_family,
      entryurl:payload.entryurl}
      this.wordfamily = wordfamily
    },
    swapRelatedwords(payload){
      console.log('gothere3')
      this.currentRelatedwords = {related_words: payload.related_words,
      entryurl:payload.entryurl}
      this.relatedwords = relatedwords
                              }
  },
  mounted(){
    EventBus.$on('wordfamily', this.swapWordfamily)
    EventBus.$on('relatedwords', this.swapRelatedwords)
           }
}
</script>
