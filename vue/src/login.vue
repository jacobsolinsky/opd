<template>
<div v-on:keyup.enter="submit">
<h2>Sign in</h2>
<div class="form-group row full-row">
    <label class="col-sm-2 control-label" for="user_email">Username</label>
    <div class="col-sm-6">
        <input autofocus="autofocus" class="form-control" type="email" value="" v-model="email" id="user_email">
    </div>
</div>

<div class="form-group row full-row">
    <label class="col-sm-2 control-label" for="user_password">Password{{password}}</label>
    <div class="col-sm-6">
        <input autocomplete="off" class="form-control" type="password" v-model="password" id="user_password">
    </div>
</div>

<div class="form-group row full-row">
    <div class="col-sm-6 col-sm-offset-2">
        <input type="submit" v-on:click="submit" value="Sign in" class="btn btn-primary">
    </div>
</div>
</div>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    var thing =  {
      email:'',
      password:'',
      csrftoken: ''
    }
    fetch('/vue/get-csrf-token').
                then(response => response.json()).
                then(function(data) { thing.csrftoken = data.token})
    console.log(thing.csrftoken)
    return thing
  },
  methods :{
  submit: function() {
    var data =  {username: this.email, password: this.password}; // The exact data doesn't matter
    var csrftoken = this.csrftoken; // Using JS Cookies library
    console.log(this.csrftoken)
    var headers = {'X-CSRFToken': csrftoken};
    axios.post('/vue/login',data,{headers: headers});
  }
}
}
</script>
