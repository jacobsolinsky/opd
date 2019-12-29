<template>
  <div class="search-results">
    <collectionlink v-for="collection in results" :collection="collection"></collectionlink>
  </div>
</template>
<script>
import collectionlink from './collectionlink.vue'
export default {props:['results'], components:{collectionlink}}
</script>
