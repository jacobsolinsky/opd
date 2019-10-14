<template>
  <div class="col-md-9 col-sm-9 content">
    <component :is="dynamicComponent" v-bind="currentProperties"></component>
  </div>
</template>
<script>
import mainpage from './mainpage.vue'
import searchresults from './searchresults.vue'
import mainentry from './mainentry.vue'
import login from './login.vue'
import {EventBus} from './event-bus.js'
export default {
  components: {mainpage, searchresults, mainentry, login},
  data() {
    return {
      dynamicComponent: `mainpage`,
      currentProperties: {}
    }
  },
  methods: {
    swapSearchresults(payload){
      this.currentProperties = {entries: payload}
      this.dynamicComponent = `searchresults`
    },
    swapMainentry(payload){
      this.currentProperties = {entry: payload}
      this.dynamicComponent = `mainentry`
    },
    swapLogin(payload){
      this.dynamicComponent = `login`
    }
  },
  mounted() {
    EventBus.$on('searchresults', this.swapSearchresults)
    EventBus.$on('mainentry', this.swapMainentry)
    EventBus.$on('login', this.swapLogin)
  }
}
</script>
