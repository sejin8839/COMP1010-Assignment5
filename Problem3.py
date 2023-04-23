# Assignment written by: ___Sejin Yoon___


sentence = input("Enter a sentence: ")

words = sentence.split()  # split the sentence into words
num_words = len(words)   # count the number of words
total_length = sum(len(word) for word in words)  # sum the length of each word

average_length = total_length / num_words  # calculate the average length

print(words)
print(len(words))
print("The average word length in the sentence is:", round(average_length, 2))
