import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
/* eslint-disable no-param-reassign */
export default new Vuex.Store({
state: {
  gottenAllPartsOfSpeech:false,
  gottenAllPos: false,
  gottenAllSpeakers: false,
  gottenAllEntries:false,
  gottenAllImageresource_set: false,
  gottenAllVideoresource_set: false,
  gottenAllDocumentresource_set: false,
  gottenAllRelatedwords: false,
  behindLogin : '/'
},
mutations: {
  addAllPartsOfSpeech(state){
    state._allPartsOfSpeech = fetch("/api/littlepartsofspeech/")
    .then(response => response.json())
    state.gottenAllPartsOfSpeech = true
  },
  addAllPos(state){
    state._allPos = fetch("/api/poss/")
    .then(response => response.json())
    state.gottenAllPos = true
  },
  addAllSpeakers(state){
    state._allSpeakers = fetch("/api/speakers/")
    .then(response => response.json())
    state.gottenAllSpeakers = true
  },
  addAllEntries(state){
    state._allEntries = fetch("/api/tinylinks/")
    .then(response => response.json())
    state.gottenAllEntries = true
  },
  addAllImageresource_set(state){
    state._allImageresource_set = fetch("/api/imageresources/")
    .then(response => response.json())
    state.gottenAllImageresource_set = true
  },
  addAllVideoresource_set(state){
    state._allVideoresource_set = fetch("/api/videoresources/")
    .then(response => response.json())
    state.gottenAllVideoresource_set = true
  },
  addAllDocumentresource_set(state){
    state._allDocumentresource_set = fetch("/api/documentresources/")
    .then(response => response.json())
    state.gottenAllDocumentresource_set = true
  },
  addAllRelatedwords(state){
    state._allRelatedwords = fetch("/api/related-words/")
    .then(response => response.json())
    state.gottenAllRelatedwords = true
  },
  login(state){
    state.loggedIn = true
  },
  setBehindLogin(state, value){
    state.behindLogin = value
  }
},
actions: {
  allPartsOfSpeech(context){
    if (! context.state.gottenAllPartsOfSpeech){
          context.commit('addAllPartsOfSpeech')
        }
    },
  allPos(context){
    if (! context.state.gottenAllPos){
          context.commit('addAllPos')
        }
    },
  allSpeakers(context){
      if (! context.state.gottenAllSpeakers){
            context.commit('addAllSpeakers')
          }
    },
  allEntries(context){
    if (! context.state.gottenAllEntries){
          context.commit('addAllEntries')
        }
      },
  allImageresource_set(context){
      if (! context.state.gottenAllImageresource_set){
            context.commit('addAllImageresource_set')
        }
      },
  allVideoresource_set(context){
      if (! context.state.gottenAllVideoresource_set){
            context.commit('addAllVideoresource_set')
        }
      },
  allDocumentresource_set(context){
    if (! context.state.gottenAllDocumentresource_set){
            context.commit('addAllDocumentresource_set')
        }
      },
  allRelatedwords(context){
      if (! context.state.gottenAllRelatedwords){
            context.commit('addAllRelatedwords')
        }
      }
  }
}
)
