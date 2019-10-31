import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import searchbar from './searchbar.vue'
import advancedsearch from './advancedsearch.vue'
import content from './content.vue'
import sidebar from './sidebar.vue'
import carousel from './carousel.vue'
import loginlink from './login-link.vue'
import mainpage from './mainpage.vue'
import searchresults from './searchresults.vue'
import mainentry from './mainentry.vue'
import mainentryedit from './mainentryedit.vue'
import login from './login.vue'
import collection from './collection.vue'
import wordpart from './wordpart.vue'
import CKEditor from '@ckeditor/ckeditor5-vue'
Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(VueMaterial)
Vue.use(CKEditor)
const store = new Vuex.Store({
  loggedin : false
})
const routes = [
  {path:'/', component: mainpage},
  {path:'/users/sign-in', component: login},
  {path:'/main-entry/:entry', component: mainentry, props:true},
  {path:'/edit/main-entry/:entry', component: mainentryedit, props:true},
  {path:'/search', component: searchresults, props:true},
  {path:'/collection/:id', component: collection, props:true},
  {path:'/word-part/:entry', component: wordpart, props:true},
  {path:'/advanced_search', component:advancedsearch, props:true}
]
var router = new VueRouter({
  routes,
  mode:'history'
})
new Vue({
  el: '#content',
  router,
  components: {login, mainpage, mainentry, searchresults, collection, wordpart, advancedsearch},
  render: h => h(content)
})
new Vue({
  el: '#searchbar',
  router,
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
