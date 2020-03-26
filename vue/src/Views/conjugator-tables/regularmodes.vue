<template>
  <b-card>
    <b-tabs card>
      <b-tab title="Neutral">
        <polarities :forms='forms.neutral' :details='details'></polarities>
      </b-tab>
      <b-tab title="Preterite">
        <polarities :forms='forms.preterite' :details='details'></polarities>
      </b-tab>
      <b-tab title="Dubitative">
        <polarities :forms='forms.dubitative' :details='details'></polarities>
      </b-tab>
      <b-tab title="Preterite-dubitative">
        <polarities :forms='forms["preterite-dubitative"]' :details='details'></polarities>
      </b-tab>
    </b-tabs>
  </b-card>
</template>
<script>
import polarities from './polarities.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['forms', 'details'],
  components: {polarities, BTab, BTabs, BCard},
}
</script>
