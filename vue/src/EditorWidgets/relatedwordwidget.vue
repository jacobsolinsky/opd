<template>
  <div>
  <h3>Related Words</h3>
  <multiselect
  v-if="showOptions"
   :options="options" v-model="relatedwords" :optionsLimit="8" :custom-label="title">
   </multiselect>
   <template slot="option" slot-scope="props">
      {{props.option.title}}
  </template>
  <template slot="singleLabel" slot-scope="props">
    {{props.option.title}}
  </template>
  <div class="stylized-text">Related word family title
    <input type="text" v-model="relatedwords.title">
  </div>
    <div class="indent">
      <allentrieswidget v-for="(w, key) in relatedwords.mainentry_set" :entry="extract(w)"
      :key="key" @entryDelete="entryDelete"></allentrieswidget>
    </div>
    <button v-on:click.stop.prevent="add">Add entry to related words</button>


  </div>
</template>
<script>
import allentrieswidget from './allentrieswidget.vue'
import{Multiselect} from 'vue-multiselect'

export default{
  props:['relatedwords', 'entryurl'],
  components: {allentrieswidget, Multiselect},
  data() {
    return {
      options: [],
      showOptions: false
  }
  },
  created(){
    var self = this
    this.$store.dispatch('allRelatedwords')
    this.$store.state._allRelatedwords.then(
      data => {
        self.options = data
        self.showOptions = true
      }
    )
  },
  methods: {
    add(){
        this.relatedwords.mainentry_set.push({
            head_lemma:"",
            part_of_speech:""
        })
      },
      updateEntry(e){
        this.relatedwords.mainentry_set[e.index] = e.entry
      },
      entryDelete(index){
        console.log('index', index)
        this.relatedwords.mainentry_set.splice(index, 1)
      },
      extract(e){
        if (e.part_of_speech.hasOwnProperty('abbrev')){
          return {
            'head_lemma': e.head_lemma,
            'part_of_speech': e.part_of_speech.abbrev
          }
        }
        else {
          return e
        }
      },
      title(t){
        return t.title
      }
  }
}
</script>
