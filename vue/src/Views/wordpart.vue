<template>
<div>
        <h1 class="page-title">
  {{entry.title}}
  <span class="badge badge-oj">{{entry.initial}}</span>
</h1>

<dl>
  <dt>&nbsp;</dt>
    <dd><div class="stylized-text">{{entry.gloss}}</div></dd>
    <dt>&nbsp;</dt>

  <dt>Type:</dt>
  <dd>{{entry.type}}</dd>
  <dt v-if="entry.subtypes">Subtypes:</dt>
    <dd>{{entry.subtypes}}</dd>
  <dt v-if="entry.variants">Variants:</dt>
    <dd><div class="stylized-text">{{entry.variants}}</div></dd>
</dl>

<div class="panel panel-oj">
  <div class="panel-heading" role="tab" id="mainEntriesHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#mainEntries" aria-expanded="true" aria-controls="mainEntries">
        <span class="caret"></span>
        Words that use this part:
      </a>
    </h4>
  </div>
  <div id="mainEntries"  class="panel-collapse collapse in" role="tabpanel" aria-labelledby="mainEntriesHeader" aria-expanded="true">
    <div class="panel-body">
      <table class="table table-hover">
<tbody><tr v-for="e in entry.words_that_use_this_part">
          <td> <mediumlink :entry="e"></mediumlink></td>
        </tr></tbody></table>
    </div>
  </div>
</div>
</div>

</template>
<script>
import mediumlink from './mediumlink.vue'
export default {
  components: {mediumlink},
  props : ["entry"],
  mounted() {
    var self = this
    fetch(`/json/word-part/${self.entry}`)
      .then(response => response.json())
      .then(data => {self.entry = data})
    }
  }
</script>
