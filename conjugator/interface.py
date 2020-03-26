#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:12:21 2020

@author: jacobsolinsky
"""
import re
from .verb import VAI, VII, VTI, VTA, FormDoesNotExist
from . import morphemes




import pandas as pd
vai_index_1 = pd.MultiIndex.from_product(
        [['independent', 'conjunct', 'changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '2', '3', "3'", '3p', '1p', '21', '2p', 'X']],
         names = ['order', 'mode', 'polarity', 'subj',])

vai_index_2 = pd.MultiIndex.from_product(
        [['imperative'], ['neutral', 'prohibitative', 'delayed'], [True],
         ['2', '21', '2p']],
         names = ['order', 'mode', 'polarity', 'subj',])

vai_index = vai_index_1.union(vai_index_2)

vta_index_1 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '2', '1p', '21', '2p'], ['3', '3p', "3'"], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_2 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '2', '1p', '21', '2p'], ['3', '3p', "3'"], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_3 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['3', '3p', "3'"], ['1', '2', '1p', '21', '2p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_4 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['3', '3p', "3'"], ['1', '2', '1p', '21', '2p'], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_5 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '1p'], ['2', '2p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_6 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '1p'], ['2', '2p'], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_7 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['2', '2p'], ['1', '1p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_8 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['2', '2p'], ['1', '1p'], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_9 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['0', '0p'], ['1', '1p', '21', '2', '2p', '3', "3'", '3p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_10 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['0', '0p'], ['1', '1p', '21', '2', '2p', '3', "3'", '3p'], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_11 = pd.MultiIndex.from_product(
        [['independent', 'conjunct',], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['X'], ['1', '1p', '21', '2', '2p', '3', "3'", '3p'], ['goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_12 = pd.MultiIndex.from_product(
        [['changed-conjunct',], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['X'], ['1', '1p', '21', '2', '2p', '3', "3'", '3p'], ['goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_13 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['3', '3p'], ["3'"], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_14 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['3', '3p'], ["3'"], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_15 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ["3'"], ['3', '3p'], ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_16 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ["3'"], ['3', '3p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_17 = pd.MultiIndex.from_product(
        [['imperative'], ['neutral', 'prohibitative', 'delayed'], [True],
         ['2', '2p', ], ['3', '3p', "3'", '1', '1p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index_18 = pd.MultiIndex.from_product(
        [['imperative'], ['neutral', 'prohibitative', 'delayed'], [True],
         ['21', ], ['3', '3p', "3'"], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vta_index = vta_index_1.union(
            vta_index_2.union(
            vta_index_3.union(
            vta_index_4.union(
            vta_index_5.union(
            vta_index_6.union(
            vta_index_7.union(
            vta_index_8.union(
            vta_index_9.union(
            vta_index_10.union(
            vta_index_11.union(
            vta_index_12.union(
            vta_index_13.union(
            vta_index_14.union(
            vta_index_15.union(
            vta_index_16.union(
            vta_index_17.union(
            vta_index_18
)))))))))))))))))




vti_index_1 = pd.MultiIndex.from_product(
        [['independent', 'conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
          ['1', '1p', '21', '2', '2p', '3', "3'", '3p', 'X'], ['0', '0p'], ['actor']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vti_index_2 = pd.MultiIndex.from_product(
        [['changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['1', '1p', '21', '2', '2p', '3', "3'", '3p', 'X'], ['0', '0p'],  ['actor', 'goal']],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vti_index_3 = pd.MultiIndex.from_product(
        [['imperative'], ['neutral', 'prohibitative', 'delayed'], [True],
         ['2', '21', '2p'], ['0', '0p'], ['actor'],],
         names = ['order', 'mode', 'polarity', 'subj', 'obj', 'focus'])

vti_index = vti_index_1.union(
            vti_index_2.union(
            vti_index_3
))

vii_index = pd.MultiIndex.from_product(
        [['independent', 'conjunct', 'changed-conjunct'], ['neutral', 'preterite', 'dubitative', 'preterite-dubitative'], [True, False],
         ['0', '0p', "0'", "0'p"]],
         names = ['order', 'mode', 'polarity', 'subj',])



def nested_dict(df):
    retval = {}
    if type(df.index) == pd.MultiIndex:
        outerlevels = df.index.levels[0]
        for outerlevel in outerlevels:
            if len(df.index.names) > 1:
                try:
                    retval[outerlevel] = nested_dict(df.loc[outerlevel])
                except KeyError:
                    pass
    else:
        for outerlevel in df.index:
            try:
                retval[outerlevel] = df.loc[outerlevel]['form']
            except KeyError:
                pass
    return retval

def conj_call(entry):
    stem = re.search(r'[^+]+', entry.stem[1:-2]).group(0)
    pos = entry.part_of_speech.abbrev
    index, conjugator, type_, details = {
            'vai': (vai_index, VAI, 'vai', []),
            'vai2': (vai_index, VAI, 'vai', ['am']),
            'vti': (vti_index, VTI, 'vti', ['am']),
            'vti2': (vti_index, VTI, 'vti', ['oo']),
            'vti3': (vti_index, VTI, 'vti', []),
            'vti4': (vti_index, VTI, 'vti', ['aam']),
            'vta': (vta_index, VTA, 'vta', []),
            'vii': (vii_index, VII, 'vii', []),
        }[pos]
    data = pd.DataFrame(index=index, columns={'form':[]})
    for idx in index:
        form_list = []
        morphemes.current_variants.append(morphemes.default_variants)
        try:
            while morphemes.current_variants:
                form_list.append(
                    conjugator(
                        stem=stem, **dict(zip(index.names, idx)), variants=morphemes.current_variants.pop(), dialect=[], details = details
                    ).conjugate()
                )
            data.loc[idx] = ', '.join(form_list)
        except FormDoesNotExist:
            data.loc[idx] = '-'
    retval =  nested_dict(data)
    retval['type'] = type_
    return retval
