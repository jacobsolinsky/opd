<template>
<div>
<h1 class="page-title">{{data.title}}</h1>
<p></p><div class="stylized-text">{{data.copyright}}</div><p></p>
<dl>
  <dt>Description:</dt>
  <dd><div class="stylized-text">{{data.description}}</div></dd>
</dl>
<div v-if="data.type==='image'">
<img class="full-image" :src="data.image.src" :alt="data.image.alt">
</div>
<div v-if="data.type==='document'">
<blockquote>
  <div class="stylized-text">{{data.body}}</div>
  <div class="bibliography">from <div class="stylized-text">{{data.bibliography}}</div></div>
</blockquote>
</div>
<div v-if="data.type==='video'">
  <div id="video-player" class="video-player" data-file="">
      <img src="data.image.src" width="640px" height="360px">
      <span class="glyphicon glyphicon-play play-button"></span>
    </div>
</div>
<p></p>
</div>
</template>
<script>
export default {
  props:['id'],
  data(){
    return {data:null}
  },
  mounted(){
    var self  = this
    fetch(`/json/collection/${self.id}`)
    .then(response => response.json())
    .then(data => self.data = data)
  }
}
</script>
