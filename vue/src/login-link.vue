<template>
  <router-link  :to="'/users/sign-in'">Editor Login</router-link>
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
