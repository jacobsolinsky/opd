<template>
  <b-card>
    <b-tabs card>
      <b-tab title="Direct">
        <vtadirect :forms='forms' :details='details'></vtadirect>
      </b-tab>
      <b-tab title="Inverse">
        <vtainverse :forms='forms' :details='details'></vtainverse>
      </b-tab>
      <b-tab title="Indefinite Subject">
        <vtaindefinite :forms='forms' :details='details'></vtaindefinite>
      </b-tab>
      <b-tab title="Inanimate Subject">
        <vtainanimate :forms='forms' :details='details'></vtainanimate>
      </b-tab>
    </b-tabs>
  </b-card>
</template>
<script>
import vtadirect from './vtadirect.vue'
import vtainverse from './vtainverse.vue'
import vtaindefinite from './vtaindefinite.vue'
import vtainanimate from './vtainanimate.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['forms', 'details'],
  components: {vtadirect, vtainverse, vtaindefinite, vtainanimate, BTab, BTabs, BCard},
}

</script>
