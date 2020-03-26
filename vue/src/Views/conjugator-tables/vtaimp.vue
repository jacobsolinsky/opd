<template>
  <table>
    <tbody class="conjugation-table">
      <tr><th>Subject - Object</th><th>Wiin</th><th>Wiinawaa</th><th>3'</th></tr>
      <tr><th>Giin</th><td>{{forms['2']['3'].actor}}</td><td>{{forms['2']['3p'].actor}}</td><td>{{forms['2']["3'"].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']['3'].actor}}</td><td>{{forms['21']['3p'].actor}}</td><td>{{forms['21']["3'"].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']['3'].actor}}</td><td>{{forms['2p']['3p'].actor}}</td><td>{{forms['2p']["3'"].actor}}</td></tr>
      <tr></tr>
      <tr><th>Subject - Object</th><th>Niin</th><th>Niinawind</th></tr>
      <tr><th>Giin</th><td>{{forms['2']['1'].actor}}</td><td>{{forms['2']['1p'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']['1'].actor}}</td><td>{{forms['2p']['1p'].actor}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
