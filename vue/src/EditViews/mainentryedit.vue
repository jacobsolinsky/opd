<template>

  <div v-if="entry.url">
  <router-link  to="/edit/main-entry/new">Create new entry</router-link>
  <h3>
    <div class="pull-right index-photo"><img v-if="entry.head_image" class="collection-image index-photo" :alt="entry.head_image.alt" :src="entry.head_image.src"></div>
    <input type="text" class="lemma" v-model="entry.head_lemma">

    <partofspeechwidget :partofspeech="entry.part_of_speech" @updatePartofspeech="updatePartofspeech"></partofspeechwidget>

    <button v-show="!flags.audiorec" v-on:click.stop.prevent="addAudiorec"> Add main recording for entry </button>
    <div v-show="flags.audiorec" v-if="entry.head_speaker">
      <audiorec :audiorec="{speaker:entry.head_speaker, audio:entry.head_audio}"
      @audiorecDelete="audiorecDelete"></audiorec>
    </div>
  </h3>

  <div class="editor-panel">
  <button v-show="!flags.gloss" v-on:click.stop.prevent="addGloss"> Add gloss </button>
  <div v-show="flags.gloss">
    <button  v-on:click.stop.prevent="glossDelete"> Delete gloss </button>
    <ckeditor :editor="editor" v-model="entry.gloss"></ckeditor>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.notes" v-on:click.stop.prevent="addNotes"> Add notes </button>
  <div v-show="flags.notes">
    <button  v-on:click.stop.prevent="notesDelete"> Delete notes </button>
    <strong>Note:</strong>
    <br>
    <ckeditor :editor="editor" v-model="entry.notes"></ckeditor>
    <div v-html="entry.notes"></div>
  </div>
  </div>


  <div class="editor-panel">
  <button v-show="!flags.inflectionalform_set" v-on:click.stop.prevent="addInflectionalform_set"> Add inflectional forms table </button>
  <div v-show="flags.inflectionalform_set">
  <button  v-on:click.stop.prevent="inflectionalform_setDelete"> Delete inflectional forms table </button>
  <inflectionalformwidget :formlist="entry.inflectionalform_set"></inflectionalformwidget>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.stem" v-on:click.stop.prevent="addStem"> Add stem </button>
  <div v-show="flags.stem">
  <button v-on:click.stop.prevent="stemDelete"> Delete stem </button>
  <input type="text" v-model="entry.stem">
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.basic_audio" v-on:click.stop.prevent="addBasicaudio"> Add audio for basic forms table </button>
  <div v-show="flags.basic_audio" >
  <button  v-on:click.stop.prevent="basicaudioDelete"> Delete basic audio forms table </button>
  <audioformswidget :title="'Audio for Basic Forms'" :audioforms="entry.basic_audio" @updateAudioforms="updateBasicaudio"></audioformswidget>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.additional_audio" v-on:click.stop.prevent="addAdditionalaudio"> Add additional audio forms table </button>
  <div v-show="flags.additional_audio" >
  <button  v-on:click.stop.prevent="additionalaudioDelete"> Delete additional audio forms table </button>
  <audioformswidget :title="'Additional Audio'"  :audioforms="entry.additional_audio" @updateAudioforms="updateAdditionalaudio"></audioformswidget>
  </div>
  </div>


  <div class="editor-panel">
  <button v-show="!flags.sentence_examples" v-on:click.stop.prevent="addSentence_examples"> Add sentence examples table </button>
  <div v-show="flags.sentence_examples">
  <button  v-on:click.stop.prevent="sentence_examplesDelete"> Delete sentence examples table </button>
  <sentenceexampleswidget :sentenceexamples="entry.sentence_examples"></sentenceexampleswidget>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.word_parts" v-on:click.stop.prevent="addWord_parts"> Add word parts </button>
  <div v-show="flags.word_parts">
  <button  v-on:click.stop.prevent="word_partsDelete"> Delete word parts </button>
  <ckeditor :editor="editor" v-model="entry.word_parts"></ckeditor>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.reduplication" v-on:click.stop.prevent="addReduplication"> Add reduplication </button>
  <div v-show="flags.reduplication">
  <button  v-on:click.stop.prevent="reduplicationDelete"> Delete reduplication </button>
  <input type="text" v-model="entry.reduplication">
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.imageresource_set" v-on:click.stop.prevent="addImageresource_set"> Add image resources table </button>
  <div v-show="flags.imageresource_set">
  <button  v-on:click.stop.prevent="imageresource_setDelete"> Delete image resources table </button>
  <imageresourcesetwidget :imageresourceset="entry.imageresource_set"></imageresourcesetwidget>
  </div>
  </div>


  <div class="editor-panel">
  <button v-show="!flags.videoresource_set" v-on:click.stop.prevent="addVideoresource_set"> Add video resources table </button>
  <div v-show="flags.videoresource_set">
  <button  v-on:click.stop.prevent="videoresource_setDelete"> Delete video resources table </button>
  <videoresourcesetwidget :videoresourceset="entry.videoresource_set"></videoresourcesetwidget>
  </div>
  </div>

  <div class="editor-panel">
  <button v-show="!flags.documentresource_set" v-on:click.stop.prevent="addDocumentresource_set"> Add document resources table </button>
  <div v-show="flags.documentresource_set">
  <button  v-on:click.stop.prevent="documentresource_setDelete"> Delete document resources table </button>
  <documentresourcesetwidget :documentresourceset="entry.documentresource_set"></documentresourcesetwidget>
  </div>
  </div>

  <button v-on:click="submit">Submit</button>
  <historywidget :historyset="entry.history_set"></historywidget>
  </div>
