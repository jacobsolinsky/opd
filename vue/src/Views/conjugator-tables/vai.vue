<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Subject</th><th>Form</th></tr>
      <tr v-if="!details.plural_only"><th>Niin</th><td>{{forms['1']}}</td></tr>
      <tr v-if="!details.plural_only"><th>Giin</th><td>{{forms['2']}}</td></tr>
      <tr v-if="!details.plural_only"><th>Wiin</th><td>{{forms['3']}}</td></tr>
      <tr><th>3'</th><td>{{forms["3'"]}}</td></tr>
      <tr><th>Wiinawaa</th><td>{{forms['3p']}}</td></tr>
      <tr><th>Niinawind</th><td>{{forms['1p']}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']}}</td></tr>
      <tr><th>X</th><td>{{forms['X']}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
