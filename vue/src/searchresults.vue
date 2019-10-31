<template>
  <div class="search-results">
    <searchlink v-for="entry in entries" :entry="entry" :key="entry.url"></searchlink>
  </div>
</template>
<script>
import searchlink from './searchlink.vue'
function jsonToQueryString(json) {
    return '?' +
        Object.keys(json).map(function(key) {
            return encodeURIComponent(key) + '=' +
                encodeURIComponent(json[key]);
        }).join('&');
}
export default {
  components: {searchlink},
  props: ['entries'],
  mounted(){
    var self = this;
    fetch(`/vue/json/search${jsonToQueryString(self.$route.query)}`)
      .then(results => results.json())
      .then(data => {self.entries = data})
  }
}
</script>
