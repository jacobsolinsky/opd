<template>
<div>
<h3>
  <div class="pull-right index-photo"><img v-if="entry.head_image" class="collection-image index-photo" :alt="entry.head_image.alt" :src="entry.head_image.src"></div>
  <span class="lemma">{{entry.head_lemma}}</span>
  <span class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="entry.part_of_speech.full">{{entry.part_of_speech.abbrev}}</span>
    <a v-if="entry.head_speaker" :href="entry.head_speaker.href" class="speaker-initials" data-toggle="modal" data-target="#voiceModal" data-remote="false">
      {{entry.head_speaker.initials}}</a>
       <span v-if="entry.head_audio" class="badge badge-oj badge-audio-player">
      <div id="audio-player-116840" class="audio-player" :data-file="entry.head_audio.regular" :data-mobile-file="entry.head_audio.regular">
        <span class="glyphicon glyphicon-volume-up glyphicon-audio-player"></span>
        Listen
      </div>
    </span>
</h3>
<p v-if="entry.region.length>0" class="regions">
<span v-for="r in entry.region" class="badge badge-oj" data-toggle="tooltip" data-placement="right" title="" :data-original-title="r.full">{{r.abbrev}}</span>
</p>

<div v-html="entry.gloss" style="display: inline;"></div>

<div v-if="entry.notes">
  <strong>Note:</strong>
  <br>
  <div v-html="entry.notes"></div>
</div>

<p v-if="entry.inflectionalform_set.length>0" class="inflectional-forms">
  <div v-for="form in entry.inflectionalform_set" style="display: inline;">
  <strong >
    {{form.form}}
  </strong>
    <span  v-for="pos in form.poss" data-toggle="tooltip" data-placement="top" title="" :data-original-title="pos.full">{{pos.abbrev +" "}}</span>;
  </div>
<div v-if="entry.stem">
<i>Stem:</i> {{entry.stem}}
</div>
</p>

<div v-if="entry.basic_audio.length>0" class="panel panel-oj">
  <div class="panel-heading" role="tab" id="audioBasicFormsHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#audioBasicForms" aria-expanded="true" aria-controls="audioBasicForms">
        <span class="caret"></span>
        Audio for Basic Forms
      </a>
    </h4>
  </div>
  <div id="audioBasicForms" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="audioBasicFormsHeader" aria-expanded="true">
    <div class="panel-body">
      <table class="table table-hover audio-table">
          <tbody>
                <tr v-for="audio_form in entry.basic_audio"><td><strong>{{audio_form.ojibwe}}</strong></td>
                  <td><em>
                  <span  v-for="pos in audio_form.poss" data-toggle="tooltip" data-placement="top" title="" :data-original-title="pos.ful">{{pos.abbrev +" "}}</span></em>
                <td class="text-right">
                  <div v-for="audio_rec in audio_form.audio_rec">
                    <a :href="audio_rec.speaker.href" class="speaker-initials" data-toggle="modal" data-target="#voiceModal" data-remote="false">
                      {{audio_rec.speaker.initials}}
                    </a>
                    <span class="badge badge-oj badge-audio-player">
                      <div id="audio-player-116840" class="audio-player" :data-file="audio_rec.audio.regular" :data-mobile-file="audio_rec.audio.mobile">
                        <span class="glyphicon glyphicon-volume-up glyphicon-audio-player"></span>
                        Listen
                      </div>
                    </span><br>
                  </div>
                </td>
                </tr>
      </tbody></table>
    </div>
  </div>
</div>


<div v-if="entry.additional_audio.length>0" class="panel panel-oj">
  <div class="panel-heading" role="tab" id="adtlAudioHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#adtlAudio" aria-expanded="true" aria-controls="adtlAudio">
        <span class="caret"></span>
        Audio for Basic Forms
      </a>
    </h4>
  </div>
  <div id="audioBasicForms" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="adtlAudio" aria-expanded="true">
    <div class="panel-body">
      <table class="table table-hover audio-table">
          <tbody>
                <tr v-for="audio_form in entry.additional_audio"><td><strong>{{audio_form.ojibwe}}</strong></td>
                  <td><em>
                  <span v-for="pos in audio_form.poss" data-toggle="tooltip" data-placement="top" title="" :data-original-title="pos.ful">{{pos.abbrev +" "}} </span></em>
                <td class="text-right">
                  <div v-for="audio_rec in audio_form.audio_rec">
                    <a :href="audio_rec.speaker.href" class="speaker-initials" data-toggle="modal" data-target="#voiceModal" data-remote="false">
                      {{audio_rec.speaker.initials}}
                    </a>
                    <span class="badge badge-oj badge-audio-player">
                      <div id="audio-player-116840" class="audio-player" :data-file="audio_rec.audio.regular" :data-mobile-file="audio_rec.audio.mobile">
                        <span class="glyphicon glyphicon-volume-up glyphicon-audio-player"></span>
                        Listen
                      </div>
                    </span><br>
                  </div>
                </td>
                </tr>
      </tbody></table>
    </div>
  </div>
</div>
  <p></p>
