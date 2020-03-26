<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Subject - Object</th><th>Wiin</th><th>Wiinawaa</th><th>3'</th></tr>
      <tr><th>Niin</th><td>{{forms['1']['3'].actor}}</td><td>{{forms['1']['3p'].actor}}</td><td>{{forms['1']["3'"].actor}}</td></tr>
      <tr><th>Giin</th><td>{{forms['2']['3'].actor}}</td><td>{{forms['2']['3p'].actor}}</td><td>{{forms['2']["3'"].actor}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['1p']['3'].actor}}</td><td>{{forms['1p']['3p'].actor}}</td><td>{{forms['1p']["3'"].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']['3'].actor}}</td><td>{{forms['21']['3p'].actor}}</td><td>{{forms['21']["3'"].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']['3'].actor}}</td><td>{{forms['2p']['3p'].actor}}</td><td>{{forms['2p']["3'"].actor}}</td></tr>
      <tr></tr>
      <tr><th>Subject - Object</th><th>3'</th></tr>
      <tr><th>Wiin</th><td>{{forms['3']["3'"].actor}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms['3p']["3'"].actor}}</td></tr>
      <tr><th>3'</th><td>{{forms["3'"].actor}}</td></tr>
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
