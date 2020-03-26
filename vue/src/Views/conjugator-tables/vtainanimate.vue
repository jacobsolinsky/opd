<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Object > Subject</th><th>0</th><th>0p</th></tr>
      <tr><th>Niin</th><td>{{forms['0']['1'].actor}}</td><td>{{forms['0p']['1'].actor}}</td></tr>
      <tr><th>Giin</th><td>{{forms['0']['2'].actor}}</td><td>{{forms['0p']['2'].actor}}</td></tr>
      <tr><th>Wiin</th><td>{{forms['0']['3'].actor}}</td><td>{{forms['0p']['3'].actor}}</td></tr>
      <tr><th>3'</th><td>{{forms['0']["3'"].actor}}</td><td>{{forms['0p']["3'"].actor}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms['0']['3p'].actor}}</td><td>{{forms['0p']['3p'].actor}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['0']['1p'].actor}}</td><td>{{forms['0p']['1p'].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['0']['21'].actor}}</td><td>{{forms['0p']['21'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['0']['2p'].actor}}</td><td>{{forms['0p']['2p'].actor}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