<div v-if="entry.sentence_examples.length>0" class="panel panel-oj">
  <div class="panel-heading" role="tab" id="sentenceExamplesHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#sentenceExamples" aria-expanded="true" aria-controls="sentenceExamples">
        <span class="caret"></span>
        Sentence Examples
      </a>
    </h4>
  </div>
  <div id="sentenceExamples" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="sentenceExamplesHeader" aria-expanded="true">
    <div class="panel-body">
      <table class="table table-hover audio-table">
            <tbody>
                <tr v-for="sentence in entry.sentence_examples"><td><strong><div class="stylized-text">{{sentence.ojibwe}}</div><br></strong><small><em>
                  <div class="stylized-text">{{sentence.english}}</div></em></small></td>
                  <td class="text-right">
                    <div v-for="audio_rec in sentence.audio_rec">
                          <a :href="audio_rec.speaker.href" class="speaker-initials" data-toggle="modal" data-target="#voiceModal" data-remote="false">
                  {{audio_rec.speaker.initials}}
                          </a>
                          <span class="badge badge-oj badge-audio-player">
                                <div id="audio-player-116840" class="audio-player" :data-file="audio_rec.audio.regular" :data-mobile-file="audio_rec.audio.mobile">
                                  <span class="glyphicon glyphicon-volume-up glyphicon-audio-player"></span>
                                  Listen
                                </div>
                              </span><br>
              </div>
                            </td>
                    </tr>
            </tbody>
      </table>
    </div>
  </div>
</div>

<div v-if="entry.word_parts" v-html="entry.word_parts">
</div>

<div v-if="entry.reduplication" class="panel panel-oj">
  <div class="panel-heading" role="tab" id="reduplicatedFormsHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#reduplicatedForms" aria-expanded="true" aria-controls="reduplicatedForms">
        <span class="caret"></span>
        Reduplication
      </a>
    </h4>
  </div>
  <div id="reduplicatedForms" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="reduplicatedFormsHeader" aria-expanded="true">
    <div class="panel-body">
      Reduplicated Form: <strong>{{entry.reduplication}}</strong>

    </div>
  </div>
</div>


<div class="panel panel-oj">
  <div class="panel-heading" role="tab" id="conjugatedFormsHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#conjugatedForms" aria-expanded="true" aria-controls="conjugatedForms">
        <span class="caret"></span>
        Conjugation
      </a>
    </h4>
  </div>
  <div id="conjugatedForms" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="conjugatedFormsHeader" aria-expanded="true">
    <div class="panel-body" v-html="entry.conjugation">
    </div>
  </div>
</div>
<div class="panel panel-oj" v-if="entry.imageresource_set.length>0 || entry.videoresource_set.length>0 || entry.documentresource_set.length>0">
  <div class="panel-heading" role="tab" id="relatedResourcesHeader">
    <h4 class="panel-title">
      <a class="" role="button" data-toggle="collapse" href="#relatedResources" aria-expanded="true" aria-controls="relatedResources">
        <span class="caret"></span>
        Related Resources
      </a>
    </h4>
  </div>
  <div id="relatedResources" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="relatedResourcesHeader" aria-expanded="true">
    <div class="panel-body">
      <ul class="media-list collection">
        <li v-for="resource in entry.imageresource_set" class="media"><div class="media-left">
          <a :href="resource.righthref.url"><img class="media-object collection-thumb" :src="resource.image.src" :alt="resource.image.alt"></a>
        </div>
        <div class="media-body">
          <h4 class="media-heading">
            <a :href="resource.righthref.url">{{resource.righttext}}</a>
          </h4>
        </div>
      </li>
        <li v-for="resource in entry.videoresource_set" class="media"><div class="media-left">
          <a :href="resource.righthref.url"><img class="media-object collection-thumb" :src="resource.image.src" :alt="resource.image.alt"></a>
        </div>
        <div class="media-body">
          <h4 class="media-heading">
            <a :href="resource.righthref.url">{{entry.righttext}}</a>
          </h4>
        </div>
      </li>
        <li v-for="resource in entry.documentresource_set" class="media"><div class="media-left">
          <a :href="resource.righthref.url"><span class="glyphicon glyphicon-duplicate document-icon"></span></a></div><div class="media-body"><h4 class="media-heading"><a :href="resource.righthref.url">{{resource.righttext}}</a></h4></div></li>
      </ul>
    </div>
  </div>
</div>
<router-link :to="`/vue/edit${entry.url}`" >{{"Edit " + entry.head_lemma}}</router-link>
</div>
</template>
<script>
import { EventBus } from './event-bus.js';
export default {
  props : ["entry"],
  mounted() {
    var self = this
    fetch(`/vue/json/main-entry/${self.entry}`)
      .then(response => response.json())
      .then(data => {
        self.entry = data
        if (self.entry.related_words){
          EventBus.$emit('relatedwords',
          {'related_words':self.entry.related_words,
           'entryurl': self.entry.url})
          }
        if (self.entry.word_family){
        EventBus.$emit('wordfamily',
        {'word_family':self.entry.word_family,
         'entryurl': self.entry.url})
        }
      })
  }
}
</script>
