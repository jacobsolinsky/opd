<template>
<div class="search-results">
<div class="english-search-result">
  <template v-for="kw in results">
  <div class="english-search-header">
    <div class="keyword">{{kw.name}}</div>
    <div class="distinguisher" v-if="kw.distinguisher">{{kw.distinguisher}}</div>
    <div class="pos-english">{{kw.pos}}</div>
    <div class="keyword-note"> <div class="stylized-text" v-if="kw.description" v-html="kw.description"></div></div>
  </div>
  <div class="english-search-contents">
    <div class="english-search-keyword-group" v-for="kwg in kw.keywordgroup_set">
      <div class="keyword-group">{{kwg.name}}</div>
      <div class="english-search-keyword-group-body">
          <mediumlink v-for="entry in kwg.mainentry_set"  :entry="entry"></mediumlink>

      </div>

      </div>
    </div>
  </template>
</div>
</div>
</template>
<script>
import mediumlink from "./mediumlink.vue"
export default {
  components: {mediumlink},
  props:['results']
}
</script>
