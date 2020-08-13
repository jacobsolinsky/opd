import re
import numpy as np
from weighted_levenshtein import lev
from functools import partial


default_variants = {
        'banii/bane': 'bane',
        'siin/sii': 'siin',
        'dubitative-aa-echo': True,
        'widog': True,
        'sinoonaan/sinowaan': 'sinoonaan',
        'shinaang?': 'shinaang'
        }
variants_available = {
        'banii/bane': ['bane', 'banii'],
        'siin/sii': ['siin', 'sii'],
        'dubitative-aa-echo': [True, False],
        'widog': [True, False],
        'sinoonaan/sinowaan': ['sinoonaan', 'sinowaan'],
        'shinaang?': ['shinaang', 'shinaan', 'shinaam']
        }
current_variants = []

'''
Internal orthography correspondence
to double vowel orthography
VOWELS
a = a
A = aa
e = ε (nonpalatalizing short i)
E = e
i = i
I = ii
o = o
O = oo

v = any short vowel
V = any long vowel

CONSONANTS
m = m
b = b
p = p
w = w
n = n
d = d
t = t
N = algonquian θ (alternates between n and zh)
s = s
z = z
j = j
c = ch
Z = zh
S = sh
y = y
g = g
k = k
h = glottal stop
C = any consonant
F = any fortis consonant
L = any lenis consonant
Q = any nasal consonant
Y = any palatalizable consonant
'''
#Converting to internal orthography
C = "hbpwmdtnszSZcjykghN"
v = 'aieo'
V= 'AIEO'
F = 'ptsSck'
L = 'bdzZjg'
Q = 'nm'
Y = 'Ndtsz'
internal_alphabet = "aAbcdEghiIjkmnoOpsStwyzZ"
insert_costs = np.full((128,), 1000, dtype=np.float64)
for i in range(128):
    if chr(i) in internal_alphabet: insert_costs[i] = 5
delete_costs = np.full((128,), 5, dtype=np.float64)
substitution_costs = np.full((128, 128), 1000, dtype=np.float64)
for i in internal_alphabet:
    i = ord(i)
    for j in internal_alphabet:
        j = ord(j)
        substitution_costs[i][j] = 9
        substitution_costs[j][i] = 9

for i in 'aioAIEO':
    i = ord(i)
    for j in 'aioAIEO':
        j = ord(j)
        substitution_costs[i][j] = 3
        substitution_costs[j][i] = 3

for i in 'hbpwmdtnszSZcjykgh':
    i = ord(i)
    for j in 'hbpwmdtnszSZcjykgh':
        j = ord(j)
        substitution_costs[i][j] = 6
        substitution_costs[j][i] = 6

for i, j in zip(F, L):
    i = ord(i)
    j = ord(j)
    substitution_costs[i][j] = 1.5
    substitution_costs[j][i] = 1.5

for i, j in zip('aio', 'AIO'):
    i = ord(i)
    j = ord(j)
    substitution_costs[i][j] = 1.5
    substitution_costs[j][i] = 1.5

for i, j in zip('dtszn', 'jcSZZ'):
    i = ord(i)
    j = ord(j)
    substitution_costs[i][j] = 2
    substitution_costs[j][i] = 2

ojibwe_lev = partial(lev, insert_costs=insert_costs,
                          delete_costs=delete_costs,
                          substitute_costs=substitution_costs)

def from_double_vowel(string):
    skip = False
    result = []
    for i, letter in enumerate(string):
        if skip:
            skip = False
        elif letter == 'e':
            result.append('E')
        elif i == len(string) - 1:
            result.append(letter.lower())
        elif letter in 'aio' and string[i+1] == letter:
            result.append(letter.upper())
            skip = True
        elif letter in 'szc' and string[i+1] == 'h':
            result.append(letter.upper())
            skip = True
        elif letter == "'":
            result.append('h')
        elif letter == 'N':
            result.append(letter)
        else:
            result.append(letter.lower())
    return ''.join(result)

