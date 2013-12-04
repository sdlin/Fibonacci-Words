Fibonacci-Words
===================

Take F(x) to be any bijective map from the set of letters [a...z] to the set of integers [0...25].
A Fibnoacci-Word, as used here, is a word, WORD, such that [F(letter) for letter in WORD] is a fibonacci number.

So given the one-to-one map between the letters a...z and the numbers 0...25, the word can be expressed as a fibonacci number.

As an example, take the word "aphorismos".

If we use the map where: <br />
a: 4 <br />
p: 8 <br />
h: 0 <br />
o: 7 <br />
r: 5 <br />
i: 2 <br />
s: 6 <br />
m: 9 <br />

Then we get that "aphorismos" can be represented as the 48th Fibonacci number, 4807526976.

This script finds the longest word that is also a fibonacci-word.  Note, it requires some long list of words (presumeably a long list of valid English words), which I've not included in this repository.  An example output is included in "output.txt"