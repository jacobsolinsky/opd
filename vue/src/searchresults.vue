<template>
  <div class="search-results">
    <searchlink v-for="entry in entries" :entry="entry" :key="entry.url"></searchlink>
  </div>
</template>
<script>
import searchlink from './searchlink.vue'
export default {
  components: {searchlink},
  props:['entries']}
</script>
