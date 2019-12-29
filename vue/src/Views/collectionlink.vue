<template>
<dl class="dl-horizontal no-margin">
  <dt>
    <a v-if="['image', 'video'].includes(collection.type)" class="image" :href="collection.url"><img src=""></a>
    <a v-else-if="collection.type==='document'" class="image" :href="collection.url"><span class="glyphicon glyphicon glyphicon-duplicate"></span></a>
  </dt>
<dd>
<a :href="collection.url">{{collection.title}}</a>
</dd>
</dl>
</template>
<script>
export default{props:['collection']}
</script>
