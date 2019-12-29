<template>
  <div class="search-results">
    <searchlink v-for="entry in results" :entry="entry" :key="entry.url"></searchlink>
  </div>
</template>
<script>
import searchlink from './searchlink.vue'
export default {
  components: {searchlink},
  props: ['results']
}
</script>