def to_double_vowel(string):
    result = []
    for letter in string:
        if letter in 'AIO':
            result.append(2* letter.lower())
        elif letter in 'cSZ':
            result.append(letter.lower()+'h')
        elif letter == 'e':
            result.append('i')
        elif letter == 'E':
            result.append('e')
        elif letter == 'x':
            pass
        elif letter  == 'N':
            if string[string.index(letter)-1] == 'n':
                pass
            else:
                result.append('n')
        elif letter == 'h':
            result.append("'")
        else:
            result.append(letter)
    return ''.join(result)







#Processes
PALATALIZATIONS = {
        'N':'Z',
        'd':'j',
        't':'c',
        's':'S',
        'z':'Z',
        }
LENGTHENINGS = {
        'a':'A',
        'e':'I',
        'i':'I',
        'o':'O'
        }
SHORTENINGS = {
        'A':'a',
        'E':'i',
        'I':'i',
        'O':'o'
        }
FORTIFICATIONS = {
        'b':'p',
        'd':'t',
        'z':'s',
        'j':'c',
        'Z':'S',
        'g':'k'
        }
LENITIONS = {v: k for k, v in FORTIFICATIONS.items()}
INITIALVOWELCHANGES = {
        'a':'E',
        'e':'E',
        'i':'E',
        'o':'wE',
        'A':'ayA',
        'I':'A',
        'E':'ayE',
        'O':'wA'
        }
class Morpheme():
    stem = False
    modal = False
    peripheral = False
    default_form = ''
    def __init__(self, verb):
        self.verb = verb
        self.form = self.default_form



    @property
    def position(self):
        return list(self.verb.slots.keys()).index(self.slot)

    @property
    def ps(self):
        return ''.join([
            m.form for m in list(self.verb.slots.values())[:self.position] if m
            ])

    @property
    def fs(self):
        return ''.join([
            m.form for m in list(self.verb.slots.values())[self.position + 1:] if m
            ])

    @property
    def preceding(self):
        for m in reversed(list(self.verb.slots.values())[:self.position]):
            if m:
                return m
        return NullMorpheme()

    @property
    def following(self):
        for m in list(self.verb.slots.values())[self.position+1:]:
            if m:
                return m
        return NullMorpheme()

    #Palatalizes final consonant of morpheme
    def final_palatalize(self):
        if re.search(rf'[{Y}]$', self.form):
            self.form = self.form[:-1] + PALATALIZATIONS[self.form[-1]]

    #Lenites initial consonant of morpheme
    def initial_lenite(self):
        if re.search(rf'^[{F}]', self.form):
            self.form = LENITIONS[self.form[0]] + self.form[1:]

    #Fortifies initial consonant of morpheme
    def initial_fortify(self):
        if re.search(rf'^[{L}]', self.form):
            self.form = FORTIFICATIONS[self.form[0]] + self.form[1:]

    def initial_vowel_change(self):
        initial_vowel = re.search(rf'^([{C}]*)([{v+V}])', self.form).group(2)
        self.form = re.sub(rf'^([{C}]*)([{v+V}])', r'\g<1>' +INITIALVOWELCHANGES[initial_vowel], self.form)

    def initial_vowel_lengthen(self):
        if re.search(rf'^([{C}]*)([{v}])', self.form):
            initial_vowel = re.search(rf'^([{C}]*)([{v}])', self.form).group(2)
            self.form = re.sub(rf'^([{C}]*)([{v}])', r'\g<1>' + LENGTHENINGS[initial_vowel], self.form)

    def final_vowel_lengthen(self):
        if re.search(rf'[{v}]$', self.form):
            self.form = re.sub(rf'[{v}]$', LENGTHENINGS[self.form[-1]], self.form)

    #Appends an o to the end of a morpheme
    def o_epenthesis(self):
        if re.search(f'[{C}]$', self.form):
            self.form += 'o'

    #Appends an ε to the end of a morpheme
    def e_epenthesis(self):
        if re.search(f'[{C}]w$', self.form):
            self.form = self.form[:-1] + 'o'
        elif re.search(f'[{C}]$', self.form):
            self.form += 'e'

    #Appends an i to the end of a morpheme and palatalizes self.preceding consonant, if possible
    def i_epenthesis(self):
        if re.search(f'[{C}]w$',self.form):
            self.form = self.form[:-1] + 'o'
        elif re.search(f'[{C}]$', self.form):
            self.final_palatalize()
            self.form += 'i'

    #These are the only
    def apocope(self):
        if re.search(f'[{V}]', self.form) or len(re.findall(f'[{v}]', self.form)) >2:
            if re.search(f'[{v}]$', self.form):
                self.form = self.form[:-1]

    def final_w_loss(self):
        if re.search(f'[{C}]w$', self.form):
            self.form = self.form[:-1]



    def __repr__(self):
        return to_double_vowel(self.form)

    def mutate(self):
        if re.search(f'$[{C}]', self.ps):
            self.preceding.i_epenthesis()

