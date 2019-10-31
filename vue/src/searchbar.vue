<template>
<div id="searchbar" class="col-md-9 col-sm-9 section search-form">

    <h2>Search the dictionary <small><router-link to="/advanced_search">Advanced Search</router-link></small></h2>

      <div class="row search-form-row">
        <div class="col-md-9">
          <input type="text" v-model="q"  class="form-control search-input" placeholder="Search" v-on:keyup.enter="submit">
        </div>
        <div class="col-md-3">
          <input type="submit" name="commit" value="Search"  class="btn-submit" v-on:click="submit">
        </div>
      </div>
      <div class="row search-type">
        <div class="col-md-12">
          <label class="radio-inline">
            <input type="radio" v-model="type"  value="ojibwe">
            Search in Ojibwe
          </label>
          <label class="radio-inline">
            <input type="radio" v-model="type"  value="english">
            Search in English
          </label>
          <label class="radio-inline">
            <input type="radio" v-model="type"  value="collections">
            Search Cultural Collections
          </label>
          <span class="glyphicon glyphicon-question-sign" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Allows users to search and discover numerous Ojibwe artifacts, photographs and historical documents.">
        </span></div>
      </div>
</div>
</template>
<script>
export default {
  data(){return {
      q:"",
      type:"ojibwe",
    }
  },
  methods: {
    submit(){
      var self  = this;
       window.location.href = `/search?utf8=%E2%9C%93&q=${self.q}&commit=Search&type=${self.type}`;
    }
  }
}
</script>
