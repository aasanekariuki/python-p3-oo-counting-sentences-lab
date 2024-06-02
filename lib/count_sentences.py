#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self.value = value
        
        if (isinstance (value, str)):
            
          print("The value must be a string.")
        
        
    def is_sentence(self):
        if self.value.endswith ("."):
            return True
        
        else: 
            return False
        
    def  is_question(self):
         if self.value.endswith("?"):
             return True
         
         else:
             return False
         
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        
        else:
            return False
        
    def count_sentences(self):
        
          sentences = re.split(r'[.!?]', self._value)
        
          return len([sentence for sentence in sentences if sentence.strip() != ""])
pass