class NullMorpheme(Morpheme):
    peripheral = False
    modal = False
    stem = False
    form = ''
    def __init__(self, *args):
        pass

    def __bool__(self):
        return False


#PERSONAL SUFFIXES
class Ni(Morpheme):
    default_form = 'ni'
    slot = 'personal_prefix'
    def mutate(self):
        if re.search('^b', self.fs):
            self.form = 'im'
        elif re.search(f'^[{L}]', self.fs):
            self.form = 'in'
        elif re.search(f'^[{v}AE]', self.fs):
            self.form = 'ind'
            if re.search('^o', self.fs):
                self.following.initial_vowel_lengthen()
        elif re.search('^[OI]', self.fs):
            self.form = 'n'

class Gi(Morpheme):
    default_form = 'gi'
    slot = 'personal_prefix'
    def mutate(self):
        if re.search(f'^[{v}AE]', self.fs):
            self.form = 'gid'
            if re.search('^o', self.fs):
                self.following.initial_vowel_lengthen()
        elif re.search('^[OI]', self.fs):
            self.form = 'g'

class O(Morpheme):
    default_form = 'o'
    slot = 'personal_prefix'
    def mutate(self):
        if re.search(f'^[{v}AE]', self.fs):
            self.form = 'od'
            if re.search('^o', self.fs):
                self.following.initial_vowel_lengthen()
        elif re.search('^I', self.fs):
            self.form = 'w'
        elif re.search('^O', self.fs):
            self.form = ''
#Stem class:
class Stem(Morpheme):
    slot = 'stem'
    def __init__(self, verb, string):
        self.form = from_double_vowel(string)
        self.verb = verb

#THEME SIGNS 1
class M(Morpheme):
    default_form = 'm'
    slot = 'm_obviative'
    def mutate(self):
        self.preceding.e_epenthesis()

class I(Morpheme):
    default_form = ''
    slot = 'theme_sign'
    def mutate(self):
        self.preceding.i_epenthesis()
        if self.following.peripheral:
            self.verb.slots['minor'] = None


class Am(Morpheme):
    default_form = 'am'
    slot = 'theme_sign'
    def mutate(self):
        if type(self.following) == Ni_animate:
            pass
        elif type(self.following) == Nimperative:
            self.form = 'a'
        elif type(self.following) == Ng:
            self.e_epenthesis()
        elif re.search(f'^[{Q}]', self.fs):
            self.form = 'A'

class Aam(Morpheme):
    default_form = 'Am'
    slot = 'theme_sign'
    def mutate(self):
        self.preceding.form = self.preceding.form[:-1]
        if type(self.following) == Ng:
            self.e_epenthesis()
        elif re.search(f'^[{Q}]', self.fs):
            self.form = 'A'

#THEME SIGNS 2
class Aa(Morpheme):
    default_form = 'A'
    def __init__(self, verb, slot):
        self.verb = verb
        self.slot = slot
        self.form = self.default_form

