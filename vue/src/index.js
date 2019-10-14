import Vue from 'vue'
import searchbar from './searchbar.vue'
import content from './content.vue'
import sidebar from './sidebar.vue'
import carousel from './carousel.vue'
import loginlink from './login-link.vue'
console.log('Hello world');
new Vue({
  el: '#searchbar',
  render: h => h(searchbar),
});
new Vue({
  el: '#content',
  render: h => h(content),
});
new Vue({
  el: '#sidebar',
  render: h => h(sidebar),
});
new Vue({
  el: '#carousel-homepage',
  render: h => h(carousel),
});
new Vue({
  el: '#loginlink',
  render: h => h(loginlink),
});
