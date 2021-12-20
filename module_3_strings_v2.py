import re
# Source text
txt = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
source = re.sub(r' iz ', ' is ', txt.lower())

#print(source)

# Additional sentence creation

addit_sentence = []
for s in re.sub(r'\n|\t', '', source).replace(':', '.').split("."):
    addit_sentence.extend(re.findall(r'\w+$', s))
addit_sentence = (' '.join(str(i) for i in addit_sentence) + '.')
print(" Additional sentence is:\n",addit_sentence)
print()

# Text normalization

tab = source.split('\t')

#print (tab)

tab_norm = []
normalized_text = ""

# Capitalize after tabular
for i in tab:
    i = i.lower()
    i = i.strip()
    i = i.replace('\n\n', '\n')
    i = i.replace('\n', '')
    i = i.replace('\t', '')
    i = i.replace(':', '.')
    i = i.capitalize()
    tab_norm.append(i)
#print('. '.join(tab_norm))

#Insert the additional sentence into the text
tab_norm.insert(3, addit_sentence)
for y in tab_norm:
    normalized_text += y + "\n"


print(normalized_text)

a = normalized_text.split('. ')
# print("A",a)


b = []
for y in a:
    y = y.capitalize()
    y = y.strip()
   # y = y.replace('\n\n', '\n')
    #y = y.replace('\n', '')
    #y = y.replace('\t', '')
    y = y.replace('Homework.', 'Homework:')
    b.append(y)
#print (b)
capitalized = ('. '.join(b))
#capitalized = ('. '.join(str(e) for e in b).capitalize())
print (capitalized)
#



## Whitespaces calculation
spaces = 0
for i in txt:
    spaces += i.count(" ")
    spaces += i.count("\n")
    spaces += i.count("\t")
print()
print("The number of whitespaces is:", spaces)