class N2ndPerson(Morpheme):
    default_form = 'n'
    def __init__(self, verb, slot):
        self.form = self.default_form
        self.verb = verb
        self.slot = slot

    def mutate(self):
        #AW Contraction
        if re.search('aw$', self.ps):
            self.preceding.form = self.preceding.form[:-2] + 'O'
        else:
            self.preceding.e_epenthesis()
        if type(self.following) == Si:
            self.form = self.form[:-1]
        if type(self.following) == Mw:
            self.form += 'in'


class Go(Morpheme):
    default_form = 'go'
    slot = 'theme_sign'
    def mutate(self):
        #AW Contraction
        if re.search('aw$', self.ps):
            self.preceding.form = self.preceding.form[:-2] + 'A'
        elif self.preceding.form == 'iN':
            self.preceding.form = 'i'
        else:
            self.preceding.e_epenthesis()
        if self.following.peripheral:
            self.form = self.form[:-1] + 'O'
        if not self.following:
            self.form = self.form[:-1]


class Goo(Morpheme):
    default_form = 'gO'
    slot = 'theme_sign'
    def mutate(self):
        #AW Contraction
        if re.search('aw$', self.ps):
            self.preceding.form = self.preceding.form[:-2] + 'A'
        elif self.preceding.form == 'iN':
            self.preceding.form = 'i'
        else:
            self.preceding.e_epenthesis()


class Shi(Morpheme):
    default_form = 'Si'
    slot = 'theme_sign'
    def mutate(self):
        self.preceding.i_epenthesis()

