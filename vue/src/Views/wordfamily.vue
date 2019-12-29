<template>
  <div>
  <h3>Word Family</h3>
  <div class="word-family">
  <span :class="entryurl===word_family.head.url ?'word-family-child highlight' : 'word-family-child'">
    <mediumlink :entry="word_family.head"></mediumlink>
  </span>
      <div class="indent"><span :class="entryurl===pair.url ?'word-family-child highlight' : 'word-family-child'" v-for="pair in word_family.members" v-if="pair.kind !== 'head'">
        {{pair.kind}}<mediumlink :entry="pair.member"></mediumlink>
      </span></div></div>
  </div>
</template>
<script>
import mediumlink from './mediumlink.vue'
export default{
  components: {mediumlink},
  props:['word_family', 'entryurl']
}
</script>
