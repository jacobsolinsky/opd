import Vue from 'vue'
import searchbar from './searchbar.vue'
console.log('Hello world');
new Vue({
  el: '#searchbar',
  render: h => h(searchbar),
});
