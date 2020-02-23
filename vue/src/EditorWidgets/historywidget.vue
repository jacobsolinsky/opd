<template>
  <ul>
    <historyrow v-for="(history, key) in historyset.history_set" :history="history" :key="key">
    </historyrow>
  </ul>
</template>
<script>
import historyrow from './historyrow.vue'
export default {
  props: ["historyset"],
  components: {historyrow}
}
</script>
