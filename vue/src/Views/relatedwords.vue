<template>
  <div>
  <h3>Related Words</h3>
  <div class="stylized-text">{{related_words.title}}</div>
    <div class="indent">
      <mediumlink v-for="w in related_words.mainentry_set" :entry="w"></mediumlink>
    </div>
  </div>
</template>
<script>
import mediumlink from './mediumlink.vue'
export default{
  props:['related_words', 'entryurl'],
  components: {mediumlink}
}
</script>
