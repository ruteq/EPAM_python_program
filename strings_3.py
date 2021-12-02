import re

txt = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


txt_1 = txt.capitalize()
txt_2 = txt.splitlines()

print (txt_2)
# #print(txt_1, [5])

# new_txt = []
#
# for sentence in txt_2:
#     if
# print(new_sentence)


# spaces = 0
# new_line = 0
# for i in txt:
#     if i == ' ':
#         spaces = spaces + 1
#     elif i == '\n':
#         new_line = new_line + 1
# print ("Spaces count: ", spaces)
# print ("New line count: ", new_line)
# print(txt_1, [5])
#
# result = re.search(r' ', txt)
# print(result)
# #print(result.group())




#txt1.replace('iz', 'is')

#print(txt1)

# result = re.search(r' iz? ', txt1)
# print (result.group())