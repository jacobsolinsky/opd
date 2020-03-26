#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:43:42 2020

@author: jacobsolinsky
todo: prevent keys from being added to slots
check that all morphemes are initialized with key and verb
"""



from .persons import (p1, p1p, p21, p2, p2p, p3, p3p, p3o, p3op,
                     p0, p0p, p0o, p0op, pX, TOPERSON, Person21)
from .morphemes import(Stem, Ni, Gi, O, M, I, Am, Aam, Aa, N2ndPerson, Go, Goo, Shi, Si,
                      Sin, Wnegative, Wdelayed, Wdubitative,
                      Mw, Min, Local_singular, Nsingular, Naan, Daa,
                      Naawaa, W3rdperson, W0thPerson, Aan, Ag, An, Ad, Aang, Angid,
                      Ang, Egw, Ng, Ind, Agogw, D, G, K2ndPerson,  Waaw, Waa,
                      Ni_animate, Ni_inanimate, Kdelayed, Ke,  Naam, Ban,
                      Dog, An_, Ag_, Ah_, Nimperative, Og, Gon, Aangen, En_dubitative,
                      NullMorpheme, to_double_vowel, Morpheme)
from . import morphemes
from collections import OrderedDict

from functools import partial



class SelectionFinished(Exception):
    pass

class FormDoesNotExist(Exception):
    pass


class OjibweVerb:
    MODES = ('neutral', 'preterite', 'dubitative', 'preterite-dubitative', 'prohibitative', 'delayed')
    ORDERS = ('independent', 'conjunct', 'changed-conjuct', 'imperative')
    def __init__(self, *, stem, details, subj, order, mode, polarity, dialect, variants):
        self.stem = Stem(self, stem)
        self.details = details
        self.subj = TOPERSON[subj]
        self.order, self.mode, self.polarity, self.dialect, self.variants = \
        order, mode, polarity, dialect, variants

    @property
    def neutral(self):
        return self.mode == 'neutral'

    @property
    def conjunct(self):
        #Note: preterite-dubitative independent verbs conjugate like conjunct verbs
        return self.order in ('conjunct', 'changed-conjunct') or \
        self.mode == 'preterite-dubitative' and self.order == 'independent'

    @property
    def changed_conjunct(self):
        return self.order == 'changed-conjunct'

    @property
    def preterite(self):
        return self.mode in ('preterite', 'preterite-dubitative')

    @property
    def dubitative(self):
        return self.mode in ('dubitative', 'preterite-dubitative')

    @property
    def independent(self):
        return self.order == 'independent' and not self.mode == 'preterite-dubitative'

    @property
    def imperative(self):
        return self.order == 'imperative'

    @property
    def delayed(self):
        return self.mode == 'delayed'

    @property
    def prohibitative(self):
        return self.mode == 'prohibitative'

    def select_negative(self):
        if not self.polarity:
            self.slots['negative'] = Si(self)
            self.slots['negative_w'] = Wnegative(self)

    def select_mode(self):
        if self.preterite:
            self.slots['mode'] = Ban(self)
        if self.dubitative:
            if self.conjunct:
                self.slots['en'] = En_dubitative(self)
            elif self.independent:
                self.slots['mode'] = Dog(self)
            if self.conjunct:
                self.slots['dubitative_w'] = Wdubitative(self)
        elif self.prohibitative:
            if self.subj == p21:
                self.slots['negative'] = Si(self)
                self.slots['negative_w'] = Wnegative(self)
            else:
                self.slots['mode'] = Ke(self)
        elif self.delayed:
            self.slots['w_delayed'] = Wdelayed(self)
            self.slots['mode'] = Kdelayed(self)



    def check_validity(self):
        assert self.order in self.ORDERS, 'not a valid order'
        assert self.mode in self.MODES, 'not a valid mode'
        if self.order in ('independent', 'conjunct', 'changed-conjunct'):
            assert self.mode not in ('prohibitative', 'delayed'),\
                'prohibitative and delayed modes go only with imperative order'
        elif self.order == 'imperative':
            assert self.mode not in ('preterite', 'dubitative', 'preterite-dubitative'),\
                'preterite, dubitative, and preterite-dubitative  modes go only with independent, conjunct, and changed conjunct orders'

    @staticmethod
    def conjugate(cls, verb):
        try:
            verb.slots['stem'] = verb.stem
            cls.select_personal_prefix(verb)
            cls.select_theme_sign(verb)
            cls.select_negative(verb)
            cls.select_major(verb)
            cls.select_mode(verb)
            cls.select_minor(verb)
        except SelectionFinished: pass
    
    def select_personal_prefix(self): 
        pass
    def select_theme_sign(self):
        pass




class TransitiveVerb(OjibweVerb):
    def __init__(self, *, obj, focus = None, **kwargs ):
        super().__init__(**kwargs)
        self.obj = TOPERSON[obj]
        if focus == "goal":
            self.focus = self.obj
        elif focus == "actor":
            self.focus = self.subj
        else:
            self.focus == TOPERSON[focus]
        self.primary = self.subj if PRIMACY(self.subj) > PRIMACY(self.obj) else self.obj

class VTA(TransitiveVerb):
    type = "vta"

    def check_validity(self):
        super().check_validity()
        assert (self.subj.animacy or self.obj.animacy), "Subject and Object cannot both be inanimate"
        assert self.subj != self.obj, "Use Reflexive VAI for this VTA stem"
        if self.subj == p21:
            assert not self.obj in [p1, p1p, p2, p2p], \
           """Inclusive Giinawind can't act on itself or
           be acted upon by itself.
           """
        if self.obj == p21:
            assert not self.subj in [p1, p1p, p2, p2p], \
            """Inclusive Giinawind can't act on itself or
           be acted upon by itself.
           """
    def conjugate(self):
        if self.order == 'independent' and self.preterite and self.dubitative:
            raise FormDoesNotExist
        if self.independent:
            self.slots = vta_independent_slots()
        elif self.conjunct:
            self.slots = vta_conjunct_slots()
        elif self.imperative:
            self.slots = vta_imperative_slots()
        v = Morpheme(self)
        OjibweVerb.conjugate(VTA, self)
        for morpheme in self.slots.values():
            if morpheme:
                morpheme.mutate()
        v.form = ''.join([morpheme.form for morpheme in self.slots.values() if morpheme])
        if self.changed_conjunct:
            v.initial_vowel_change()
        v.apocope()
        v.final_w_loss()
        if to_double_vowel(v.form) == 'gidinigoosiiiin':
            for morpheme in self.slots.values():
                print(morpheme)
                print(type(morpheme))
            print(self.variants)
        return to_double_vowel(v.form)

    def select_personal_prefix(self):
        if self.independent:
            if self.subj.person == 2 or self.obj.person == 2:
                self.slots['personal_prefix'] = Gi(self)
            elif self.subj.person == 1 or self.obj.person == 1:
                self.slots['personal_prefix'] = Ni(self)
            elif self.subj.person == 3:
                self.slots['personal_prefix'] = O(self)

    def select_theme_sign(self):
        #Conjugate like a VTI with theme sign Go
        if self.subj.person == 0:
            self.slots['theme_sign'] = Go(self)
            self.subj, self.obj = self.obj, self.subj
            OjibweVerb.conjugate(VTI, self)
            raise SelectionFinished
        
        #Conjugate like a VAI with theme sign Goo
        elif self.subj == p1p and self.obj.person == 2 and not self.imperative or \
        self.subj == pX and self.obj.person != 3:
            self.slots['theme_sign'] = Goo(self)
            self.subj, self.obj = self.obj, self.subj
            OjibweVerb.conjugate(VAI, self)
            raise SelectionFinished
        
        if self.obj.obviacy and self.subj.locality:
            self.slots['m_obviative'] = M(self)
        if self.independent:
            if self.obj.person == 3 and not self.subj.obviacy:
                self.slots['theme_sign'] = Aa(self, 'theme_sign')
            elif self.obj.person == 3 and self.subj.obviacy:
                self.slots['theme_sign'] = Go(self)
            elif self.subj.person == 3 and self.obj.locality:
                self.slots['theme_sign'] = Go(self)
            elif self.subj.person == 2 and self.obj.person == 1:
                self.slots['theme_sign'] = I(self)
            elif self.subj.person == 1 and self.obj.person == 2:
                self.slots['theme_sign'] = N2ndPerson(self, 'theme_sign')
                if not self.polarity:
                    self.slots['echo'] = N2ndPerson(self, 'echo')
                    self.slots['2nd_echo'] = N2ndPerson(self, '2nd_echo')
        
        elif self.conjunct:
            if self.subj.locality and not self.obj.locality:
                self.slots['theme_sign'] = Aa(self, 'theme_sign')
            elif self.obj.locality:
                if self.obj.person == 1:
                    self.slots['theme_sign'] = I(self)
                elif self.obj.person in (2, Person21):
                    self.slots['theme_sign'] = N2ndPerson(self, 'theme_sign')
                    if not self.polarity:
                        self.slots['echo'] = N2ndPerson(self, 'echo')
                        if self.obj == p2 and self.subj == p1:
                            if self.variants['sinoonaan/sinowaan'] == 'sinoonaan':
                                self.slots['2nd_echo'] = N2ndPerson(self, '2nd_echo')
                                morphemes.current_variants.append({**morphemes.default_variants, 'sinoonaan/sinowaan': 'sinowaan'})
                            else:
                                pass
            elif self.obj.obviacy and self.subj.person == 3:
                self.slots['theme_sign'] = Aa(self, 'theme_sign')
            elif self.subj.obviacy and self.obj.person == 3:
                self.slots['theme_sign'] = Go(self)
        
        elif self.imperative:
            if self.obj.person == 3 and not (self.mode == 'neutral' and self.subj in (p2, p2p)):
                self.slots['theme_sign'] = Aa(self, 'theme_sign')
            elif self.subj == p2 and self.obj.person == 3 and self.mode == 'neutral':
                self.slots['theme_sign'] = I(self)
            elif self.obj.person == 1:
                self.slots['theme_sign'] = Shi(self) 

    def select_major(self):
        theme_sign = self.slots['theme_sign']
        if self.independent:
            if type(theme_sign) in (Aa, Go):
                self.slots['major'] = INDEPENDENT_CENTRAL_VTA(self.primary)(self)
                if type(theme_sign) == Aa and type(self.slots['major']) in (Naan, Waaw) and not self.polarity:
                    self.slots['2nd_echo'] = Aa(self, '2nd_echo')
            elif type(theme_sign) in (I, N2ndPerson):
                self.slots['major'] = INDEPENDENT_CENTRAL_VAI(self.primary)(self)
        elif self.conjunct:
            if self.obj == p1 and self.subj.person == 3:
                self.slots['major'] = D(self)
            elif self.obj == p2 and self.subj.person == 3:
                self.slots['major'] = K2ndPerson(self)
            elif type(theme_sign) == Aa:
                if self.primary.locality:
                    self.slots['major'] = CONJUNCT_CENTRAL_THEME_AA(self.primary)(self)
                    if self.polarity and not self.dubitative:
                        self.slots['theme_sign'] = NullMorpheme()
                    elif not self.polarity and self.dubitative and self.variants['dubitative-aa-echo']:
                        morphemes.current_variants.append({**morphemes.default_variants, 'dubitative-aa-echo': False})
                        self.slots['echo'] = Aa(self, 'echo')
                else:
                    self.slots['major'] = D(self)
            elif type(theme_sign) == N2ndPerson:
                if self.subj.person == 1:
                    self.slots['major'] = CONJUNCT_CENTRAL_THEME_N(self.primary)(self)
                else:
                    self.slots['major'] = CONJUNCT_CENTRAL_THEME_AA(self.primary)(self)
            elif type(theme_sign) == I:
                if self.subj.person == 2:
                    self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.primary)(self)
                else:
                    self.slots['major'] = CONJUNCT_CENTRAL_THEME_AA(self.primary)(self)
            else:
                self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.primary)(self)
            if p3p in (self.minor, self.major) and not (self.changed_conjunct and self.focus==p3p):
                if type(self.slots['major']) == D and (self.polarity or self.dubitative):
                    self.slots['special'] = Waa(self)
                else:
                    self.slots['waaw'] = Waaw(self, 'waaw')
        elif self.imperative:
            if self.mode == 'delayed':
                self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.primary)(self)
            else:
                if self.primary == p2:
                    if self.mode != 'neutral' or self.obj == p1:
                        self.slots['major'] = Nimperative(self)
                elif self.primary == p2p:
                    if self.mode == 'neutral':
                        self.slots['major'] = Og(self)
                    elif self.mode == 'prohibitative':
                        self.slots['major'] = Gon(self)
                elif self.primary == p1p:
                    if self.mode == 'neutral':
                        self.slots['major'] = Naam(self)
                    elif self.mode == 'prohibitative':
                        self.slots['major'] = Aangen(self)
                elif self.primary == p21:
                    self.slots['major'] = Daa(self)
                

    def select_minor(self):
        if self.changed_conjunct:
            self.slots['minor'] = {
                    p3p: Ag_,
                    p3o: An_,
                    p3op: Ah_,
                    p0p: An_,
                    }.get(self.focus, NullMorpheme)(self)
        #define property minor
        elif self.independent or self.imperative:
            self.slots['minor'] = {
                    p3p: Ag_,
                    p3o: An_,
                    p3op: Ah_,
                    }.get(self.minor, NullMorpheme)(self)



    @property
    def major(self):
        return self.subj if PRIMACY(self.subj)  >= PRIMACY(self.obj) else self.obj

    @property
    def minor(self):
        return self.subj if PRIMACY(self.subj)  < PRIMACY(self.obj) else self.obj

class VTI(TransitiveVerb):
    type = "vti"
    def check_validity(self):
        super().check_validity()
        assert self.subj.animacy, "Subjects of VTI must be animate"
        assert self.obj in [p0, p0p, p0o, p0op], "Objects of VTI must be inanimate"

    def conjugate(self):
        if self.order == 'independent' and self.preterite and self.dubitative and self.subj.person != 3:
            raise FormDoesNotExist
        if self.independent:
            self.slots = vai_independent_slots()
        elif self.conjunct:
            self.slots = vai_conjunct_slots()
        elif self.imperative:
            self.slots = vti_imperative_slots()
        v = Morpheme(self)
        OjibweVerb.conjugate(VTI, self)
        for morpheme in self.slots.values():
            if morpheme:
                morpheme.mutate()
        v.form = ''.join([morpheme.form for morpheme in self.slots.values() if morpheme])
        if self.changed_conjunct:
            v.initial_vowel_change()
        v.apocope()
        v.final_w_loss()
        return to_double_vowel(v.form)

    def select_personal_prefix(self):
        if self.independent:
            self.slots['personal_prefix'] = {
                    1: Ni,
                    Person21: Gi,
                    2: Gi,
                    3: O,
                    }.get(self.subj.person, NullMorpheme)(self)

    def select_theme_sign(self):
        if 'am' in self.details:
            self.slots['theme_sign'] = Am(self)
        elif 'aam' in self.details:
            self.slots['theme_sign'] = Aam(self)
        elif 'oo' in self.details:
            self.slots['stem'].form += 'O'

    def select_major(self):
        if self.independent:
            self.slots['major'] = INDEPENDENT_CENTRAL_VTI(self.subj)(self)
        elif self.conjunct:
            VAI.select_major(self)
        elif self.imperative:
            if self.mode == "neutral":
                self.slots['major'] = {
                        p2: Nimperative,
                        p2p: Og,
                        p21: Daa
                        }[self.subj](self)
            elif self.mode == "delayed":
                if self.subj in (p2, p2p):
                    self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.subj)(self)
                else:
                    self.slots['major'] = Daa(self)
            elif self.mode == "prohibitative":
                self.slots['major'] = {
                        p2: Nimperative,
                        p2p: Gon,
                        p21: Aangen
                        }[self.subj](self)

    def select_minor(self):
        if self.independent:
            self.slots['minor'] = {
                    p0p: An_,
                    p3o: An_,
                    p3p: Ag_,
                    p3op: Ah_,
                    }.get(self.obj, NullMorpheme)(self)
        elif self.changed_conjunct:
            self.slots['minor'] = {
                    p0p: An_,
                    p3o: An_,
                    p3p: Ag_,
                    p3op: Ah_,
                    }.get(self.focus, NullMorpheme)(self)
        raise SelectionFinished


class IntransitiveVerb(OjibweVerb):
    @property
    def focus(self):
        return self.subj


class VAI(IntransitiveVerb):
    type = "vai"
    def conjugate(self):
        if self.order == 'independent' and self.preterite and self.dubitative and self.subj.person != 3:
            raise FormDoesNotExist
        if self.independent:
            self.slots = vai_independent_slots()
        elif self.conjunct:
            self.slots = vai_conjunct_slots()
        elif self.imperative:
            self.slots = vai_imperative_slots()
        v = Morpheme(self)
        OjibweVerb.conjugate(VAI, self)
        for morpheme in self.slots.values():
            if morpheme:
                morpheme.mutate()
        v.form = ''.join([morpheme.form for morpheme in self.slots.values() if morpheme])
        if self.changed_conjunct:
            v.initial_vowel_change()
        v.apocope()
        v.final_w_loss()
        return to_double_vowel(v.form)

    def select_theme_sign(self):
        if 'am' in self.details:
            self.slots['theme_sign'] = Am(self)

    def select_personal_prefix(self):
        if self.independent:
            self.slots['personal_prefix'] = {
                    1: Ni,
                    Person21: Gi,
                    2: Gi,
                    }.get(self.subj.person, NullMorpheme)(self)

    def select_major(self):
        if self.independent:
            self.slots['major'] = INDEPENDENT_CENTRAL_VAI(self.subj)(self)
        elif self.conjunct:
            self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.subj)(self)
            if self.subj.obviacy:
                self.slots['special'] = Ni_animate(self)
            elif self.subj == p3p and not (self.changed_conjunct and self.focus == p3p):
                if not self.polarity and not self.dubitative:
                    self.slots['waaw'] = Waaw(self, 'waaw')
                else:
                    self.slots['special'] = Waa(self)
        elif self.imperative:
            if self.mode == "neutral":
                self.slots['major'] = {
                        p2: Nimperative,
                        p2p: Og,
                        p21: Daa
                        }[self.subj](self)
            elif self.mode == "delayed":
                if self.subj in (p2, p2p):
                    self.slots['major'] = CONJUNCT_CENTRAL_PRIMARY(self.subj)(self)
                else:
                    self.slots['major'] = Daa(self)
            elif self.mode == "prohibitative":
                self.slots['major'] = {
                        p2: Nimperative,
                        p2p: Gon,
                        p21: Aangen
                        }[self.subj](self)
        


    def select_minor(self):
        if self.independent or self.changed_conjunct:
            self.slots['minor'] ={
                    p3o: An_,
                    p3p: Ag_,
                    p3op: Ah_,
                    }.get(self.subj, NullMorpheme)(self)
        raise SelectionFinished


class VAIO(VTI):
    type = "vaio"
    def check_validity(self):
        super().check_validity()
        assert self.obj in [p0, p0p, p0o, p0op, p3, p3o, p3p, p3op]


class VII(IntransitiveVerb):
    type = "vai"
    def conjugate(self):
        if self.independent:
            self.slots = vii_independent_slots()
        elif self.conjunct:
            self.slots = vii_conjunct_slots()
        v = Morpheme(self)
        OjibweVerb.conjugate(VII, self)
        for morpheme in self.slots.values():
            if morpheme:
                morpheme.mutate()
        v.form = ''.join([morpheme.form for morpheme in self.slots.values() if morpheme])
        if self.changed_conjunct:
            v.initial_vowel_change()
        v.final_w_loss()
        return to_double_vowel(v.form)

    def select_negative(self):
        if not self.polarity:
            self.slots['negative'] = Sin(self)
    
    def select_major(self):
        if self.independent:
            self.slots['major'] = W0thPerson(self)
        elif self.conjunct:
            self.slots['major'] = G(self)
        if self.subj.obviacy:
            self.slots['special'] = Ni_inanimate(self)
            
    def select_mode(self):
        if self.preterite:
            self.slots['mode'] = Ban(self)
        if self.dubitative:
            if self.conjunct:
                self.slots['en'] = En_dubitative(self)
            elif self.independent:
                self.slots['mode'] = Dog(self)
    
    def select_minor(self):
        if not self.order == 'conjunct':
            if self.subj.plurality:
                self.slots['minor'] = An_(self)

        

def vta_independent_slots():
    return OrderedDict({
    'personal_prefix': NullMorpheme(),
    'stem': NullMorpheme(),
    'm_obviative': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'echo': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'special': NullMorpheme(),
    '2nd_echo': NullMorpheme(),
    'major': NullMorpheme(),
    'mode': NullMorpheme(),
    'minor': NullMorpheme(),
    })

def vta_conjunct_slots():
    return OrderedDict({
    'personal_prefix': NullMorpheme(),
    'stem': NullMorpheme(),
    'm_obviative': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'dubitative_w': NullMorpheme(),
    'echo': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'special': NullMorpheme(),
    '2nd_echo': NullMorpheme(),
    'major': NullMorpheme(),
    'waaw': NullMorpheme(),
    'mode': NullMorpheme(),
    'en': NullMorpheme(),
    'minor': NullMorpheme(),
    })
def vta_imperative_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'm_obviative': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'echo': NullMorpheme(),
    'w_delayed': NullMorpheme(),
    'mode': NullMorpheme(),
    'major': NullMorpheme(),
    'minor': NullMorpheme(),
    })


def vai_conjunct_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'dubitative_w': NullMorpheme(),
    'special': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'major': NullMorpheme(),
    'waaw': NullMorpheme(),
    'mode': NullMorpheme(),
    'en': NullMorpheme(),
    'minor': NullMorpheme(),})


def vai_independent_slots():
    return OrderedDict({
    'personal_prefix': NullMorpheme(),
    'stem': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'major': NullMorpheme(),
    'mode': NullMorpheme(),
    'minor': NullMorpheme(),})

def vai_imperative_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'echo': NullMorpheme(),
    'w_delayed': NullMorpheme(),
    'mode': NullMorpheme(),
    'major': NullMorpheme(),
    })

def vti_imperative_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'theme_sign': NullMorpheme(),
    'negative': NullMorpheme(),
    'negative_w': NullMorpheme(),
    'echo': NullMorpheme(),
    'w_delayed': NullMorpheme(),
    'mode': NullMorpheme(),
    'major': NullMorpheme(),
    'minor': NullMorpheme(),
    })

def vii_independent_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'negative': NullMorpheme(),
    'special': NullMorpheme(),
    'major': NullMorpheme(),
    'mode': NullMorpheme(),
    'minor': NullMorpheme(),})

def vii_conjunct_slots():
    return OrderedDict({
    'stem': NullMorpheme(),
    'negative': NullMorpheme(),
    'special': NullMorpheme(),
    'major': NullMorpheme(),
    'mode': NullMorpheme(),
    'en': NullMorpheme(),
    'minor': NullMorpheme(),})


def INDEPENDENT_CENTRAL_VAI(person):
        if person.locality:
            if person.name in ['p1','p2']:
                return Local_singular
            if person.person == 1:
                return Min
            else:
                return Mw
        elif person.person in [3,0]:
            return W3rdperson
        elif person.person == 'X':
            return Mw

def INDEPENDENT_CENTRAL_VTI(person):
        if person.person == 'X':
            return Mw
        if not person.plurality:
            return Nsingular
        elif person.person == 1:
            return Min
        elif person.plurality:
            return Naawaa
        else:
            return NullMorpheme

def INDEPENDENT_CENTRAL_VTA(person):
    return {'p1p': Naan,
            'p21': Naan,
            'p2p': partial(Waaw, slot='major'),
            'p3p': partial(Waaw, slot='major'),}.get(person.name, NullMorpheme)


def INDEPENDENT_CENTRAL_THEME_I(primary):
    if primary == p1p:
        return Min
    elif primary == p2p:
        return Mw
    else:
        return Local_singular


def CONJUNCT_CENTRAL_PRIMARY(person):
    person = person.name
    conjunctcentrali = {
         'p1':Aan,
         'p2':An,
         'p1p':Aang,
         'p21':Ang,
         'p2p':Egw,
         'pX':Ng,
         'p3':D,
         'p3p':D,
         'p3o':D,
         'p3op':D
            }
    return conjunctcentrali[person]


def CONJUNCT_CENTRAL_THEME_AA(person):
    return {'p1':Ag,
         'p2':Ad,
         'p1p':Angid,
         'p21':Ang,
         'p2p':Egw,
         'pX':Ind}[person.name]

def CONJUNCT_CENTRAL_THEME_N(primary):
    if primary == p2:
        return Aan
    elif primary == p2p:
        return Agogw
    else:
        return NullMorpheme

def PRIMACY(person):
    person = person.name
    primacy = {'p0o':0,
         'p0op':0,
         'p0':1,
         'p0p':1,
         'p3o':2,
         'p3op':2,
         'p3':3,
         'p3p':3,
         'pX':4,
         'p1':5,
         'p1p':7,
         'p2':6,
         'p21':6,
         'p2p':6}
    return primacy[person]

#test
#vv = VAI(stem='bakade', details=[], subj='1', order='independent', mode='neutral', polarity=True, dialect=[], variants = default_variants)
