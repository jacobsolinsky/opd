<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Subject</th><th>Form</th></tr>
      <tr v-if="!details.plural_only"><th>0</th><td>{{forms['0']}}</td></tr>
      <tr v-if="!details.plural_only"><th>0'</th><td>{{forms["0'"]}}</td></tr>
      <tr><th>0p</th><td>{{forms['0p']}}</td></tr>
      <tr><th>0'p</th><td>{{forms["0'p"]}}</td></tr>
    </tbody>
  </table>
</template>
<script>
  export default {
    props: ['forms', 'details'],
  }
</script>
