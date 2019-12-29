<template>
  <div class="search-results">
    <wordpartlink v-for="wordpart in results" :wordpart="wordpart">
    </wordpartlink>
  </div>
</template>
<script>
import wordpartlink from './wordpartlink.vue'
export default {
  components: {wordpartlink},
  props: ['results']
}
