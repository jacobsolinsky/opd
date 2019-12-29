<template>
  <div>
  <div>
    <div class="panel panel-oj">
      <div class="panel-heading">
        <h4 class="panel-title">Advanced Search</h4>
      </div><div class="panel-body">
        <form action="/advanced_search" class="form-inline" v-on:submit.stop.prevent="advancedSearch">
          <div class="form-group">
            <span>Search </span>
            <select class="form-control" v-model="type">
              <option selected="" value="main_entry">Ojibwe Entries</option>
              <option value="keyword">English Keywords</option>
              <option value="word_part">Word Parts</option>
            </select>
          </div>
          <div class="form-group">
            <span>&nbsp;by </span>
            <select class="form-control" v-model="field">
              <option value="lemma">Lemma</option>
              <option value="stem">Stem</option>
            </select>
          </div>
          <div class="form-group">
            <span>&nbsp;which </span>
            <select class="form-control" v-model="scope">
              <option value="starts_with">start with</option>
              <option value="exact">exactly match</option>
              <option value="contains">contain</option>
              <option value="ends_with">end with</option>
              <option value="inexact">are similar to</option>
            </select>
            <span>&nbsp;</span>
          </div>
          <div class="form-group">
            <input type="text" placeholder="Search" class="form-control" v-model="q" size="14">
          </div>
          <div class="pull-right">
            <input type="submit">
          </div>
        </form>
      </div>
    </div>
  </div>
  <searchresults :results="results" :key="key"></searchresults>
</div>
</template>
<script>
import searchresults from './searchresults.vue'
function jsonToQueryString(json) {
    return '?' +
        Object.keys(json).map(function(key) {
            return encodeURIComponent(key) + '=' +
                encodeURIComponent(json[key]);
        }).join('&');
}
export default {
  components: {searchresults},
  data(){
    return {
      type: "main_entry",
      field: "lemma",
      scope: "inexact",
      q: "",
      entries: []
    }
  },
  beforeMount(){
    if (this.$route.query.type){this.type = this.$route.query.type}
    if (this.$route.query.field){this.field = this.$route.query.field}
    if (this.$route.query.scope){this.scope = this.$route.query.scope}
    if (this.$route.query.q){this.q = this.$route.query.q}
    this.key=1
    advancedSearch()
  },
  methods: {
    advancedSearch(){
      this.$router.replace(`/advanced_search${jsonToQueryString(this.$data)}`)
      this.key += 1
    }
  }
}
</script>