</template>
<script>
import { EventBus } from '../Views/event-bus.js';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import axios from 'axios';
import partofspeechwidget from '../EditorWidgets/partofspeechwidget.vue'
import speakerwidget from '../EditorWidgets/speakerwidget.vue'
import inflectionalformwidget from '../EditorWidgets/inflectionalformwidget.vue'
import audioformswidget from '../EditorWidgets/audioformswidget.vue'
import audiorec from '../EditorWidgets/audiorec.vue'
import sentenceexampleswidget from '../EditorWidgets/sentenceexampleswidget.vue'
import imageresourcesetwidget from '../EditorWidgets/imageresourcesetwidget.vue'
import videoresourcesetwidget from '../EditorWidgets/videoresourcesetwidget.vue'
import documentresourcesetwidget from '../EditorWidgets/documentresourcesetwidget.vue'
import allentrieswidget from '../EditorWidgets/allentrieswidget.vue'
import historywidget from '../EditorWidgets/historywidget.vue'

var csrftoken = 1
export default {
  components: {partofspeechwidget, inflectionalformwidget, speakerwidget,
  audioformswidget, audiorec, sentenceexampleswidget, imageresourcesetwidget,
  videoresourcesetwidget, documentresourcesetwidget, allentrieswidget,
  historywidget},
  data(){
    return {
      entry:{url:"url", head_lemma:"lemma"},
      editor: ClassicEditor}
  },
  computed: {
    flags(){
      return {
      notes: this.entry.hasOwnProperty('notes'),
      gloss: this.entry.hasOwnProperty('gloss'),
      audiorec: this.entry.hasOwnProperty('head_speaker'),
      head_image: this.entry.hasOwnProperty('head_image'),
      word_parts: this.entry.hasOwnProperty('word_parts'),
      reduplication: this.entry.hasOwnProperty('reduplication'),
      stem: this.entry.hasOwnProperty('stem'),
      inflectionalform_set: this.entry.hasOwnProperty('inflectionalform_set'),
      region: this.entry.hasOwnProperty('region'),
      basic_audio: this.entry.hasOwnProperty('basic_audio'),
      additional_audio: this.entry.hasOwnProperty('additional_audio'),
      sentence_examples: this.entry.hasOwnProperty('sentence_examples'),
      imageresource_set: this.entry.hasOwnProperty('imageresource_set'),
      videoresource_set: this.entry.hasOwnProperty('videoresource_set'),
      documentresource_set: this.entry.hasOwnProperty('documentresource_set')
      }
    }
  },
  created(){
    var self = this
    fetch('/get-csrf-token').
                then(response => response.json()).
                then(function(data) { self.csrftoken = data.token})
  },
  beforeRouteEnter(to, from, next) {
    var entryurl = to.params.entryurl
    if (entryurl === "new") {
      next()
    }
    else{
      EventBus.$emit("edit")
      fetch(`/json/main-entry/${to.params.entryurl}`)
        .then(response => response.json())
        .then(data => {
          if (data.related_words){
            console.log('editedrelatedwords')
            EventBus.$emit('editrelatedwords',
            {'related_words':data.related_words,
             'entryurl': data.url})
            }
          if (data.word_family){
          EventBus.$emit('editwordfamily',
          {'word_family':data.word_family,
           'entryurl': data.url})
          }
          next(vm => vm.entry = data)
        })
    }
  },
  beforeRouteUpdate(to, from, next) {
    EventBus.$emit("edit")
    var entryurl = to.params.entryurl
    if (entryurl === "new") {
      next()
    }
    else {
    fetch(`/json/main-entry/${to.params.entryurl}`)
      .then(response => response.json())
      .then(data => {
        if (data.related_words){
          console.log('editedrelatedwords')
          EventBus.$emit('editrelatedwords',
          {'related_words':data.related_words,
           'entryurl': data.url})
          }
        if (data.word_family){
        EventBus.$emit('editwordfamily',
        {'word_family':data.word_family,
         'entryurl': data.url})
        }
        this.entry = data
      })
    }
  },
    methods: {
      submit(){
        const submitval =  (({
          head_lemma, part_of_speech, notes, gloss, audiorec, head_image, word_parts, reduplication, stem,
          inflectionalform_set, region, basic_audio, additional_audio,
          sentence_examples, imageresource_set, videoresource_set,documentresource_set
        }) => ({
          head_lemma, part_of_speech, notes, gloss, audiorec, head_image, word_parts, reduplication, stem,
          inflectionalform_set, region, basic_audio, additional_audio,
          sentence_examples, imageresource_set, videoresource_set,documentresource_set
        }))(this.entry)
        var self = this
        var headers = {'X-CSRFToken': this.csrftoken};
        axios.post(`/api/main-entry`,submitval,{headers: headers})
      },
      updatePartofspeech(e){
        this.entry.part_of_speech=e
      },
      updateBasicaudio(e){
        this.entry.basic_audio=e
      },
      updateAdditionalaudio(e){
        this.entry.additional_audio=e
      },
      updateSentenceexamples(e){
        this.entry.sentence_examples=e
      },
      audiorecDelete(){
        this.$delete(this.entry, "head_speaker")
        this.$delete(this.entry, "head_audio")
      },
      addAudiorec(){
        this.$set(this.entry, "head_speaker", {"initials":"Choose Speaker",
                                                "primary_name": ""})
        this.$set(this.entry, "head_audio", {})
      },
      addNotes(){this.$set(this.entry, "notes", "")},
      notesDelete(){this.$delete(this.entry, "notes")},
      addGloss(){this.$set(this.entry, "gloss", "")},
      glossDelete(){this.$delete(this.entry, "gloss")},
      addHead_image(){this.$set(this.entry, "head_image", {})},
      head_imageDelete(){this.$delete(this.entry, "head_image")},
      addWord_parts(){this.$set(this.entry, "word_parts", "")},
      word_partsDelete(){this.$delete(this.entry, "word_parts")},
      addReduplication(){this.$set(this.entry, "reduplication", "")},
      reduplicationDelete(){this.$delete(this.entry, "reduplication")},
      addInflectionalform_set(){this.$set(this.entry, "inflectionalform_set", [])},
      inflectionalform_setDelete(){this.$delete(this.entry, "inflectionalform_set")},
      addStem(){this.$set(this.entry, "stem", "")},
      stemDelete(){this.$delete(this.entry, "stem")},
      addRegion(){this.$set(this.entry, "region", [])},
      regionDelete(){this.$delete(this.entry, "region")},
      addBasicaudio(){this.$set(this.entry, "basic_audio", [])},
      basicaudioDelete(){this.$delete(this.entry, "basic_audio")},
      addAdditionalaudio(){this.$set(this.entry, "additional_audio", [])},
      additionalaudioDelete(){this.$delete(this.entry, "additional_audio")},
      addSentence_examples(){this.$set(this.entry, "sentence_examples", [])},
      sentence_examplesDelete(){this.$delete(this.entry, "sentence_examples")},
      addImageresource_set(){this.$set(this.entry, "imageresource_set", [])},
      imageresource_setDelete(){this.$delete(this.entry, "imageresource_set")},
      addVideoresource_set(){this.$set(this.entry, "videoresource_set", [])},
      videoresource_setDelete(){this.$delete(this.entry, "videoresource_set")},
      addDocumentresource_set(){this.$set(this.entry, "documentresource_set", [])},
      documentresource_setDelete(){this.$delete(this.entry, "documentresource_set")}
    }
}
</script>
<style>
.editor-panel{
    background: #F6F1EE;
    border: 1px solid #F6F1EE;
    padding: 0 6px 6px 6px;
    border-radius: 0;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    margin-bottom: 20px;
    box-sizing: border-box;
}
</style>
