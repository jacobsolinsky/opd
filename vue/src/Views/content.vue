<template>
  <div class="col-md-9 col-sm-9 content">
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>
<script>
export default {}
</script>
