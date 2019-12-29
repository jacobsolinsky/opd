<template>
  <div class="word-part-search-result">
    <a href="/word-part/kaa-final-1304">{wordpart.title}</a>
  <span class="badge badge-oj">{{wordpart.type}}</span>
  <div class="stylized-text"><div v-html="wordpart.gloss"></div></div>
</div>
</template>
<script>
export default {props:['wordpart']}
</script>
