<template>
  <b-card>
    <b-tabs card>
      <b-tab title="Immediate">
        <vai :forms='forms.neutral.true' :details='{...details, imperative:true}' v-if='details.type==="vai"'></vai>
        <vti :forms='forms.neutral.true' :details='{...details, imperative:true}' v-if='details.type==="vti"'></vti>
        <vtaimp :forms='forms.neutral.true' :details='{...details, imperative:true}' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
      <b-tab title="Prohibitative">
        <vai :forms='forms.prohibitative.true' :details='{...details, imperative:true}' v-if='details.type==="vai"'></vai>
        <vti :forms='forms.prohibitative.true' :details='{...details, imperative:true}' v-if='details.type==="vti"'></vti>
        <vtaimp :forms='forms.prohibitative.true' :details='{...details, imperative:true}' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
      <b-tab title="Delayed">
        <vai :forms='forms.delayed.true' :details='{...details, imperative:true}' v-if='details.type==="vai"'></vai>
        <vti :forms='forms.delayed.true' :details='{...details, imperative:true}' v-if='details.type==="vti"'></vti>
        <vtaimp :forms='forms.delayed.true' :details='{...details, imperative:true}' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
    </b-tabs>
  </b-card>
</template>
<script>
import vai from './vai.vue'
import vti from './vti.vue'
import vtaimp from './vtaimp.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['forms', 'details'],
  components: {vai, vti, vtaimp, BTab, BTabs, BCard},
}
</script>
