export default {
  namespaced: true,
  state: {
    animateActors: ['1', '2', '3', "3'", '3p', '1p', '21', '2p', 'X'],
    singularActors: ['1', '2', '3', "3'", 'X', '0', "0'"],
    pluralActors: ['1p', '21', '2p', '3p', "3'", "3'p", 'X', '0p', "0'p"],
    firstPersonActors: ['1', '1p'],
    secondPersonActors: ['2', '2p'],
    imperativeActors: ['2', '2p', '21'],
    thirdPersonActors: ['3', '3p'],
    fourthPersoActors: ["3'"],
    localActors: ['1', '1p', '21', '2', '2p', 'X'],
    nonlocalActors: ['3', "3'", '3p'],
    nonlocalActors: ['0', '0p'],
    nonlocalExtendedActors: ['0', '0p', "0'", "0'p"],
    actorOjibweNames: {'1': 'Niin', '2': 'Giin', '3': 'Wiin', "3'": "Odaya'aaman", "3'p": "Odaya'aama'", '3p': 'Wiinawaa',
      '1p': 'Niinawind', '21': 'Giinawind', '2p': 'Giinawaa', X: "Aya'aag", '0': "I'iw", '0p': "Iniw", "0'": "Odaya'iim", "0'p": "Odaya'iiman",},
    actorEnglishNames: {'1': 'I', '2': 'You (singular)', '3': 'S/he', "3'": "4th person", "3'p": "4th persons", '3p': 'They',
      '1p': 'We (and not you)', '21': 'We (including you)', '2p': 'You all', X: '"They" (nonspecific)', '0': "It", '0p': "They", "0'": "4th thing", "0'p": "4th things"},
  }
}
