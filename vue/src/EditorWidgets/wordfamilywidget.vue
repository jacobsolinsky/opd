<template>
  <div>
  <h3>Word Family</h3>
  <div class="word-family">
  <span :class="entryurl===word_family.head.url ?'word-family-child highlight' : 'word-family-child'">
    <allentrieswidget :entry="extract(word_family.head)" @updateEntry="updateHeadEntry" :key="-1"></allentrieswidget>
  </span>
      <div class="indent"><span :class="entryurl===pair.url ?'word-family-child highlight' : 'word-family-child'" v-for="(pair, index) in word_family.members" v-if="pair.kind !== 'head'">
        <label>Word Type</label>
        <input type="text" v-model="pair.kind">
        <allentrieswidget :key="index" :entry="extract(pair.member)" @updateEntry="updateEntry" @entryDelete="entryDelete"></allentrieswidget>
      </span>
    </div>
    <button v-on:click.stop.prevent="add">Add entry to word family</button>
    </div>
  </div>
</template>
<script>
import allentrieswidget from './allentrieswidget.vue'
export default{
  components: {allentrieswidget},
  props:['word_family', 'entryurl'],
  methods: {
    add(){
      this.word_family.members.push({
          kind:"",
          member:{
          head_lemma:"",
          part_of_speech:""
        }
      })
    },
    entryDelete(index){
      this.word_family.members.splice(index, 1)
    },
    updateEntry(e){
      this.word_family.members[e.index] = e.entry
    },
    updateHeadEntry(e){
      this.word_family.head = e.entry
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
    }
  }
}
</script>
