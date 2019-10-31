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
              <option value="starts_with">starts with</option>
              <option value="exact">exact match</option>
              <option value="contains">contains</option>
              <option value="ends_with">ends with</option>
              <option value="inexact">is similar to</option>
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
  <searchresults :entries="entries"></searchresults>
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
      scope: "exact",
      q: "",
      entries: []
    }
  },
  mounted(){
    this.type = this.$route.query.type
    this.field = this.$route.query.field
    this.scope = this.$route.query.scope
    this.q = this.$route.query.q
    advancedSearch()
  },
  methods: {
    advancedSearch(){
      var self = this;
      fetch(`/json/search${jsonToQueryString(self.$data)}`)
        .then(results => results.json())
        .then(data => {self.entries = data})
    }
  }
}
</script>