#Negative
class Si(Morpheme):
    default_form = 'si'
    slot = 'negative'
    def mutate(self):
        if re.search(f'[{Q}]$', self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'n'
            self.initial_lenite()

class Sin(Morpheme):
    default_form = 'sin'
    slot = 'negative'
    def mutate(self):
        if re.search(f'[{Q}]$', self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'n'
            self.initial_lenite()
        elif re.search(f'd$', self.ps):
            self.preceding.form = self.preceding.form[:-1]


class Wnegative(Morpheme):
    default_form = 'w'
    slot = 'negative_w'
    def mutate(self):
            if type(self.following) == Ng:
                if self.verb.dubitative:
                    return
                else:
                    self.form = ''
                    return
            elif type(self.following) == D:
                self.form = ''
                return
            elif self.following.peripheral:
                self.preceding.final_vowel_lengthen()
                self.form = ''
                return
            if type(self.following) == N2ndPerson and type(self.preceding) == N2ndPerson:
                self.form = 'O'
                return
            if (type(self.following) == NullMorpheme or type(self.following) in (W3rdperson, Local_singular)
            and type(self.following.following) == NullMorpheme)\
            and type(self.preceding) == Si:
                if self.verb.variants['siin/sii'] == 'siin':
                    global current_variants, default_variants
                    self.preceding.form = self.preceding.form[:-1] + 'In'
                    self.form = ''
                    current_variants.append({**default_variants, 'siin/sii': 'sii'})
                    return
                elif self.verb.variants['siin/sii'] == 'sii':
                    self.preceding.form = self.preceding.form[:-1] + 'I'
                    self.form = ''
                    return
            if re.search(f'[{C}]$', self.ps):
                self.preceding.o_epenthesis()
                if re.search(f'^[{C}]', self.fs):
                    self.form = ''
            elif re.search(f'^[{C}]', self.fs):
                self.preceding.final_vowel_lengthen()
                self.form = ''





class Wdelayed(Morpheme):
    default_form = ''
    slot = 'w_delayed'
    def mutate(self):
        self.preceding.o_epenthesis()
        self.preceding.final_vowel_lengthen()


class Wdubitative(Morpheme):
    default_form = 'w'
    slot = 'dubitative_w'
    def mutate(self):
        if type(self.following) == Ng:
            if self.verb.dubitative:
                self.preceding.o_epenthesis()
                self.form = 'w'
            else:
                self.form = ''
            return
        elif re.search(f'^[{C}]', self.fs):
            if not self.preceding.stem:
                self.preceding.final_vowel_lengthen()
            self.form = ''
        self.preceding.o_epenthesis()

#CENTRAL SIGNS
class Mw(Morpheme):
    default_form = 'mw'
    slot = 'major'
    def mutate(self):
        self.preceding.e_epenthesis()
        if self.following.peripheral:
            self.verb.slots['minor'] = None
        if self.following.modal:
            self.form += 'A'

class Min(Morpheme):
    default_form = 'min'
    slot = 'major'
    def mutate(self):
        self.preceding.e_epenthesis()
        if self.following.peripheral:
            self.verb.slots['minor'] = None
        if self.following.modal:
            self.form += 'A'

class Local_singular(Morpheme):
    default_form = ''
    slot = 'major'
    def mutate(self):
        if self.following.modal:
            self.form = 'nA'
        if self.form == 'nA':
            if type(self.preceding) == Wnegative:
                self.preceding.form = ''
                self.preceding.preceding.final_vowel_lengthen()
            else:
                self.preceding.e_epenthesis()

class Nsingular(Morpheme):
    default_form = 'n'
    slot = 'major'
    def mutate(self):
        if self.following.modal:
            self.form += 'A'

class Naan(Morpheme):
    default_form = 'nAn'
    slot = 'major'
    def mutate(self):
        if self.following.modal:
            self.form = self.form[:-1]
        if self.following.peripheral:
            self.form += 'i'

class Daa(Morpheme):
    default_form = 'dA'
    slot = 'major'
    def mutate(self):
        if self.following.peripheral:
            self.form += 'ni'
        if re.search('m$', self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'n'


class Naawaa(Morpheme):
    default_form = 'nAwA'
    slot = 'major'


class W3rdperson(Morpheme):
    default_form = 'w'
    slot = 'major'
    def mutate(self):
        if self.following.modal:
            self.preceding.o_epenthesis()
            if type(self.following) == Ban:
                #ooban
                self.preceding.final_vowel_lengthen()
                self.form = ''
            elif type(self.following) == Dog:
                #widog, owidog
                if self.verb.variants['widog']:
                    global current_variants, default_variants
                    self.form = 'wi'
                    current_variants.append({**default_variants, 'widog': False})
                else:
                    #odog
                    self.form = ''
            return
        if type(self.preceding) in (Stem, Goo, Wnegative) and not self.following:
            self.form =  'x'
            return
        elif not self.following.peripheral:
            self.preceding.o_epenthesis()
        elif self.following.peripheral:
            if re.search(f'[{C}]$', self.ps):
                self.form = 'O'
        elif re.search(f'^[{C}]', self.fs):
            self.preceding.final_vowel_lengthen()
            self.form = ''

class W0thPerson(Morpheme):
    default_form = 'w'
    slot = 'major'
    def mutate(self):
        if type(self.following) == NullMorpheme:
            self.form = ''
        elif type(self.following) == Dog:
            if type(self.preceding) == Ni_inanimate:
                self.form = 'wi'
            else:
                self.preceding.o_epenthesis()
                self.form = ''
        elif type(self.following) == Ban:
            if re.search(fr'[{C}]$', self.ps):
                self.form = 'O'
            elif re.search(fr'[{v+V}]$', self.ps):
                self.preceding.final_vowel_lengthen()
                self.form = ''
        elif type(self.preceding) == Sin and type(self.following) in (NullMorpheme, An_):
            self.form = 'On'
            self.verb.slots['minor'] = NullMorpheme()

#Conjunct Indexing Morphemes
class Aan(Morpheme):
    default_form = 'An'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if type(self.following) == Ban:
            self.form = self.form[:-1] + 'm'
            self.following.initial_vowel_lengthen()
        if self.following.peripheral:
            self.i_epenthesis()


class Ag(Morpheme):
    default_form = 'ag'
    slot = 'major'
    def mutate(self):
        if self.following.peripheral:
            self.i_epenthesis()


class An(Morpheme):
    default_form = 'an'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if type(self.following) == Ban:
            self.form = self.form[:-1] + 'm'
        if self.following.peripheral:
            self.i_epenthesis()


class Ad(Morpheme):
    default_form = 'ad'
    slot = 'major'
    def mutate(self):
        if self.following.peripheral:
            self.i_epenthesis()


class Aang(Morpheme):
    default_form = 'Ang'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if self.following.peripheral:
            self.i_epenthesis()


class Angid(Morpheme):
    default_form = 'angid'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if self.following.peripheral:
            self.i_epenthesis()


class Ang(Morpheme):
    default_form = 'ang'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if self.following.peripheral:
            self.i_epenthesis()


class Egw(Morpheme):
    default_form = 'Egw'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{v+V}]$', self.ps):
            self.preceding.form += 'y'
        if type(self.following) == Ban or self.following.peripheral:
            self.form = self.form[:-1] + 'i'


class Ng(Morpheme):
    default_form = 'ng'
    slot = 'special'
    def mutate(self):
        if self.verb.dubitative:
            self.form = 'Ing'
        if self.form == 'ng':
            self.preceding.i_epenthesis()


class Ind(Morpheme):
    default_form = 'ind'
    slot = 'major'
    def Mutate(self):
        if self.following.peripheral:
            self.i_epenthesis()

class Agogw(Morpheme):
    default_form = 'agogw'
    slot = 'major'
    def mutate(self):
        if self.following.modal:
            self.form = 'agOgw'


class D(Morpheme):
    default_form = 'd'
    slot = 'major'
    def mutate(self):
        if self.verb.dubitative or not self.verb.polarity:
            self.form = 'gw'
            if not self.verb.dubitative:
                self.verb.slots['negative'].form = self.verb.slots['negative'].form[0] + 'i'
        if self.form == 'gw':
            self.preceding.o_epenthesis()
        elif re.search(f'[{Q}]$', self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'n'
            self.form = 'g'
        elif type(self.following) == Ban:
            self.following.form = 'p' + self.following.form[1:]
            self.form = ''
        if self.following.peripheral:
            self.i_epenthesis()

class G(Morpheme):
    default_form = 'g'
    slot = 'major'
    def mutate(self):
        if self.verb.dubitative:
            self.form ='gw'
            if not self.verb.polarity:
                if type(self.preceding) == Sin:
                    #sinoogwen, #sinoogobanen
                    self.preceding.form += 'O'
                    return
                elif type(self.preceding) == Ni_inanimate:
                    #sininigobanen
                    if type(self.following) != Ban:
                        #siniigwen
                        self.preceding.final_vowel_lengthen()
                        return
                    return
        if self.form == 'gw':
            self.preceding.o_epenthesis()
        elif self.ps[-1] == 'd':
            self.preceding.form = self.preceding.form[:-1]
            self.form = 'k'
        if type(self.preceding) == Sin:
            self.preceding.o_epenthesis()
        if type(self.following) == Ban:
            self.i_epenthesis
            if type(self.preceding) == Sin:
                #sinoogiban
                self.preceding.final_vowel_lengthen()

class K2ndPerson(Morpheme):
    default_form = 'k'
    slot = 'major'
    def mutate(self):
        if self.verb.dubitative:
            self.form = 'gw'
        if type(self.preceding) == N2ndPerson:
            self.preceding.form = self.preceding.form[1:]
        if self.form == 'k' and self.following.peripheral:
            self.i_epenthesis()


class Waaw(Morpheme):
    default_form = 'wA'
    def __init__(self, verb, slot):
        self.verb = verb
        self.slot = slot
        self.form = self.default_form
    def mutate(self):
        if re.search(f'[{C}]w$', self.ps):
            self.preceding.form = self.preceding.form[:-1]


class Waa(Morpheme):
    default_form = 'wA'
    slot = 'special'
    def mutate(self):
        self.preceding.o_epenthesis()


class Ni_animate(Morpheme):
    default_form = 'ni'
    slot = 'special'
    def mutate(self):
        if re.search(f'[{C}]$', self.ps):
            self.preceding.e_epenthesis()
        if self.following.modal:
            self.form = self.form[:-1] + 'A'

class Ni_inanimate(Morpheme):
    default_form = 'ni'
    slot = 'special'
    def mutate(self):
        if re.search(f'[{C}]$', self.ps):
            self.preceding.e_epenthesis()


class Kdelayed(Morpheme):
    default_form = 'k'
    slot = 'mode'
    def mutate(self):
        if re.search(f'[{Q}]$', self.ps):
            self.preceding.form[-1] = self.preceding.form[:-1] + 'n'
            self.initial_lenite()


class Ke(Morpheme):
    default_form = 'kE'
    slot = 'mode'
    def mutate(self):
        if re.search(f'[{Q}]$', self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'n'
            self.initial_lenite()
        if re.search(f'^[{V}]', self.fs):
            self.form = self.form[:-1]




class Ban(Morpheme):
    default_form = 'ban'
    modal = True
    slot = 'mode'
    def mutate(self):
        if not re.search('m$', self.ps):
            self.preceding.e_epenthesis()
        if self.following.peripheral:
            if self.verb.variants['banii/bane'] == 'bane':
                self.form += 'E'
                global current_variants, default_variants
                current_variants.append({**default_variants, 'banii/bane': 'banii'})
            elif self.verb.variants['banii/bane'] == 'banii':
                self.form += 'I'

class Dog(Morpheme):
    default_form = 'dog'
    modal = True
    slot = 'mode'
    def mutate(self):
        if self.following.peripheral:
            if self.form == 'dog':
                self.form += 'En'

class En_dubitative(Morpheme):
    default_form = 'En'
    slot = 'en'
    def mutate(self):
        if type(self.preceding) == Waaw:
            self.preceding.form += 'w'



class PeripheralMorpheme(Morpheme):
    peripheral = True
    slot = 'minor'
    def mutate(self):
        if re.search(f'[{C}]w$',self.ps):
            self.preceding.form = self.preceding.form[:-1] + 'O'
            self.form = self.form[-1:]
        elif re.search(f'[{v+V}]$', self.ps):
            self.form = self.form[-1:]

class An_(PeripheralMorpheme):
    default_form = 'an'

class Ag_(PeripheralMorpheme):
    default_form = 'ag'

class Ah_(PeripheralMorpheme):
    default_form = 'ah'


class Nimperative(Morpheme):
    default_form = 'n'
    slot = 'major'
    def mutate(self):
        if re.search(f'[{Q}]$', self.ps):
            self.preceding.e_epenthesis()
        if self.following.peripheral:
            self.verb.slots['minor'] = None


class Og(Morpheme):
    default_form = 'g'
    slot = 'major'
    def mutate(self):
        if self.verb.type == 'vta' and self.verb.mode == 'neutral':
            self.preceding.e_epenthesis()
            self.form = 'k'
        else:
            if re.search(rf'[{v+V}]$', self.ps):
                self.preceding.form += 'y'
            if re.search(rf'[{C}]$', self.ps):
                self.preceding.o_epenthesis()
        if self.following.peripheral:
            self.verb.slots['minor'] = NullMorpheme()


class Gon(Morpheme):
    default_form = 'gon'
    slot = 'major'
    def mutate(self):
        if self.following.peripheral:
            self.verb.slots['minor'] = NullMorpheme()


class Aangen(Morpheme):
    default_form = 'AngEn'
    slot = 'major'

class Naam(Morpheme):
    default_form = 'nAm'
    def mutate(self):
        global current_variants, default_variants
        if self.verb.variants['shinaang?'] == 'shinaang':
            self.form = 'nAng'
            current_variants.append({**default_variants, 'shinaang?': 'shinaam'})
        elif self.verb.variants['shinaang?'] == 'shinaam':
            self.form = 'nAm'
            current_variants.append({**default_variants, 'shinaang?': 'shinaan'})
        elif self.verb.variants['shinaang?'] == 'shinaan':
            self.form = 'nAn'




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
