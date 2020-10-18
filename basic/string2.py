#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  """
  function has a string parameter if length of string more than 3 it adds "ing" 
  to its end if it has "ing" in its end we add "ly" instead and return this string
  if length of string less than 3 we return the string
  """
  return f"{s}{'ly' if s.endswith('ing') else 'ing'}" if len(s) > 3 else s
  


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  """
  function takes a string parameter and get substrings "not" & "bad"
  if "not" appears before "bad" it replaces the sentence "not .. bad" with "good"
  and return resulting string if not it return the same string
  """
  if s.find('not') + len('not') <= s.find('bad'):
      return s.replace(s[s.find('not'):s.find('bad') + len('not')] , 'good')
  else:
      return s



# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  """
  function has two strings as parameters a , b it returns 
  front half of a + front half of b + back half of a + back half of b
  if length of a or b odd the front half increase one of back half
  """
  len_a = len(a)//2
  len_b = len(b)//2
  if len(a)%2 == 0 and len(b)%2 == 0:
      return f"{a[:len_a]}{b[:len_b]}{a[len_a:]}{b[len_b:]}" 
  elif len(a)%2 != 0 and len(b) !=0:
      return a[:len_a+1] + b[:len_b+1] +a[len_a+1:]+b[len_b+1:]
  else:
      return a[:len_a] + b[:len_b+1] +a[len_a:]+b[len_b+1:]

        
     
     
  
  


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')
  test(front_back('abc', 'xyz'), 'abxycz')

if __name__ == '__main__':
  main()
