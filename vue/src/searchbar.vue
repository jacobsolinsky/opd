<template>
<div id="searchbar">
  <div v-on:click="submit">
  {{type + "aa"}}
</div>
<form>

      <div class="row search-form-row">
        <div class="col-md-9">
          <input type="text" v-model="q"  class="form-control search-input" placeholder="Search">
        </div>
        <div class="col-md-3">
          <input type="submit" name="commit" value="Search"  class="btn-submit">
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
</form>
</div>
</template>
<script>
export default {
  data(){return {
    q:"",
    type:"ojibwe",
  }},
  methods: {
    submit: function(){
      var self = this;
      fetch(`json/search?utf8=%E2%9C%93&q=${self.q}&commit=Search&type=${self.type}`).
      then(response => response.json()).
      then(data => console.log(data))
    }
  }
}
</script>
