<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Object - Subject</th><th>Wiin</th><th>Wiinawaa</th></tr>
      <tr><th>Niin</th><td>{{forms['3']['1'].actor}}</td><td>{{forms['3p']['1'].actor}}</td></tr>
      <tr><th>Giin</th><td>{{forms['3']['2'].actor}}</td><td>{{forms['3p']['2'].actor}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['3']['1p'].actor}}</td><td>{{forms['3p']['1p'].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['3']['21'].actor}}</td><td>{{forms['3p']['21'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['3']['2p'].actor}}</td><td>{{forms['3p']['2p'].actor}}</td></tr>
      <tr></tr>
      <tr><th>Object - Subject</th><th>3'</th></tr>
      <tr><th>Wiin</th><td>{{forms["3'"]['3'].actor}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms["3'"]['3p'].actor}}</td></tr>
      <tr></tr>
      <tr><th>Object - Subject</th><th>Niin</th><th>Niinawind</th></tr>
      <tr><th>Giin</th><td>{{forms['1']['2'].actor}}</td><td>{{forms['1p']['2'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['1']['2p'].actor}}</td><td>{{forms['1p']['2p'].actor}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
