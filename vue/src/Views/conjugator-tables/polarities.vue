<template>
  <b-card>
    <b-tabs card>
      <b-tab title="Positive">
        <vai :forms='forms.true' :details='details' v-if='details.type==="vai"'></vai>
        <vii :forms='forms.true' :details='details' v-if='details.type==="vii"'></vii>
        <vta :forms='forms.true' :details='details' v-if='details.type==="vta"'></vta>
        <vti :forms='forms.true' :details='details' v-if='details.type==="vti"'></vti>
        <vaio :forms='forms.true' :details='details' v-if='details.type==="vaio"'></vaio>
      </b-tab>
      <b-tab title="Negative">
        <vai :forms='forms.false' :details='details' v-if='details.type==="vai"'></vai>
        <vii :forms='forms.false' :details='details' v-if='details.type==="vii"'></vii>
        <vta :forms='forms.false' :details='details' v-if='details.type==="vta"'></vta>
        <vti :forms='forms.false' :details='details' v-if='details.type==="vti"'></vti>
        <vaio :forms='forms.false' :details='details' v-if='details.type==="vaio"'></vaio>
      </b-tab>
    </b-tabs>
  </b-card>
</template>
<script>
import vai from './vai.vue'
import vii from './vii.vue'
import vta from './vta.vue'
import vti from './vti.vue'
import vaio from './vaio.vue'
import {BTab, BTabs, BCard} from 'bootstrap-vue'
export default {
  props: ['forms', 'details'],
  components: {vai, vii, vta, vti, vaio, BTab, BTabs, BCard},
}

</script>
