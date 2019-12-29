<template>
  <div class="modal fade in" id="voiceModal" tabindex="-1" role="dialog" aria-labelledby="voiceModalLabel" style="display: block;">
  <div class="modal-dialog" role="document">
    <div class="modal-content"><div class="modal-header">
  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
  <h4 class="modal-title" id="myModalLabel">Ojibwe Voice</h4>
</div>
<div class="modal-body voice">
<div class="voice row full-row">
  <div class="col-lg-12">
    <h2>
      {{speaker.primary_name}}
      <div class="speaker-initials">
        {{speaker.initials}}
      </div>
    </h2>
    <img class="voice-image" src="/uploads/people/images/person/94224/320-OPD_6-2011.png" alt="320 opd 6 2011">
    <div>
      <div class="voice-info-field">
        <span class="voice-tag">Ojibwe Name:</span>
        <span class="voice-field">{{speaker.ojibwe_name}}</span>
      </div>
      <div class="voice-info-field">
        <span class="voice-tag">English Name:</span>
        <span class="voice-field">{{speaker.english_name}}</span>
      </div>
      <div class="voice-info-field">
        <span class="voice-tag">Community:</span>
        <span class="voice-field">{{speaker.community}}</span>
      </div>
      <div class="voice-info-field">
        <span class="voice-tag">Region:</span>
        <span class="voice-field">{{speaker.region}}</span>
      </div>
      <div v-html="speaker.description">
      </div>
    </div>
  </div>
</div>

</div>
<div class="modal-footer">
  <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
</div>

</div>
  </div>
</div>
</template>
