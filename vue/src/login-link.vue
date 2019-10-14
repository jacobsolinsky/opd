<template>
  <a  v-on:click="login">Editor Login</a>
</template>
<script>
import { EventBus } from './event-bus.js';
export default {
  methods: {
    login(){
      EventBus.$emit('login')
    }
  }
}
</script>
