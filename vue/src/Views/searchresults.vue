<template>
  <englishsearchresults v-if="this.$route.query.type==='english'" :results="results"></englishsearchresults>
  <ojibwesearchresults v-else-if="['ojibwe','main_entry'].includes(this.$route.query.type)" :results="results"></ojibwesearchresults>
  <collectionsearchresults v-else-if="this.$route.query.type==='collections'" :results="results"></collectionsearchresults>
  <wordpartsearchresults v-else-if="this.$route.query.type==='word_part'" :results="results"></wordpartsearchresults>
</template>
<script>
import englishsearchresults from './englishsearchresults.vue'
import ojibwesearchresults from './ojibwesearchresults.vue'
import collectionsearchresults from './collectionsearchresults.vue'
import wordpartsearchresults from './wordpartsearchresults.vue'
function jsonToQueryString(json) {
    return '?' +
        Object.keys(json).map(function(key) {
            return encodeURIComponent(key) + '=' +
                encodeURIComponent(json[key]);
        }).join('&');
}
export default {
  components: {englishsearchresults, ojibwesearchresults,
               collectionsearchresults, wordpartsearchresults},
  props: ['entries'],
  data(){
    return {results: null}
  },
  beforeMount(){
    var self = this;
    fetch(`/json/search${jsonToQueryString(self.$route.query)}`)
      .then(results => results.json())
      .then(data => {self.results = data})
  },
  watch: {
     $route (to, from){
       console.log('abba')
       var self = this;
       fetch(`/json/search${jsonToQueryString(self.$route.query)}`)
         .then(results => results.json())
         .then(data => {self.results = data})
     }
  }
}
</script>
