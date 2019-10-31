import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import searchbar from './searchbar.vue'
import content from './content.vue'
import sidebar from './sidebar.vue'
import carousel from './carousel.vue'
import loginlink from './login-link.vue'
import mainpage from './mainpage.vue'
import searchresults from './searchresults.vue'
import mainentry from './mainentry.vue'
import login from './login.vue'
import collection from './collection.vue'
import wordpart from './wordpart.vue'
Vue.use(VueRouter)
Vue.use(Vuex)
const store = new Vuex.Store({
  loggedin : false
})
const routes = [
  {path:'/vue/', component: mainpage},
  {path:'/vue/users/sign-in', component: login},
  {path:'/vue/main-entry/:entry', component: mainentry, props:true},
  {path:'/vue/search', component: searchresults, props:true},
  {path:'/vue/collection/:id', component: collection, props:true},
  {path:'/vue/word-part/:entry', component: wordpart, props:true}
]
var router = new VueRouter({
  routes,
  mode:'history'
})
new Vue({
  el: '#content',
  router,
  components: {login, mainpage, mainentry, searchresults, collection},
  render: h => h(content)
})
new Vue({
  el: '#searchbar',
  render: h => h(searchbar),
});
new Vue({
  el: '#sidebar',
  router,
  render: h => h(sidebar),
});
new Vue({
  el: '#carousel-homepage',
  render: h => h(carousel),
});
new Vue({
  el: '#loginlink',
  router,
  render: h => h(loginlink),
});
