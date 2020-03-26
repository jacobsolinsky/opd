<template>
  <b-card>
    <b-tabs card>
      <b-tab title="Immediate">
        <vaiimp :forms='forms.neutral.true' :details='details' v-if='details.type==="vai"'></vaiimp>
        <vtiimp :forms='forms.neutral.true' :details='details' v-if='details.type==="vti"'></vtiimp>
        <vtaimp :forms='forms.neutral.true' :details='details' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
      <b-tab title="Prohibitative">
        <vaiimp :forms='forms.prohibitative.true' :details='details' v-if='details.type==="vai"'></vaiimp>
        <vtiimp :forms='forms.prohibitative.true' :details='details' v-if='details.type==="vti"'></vtiimp>
        <vtaimp :forms='forms.prohibitative.true' :details='details' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
      <b-tab title="Delayed">
        <vaiimp :forms='forms.delayed.true' :details='details' v-if='details.type==="vai"'></vaiimp>
        <vtiimp :forms='forms.delayed.true' :details='details' v-if='details.type==="vti"'></vtiimp>
        <vtaimp :forms='forms.delayed.true' :details='details' v-if='details.type==="vta"'></vtaimp>
      </b-tab>
    </b-tabs>
  </b-card>
</template>
<script>
import vaiimp from './vaiimp.vue'
import vtiimp from './vtiimp.vue'
import vtaimp from './vtaimp.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['forms', 'details'],
  components: {vaiimp, vtiimp, vtaimp, BTab, BTabs, BCard},
}
</script>
