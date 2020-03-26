<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Subject - Object</th><th>0</th><th>0p</th></tr>
      <tr v-if="!details.plural_only"><th>Giin</th><td>{{forms['2']['0'].actor}}</td><td>{{forms['2']['0p'].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']['0'].actor}}</td><td>{{forms['21']['0p'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']['0'].actor}}</td><td>{{forms['2p']['0p'].actor}}</td></tr>
    </tbody>
  </table>
</template>
<script>
export default {
  props: ['forms', 'details'],
}
</script>
