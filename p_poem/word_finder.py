input_txt=open("poem.txt")
text=input_txt.read()
text=text.lower()
words=text.split()
word_counter=0
for i in words:
    if i=="land":
       word_counter+=1

print(word_counter)