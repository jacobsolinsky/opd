<template>
  <span>
    <router-link v-if="!$store.state.loggedIn"  :to="'/users/sign-in'">Editor Login</router-link>
    <a v-if="$store.state.loggedIn"  v-on:click.stop.prevent="logout">Logout</a>
  </span>
</template>
<script>
import axios from 'axios';
export default {
  methods: {
    login(){
      EventBus.$emit('login')
    },
    logout(){
      this.$store.commit('logout')
      fetch('/get-csrf-token').
                  then(response => response.json()).
                  then(function(data) {
                    var csrftoken = data.token
                    var headers = {'X-CSRFToken': csrftoken};
                    axios.post('/logout',data,{headers: headers})
                  })
    }
  }
}
</script>
