# Assignment written by: ___Sejin Yoon___


sentence = input("Enter a sentence: ")
words = sentence.split()

print("Length of each word:")
for word in words:
    print(word + ":", len(word))

avg_word_length = sum(len(word) for word in words) / len(words)
print("Average word length: {:.2f}".format(avg_word_length))

