from __future__ import print_function
import unittest
import sys

alphabet = dict()
alphabet['a']='alpha';       
alphabet['b']='bravo';      
alphabet['c']='charlie';    
alphabet['d']='delta';      
alphabet['e']='echo';       
alphabet['f']='foxtrot';    
alphabet['g']='golf';       
alphabet['h']='hotel';      
alphabet['i']='india';      
alphabet['j']='juliett';    
alphabet['k']='kilo';       
alphabet['l']='lima';       
alphabet['m']='mike';       
alphabet['n']='november';   
alphabet['o']='oscar';      
alphabet['p']='papa';       
alphabet['q']='quebec';     
alphabet['r']='romeo';      
alphabet['s']='sierra';     
alphabet['t']='tango';      
alphabet['u']='uniform';    
alphabet['v']='victor';     
alphabet['w']='whiskey';    
alphabet['x']='x-ray';      
alphabet['y']='yankee';     
alphabet['z']='zulu';       

def phonetic(string):
    if not string:
        return string

    ret = ""
    for character in string:
        try:
            phonetic = alphabet[character.lower()]
        except KeyError:
            ret += character + "\n"
            continue

        if character.isupper():
            ret += phonetic[0].upper() + phonetic[1:] + "\n"
        else:
            ret +=  phonetic + "\n"

    return ret

class TestPhonetic(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(phonetic(""), "")
    def test_lower(self):
        self.assertEqual(phonetic("a"), "alpha\n")
        self.assertEqual(phonetic("ab"), "alpha\nbravo\n")
    def test_upper(self):
        self.assertEqual(phonetic("A"), "Alpha\n")
        self.assertEqual(phonetic("AB"), "Alpha\nBravo\n")
    def test_others(self):
        self.assertEqual(phonetic(","), ",\n")
        self.assertEqual(phonetic("CS2050"), "Charlie\nSierra\n2\n0\n5\n0\n")

if "__main__" == __name__:
    for line in sys.stdin:
        print(phonetic(line))
