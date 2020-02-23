import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store.js'
import searchbar from './Views/searchbar.vue'
import advancedsearch from './Views/advancedsearch.vue'
import content from './Views/content.vue'
import sidebar from './Views/sidebar.vue'
import carousel from './Views/carousel.vue'
import loginlink from './Views/login-link.vue'
import mainpage from './Views/mainpage.vue'
import searchresults from './Views/searchresults.vue'
import englishsearchresults from './Views/englishsearchresults.vue'
import mainentry from './Views/mainentry.vue'
import mainentryedit from './EditViews/mainentryedit.vue'
import login from './Views/login.vue'
import collection from './Views/collection.vue'
import wordpart from './Views/wordpart.vue'
import CKEditor from '@ckeditor/ckeditor5-vue'
Vue.use(VueRouter)
Vue.use(CKEditor)
const routes = [
  {path:'/', component: mainpage},
  {path:'/users/sign-in', component: login},
  {path:'/main-entry/:entryurl', component: mainentry, props:true},
  {path:'/search', component: searchresults},
  {path:'/collection/:id', component: collection, props:true},
  {path:'/word-part/:entry', component: wordpart, props:true},
  {path:'/advanced_search', component:advancedsearch, props:true},
  {path:'/edit/main-entry/:entryurl', component: mainentryedit, props:true, beforeEnter(to, from, next){
    if (!store.state.loggedIn){
      fetch('/am-i-authenticated').
      then(response => response.json()).
      then( data => {
            if (data.value === "no") {
              store.commit('setBehindLogin', to.path)
              next('/users/sign-in')
            }
            else if (data.value === "yes"){
              store.commit('login')
              next()
            }
          }
        )

    }
    else{
      next()
    }
    }
  }

]
var router = new VueRouter({
  routes,
  mode:'history'
})
new Vue({
  el: '#content',
  router,
  store,
  components: {login, mainpage, mainentry, searchresults, englishsearchresults, collection, wordpart, advancedsearch},
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
  store,
  render: h => h(sidebar),
});
new Vue({
  el: '#carousel-homepage',
  render: h => h(carousel),
});
new Vue({
  el: '#loginlink',
  router,
  store,
  render: h => h(loginlink),
});
