<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Object > Subject</th><th>0</th><th>0p</th></tr>
      <tr><th>Niin</th><td>{{forms['1']['0'].actor}}</td><td>{{forms['1']['0p'].actor}}</td></tr>
      <tr><th>Giin</th><td>{{forms['2']['0'].actor}}</td><td>{{forms['2']['0p'].actor}}</td></tr>
      <tr><th>Wiin</th><td>{{forms['3']['0'].actor}}</td><td>{{forms['3']['0p'].actor}}</td></tr>
      <tr><th>3'</th><td>{{forms["3'"]['0'].actor}}</td><td>{{forms["3'"]['0p'].actor}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms['3p']['0'].actor}}</td><td>{{forms['3p']['0p'].actor}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['1p']['0'].actor}}</td><td>{{forms['1p']['0p'].actor}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']['0'].actor}}</td><td>{{forms['21']['0p'].actor}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']['0'].actor}}</td><td>{{forms['2p']['0p'].actor}}</td></tr>
      <tr><th>Indefinite</th><td>{{forms['X']['0'].actor}}</td><td>{{forms['X']['0p'].actor}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
