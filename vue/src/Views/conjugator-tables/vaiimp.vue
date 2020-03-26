<template>
  <table class="conjugation-table">
    <tbody>
      <tr><th>Subject</th><th>Form</th></tr>
      <tr v-if="!details.plural_only"><th>Giin</th><td>{{forms['2']}}</td></tr>
      <tr><th>Giinawind</th><td>{{forms['21']}}</td></tr>
      <tr><th>Giinawaa</th><td>{{forms['2p']}}</td></tr>
    </tbody>
  </table>
</template>
<script>
export default {
  props: ['forms', 'details'],
}
</script>
