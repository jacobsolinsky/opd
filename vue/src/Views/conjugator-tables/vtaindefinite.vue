<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Object > Subject</th><th>Indefinite</th></tr>
      <tr><th>Niin</th><td>{{forms['X']['1'].goal}}</td></tr>
      <tr><th>Giin</th><td>{{forms['X']['2'].goal}}</td></tr>
      <tr><th>Wiin</th><td>{{forms['X']['3'].goal}}</td></tr>
      <tr><th>3'</th><td>{{forms['X']["3'"].goal}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms['X']['3p'].goal}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['X']['1p'].goal}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['X']['21'].goal}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['X']['2p'].goal}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
