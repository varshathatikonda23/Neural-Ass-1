user_sentence = input("Enter the sentence: ")
sentence_list = user_sentence.split(" ")
new_list = []
index = 0

while index < len(sentence_list):
    if sentence_list[index] == "python":
        new_list.append("pythons")
    else:
        new_list.append(sentence_list[index])
    index += 1

resultant_sentence = ""
for word in new_list:
    resultant_sentence = resultant_sentence + word + " "

print(resultant_sentence)