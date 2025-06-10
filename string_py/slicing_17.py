#write a program to fill in a letter templete given below with name and date.
letter='''
          Dear <|Name|>
          You are selected!
          <|Date|>
         '''
print(letter.replace("<|Name|>","pranav").replace("<|Date|>","05/12/2006"))