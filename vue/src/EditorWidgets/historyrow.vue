<template>
  <a v-on:click.stop.prevent="restore">
    Restore version from: {{thisdate}}
  </a>
</template>
<script>
import axios from 'axios'
export default {
  props: ['history'],
  computed:{
    thisdate() {
      return Date(history.creation_date).toString()
    }
  },
  created(){
    var self = this
    fetch('/get-csrf-token').
                then(response => response.json()).
                then(function(data) { self.csrftoken = data.token
                })
  },
  methods: {
    restore(){
      var self = this
      var headers = {'X-CSRFToken': this.csrftoken};
      axios.post(`/history/${self.history.historic_entry}`,submitval,{headers: headers})
    }
  }
}
</script>
