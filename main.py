import random


with open("wordle-La.txt", "r") as f:
    word_list = [word.strip().upper() for word in f if len(word.strip()) == 5]

secret_word = random.choice(word_list)

print("The word is: " + "_"*len(secret_word))
print(secret_word)

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters_count_dict = {}

while True:
    myWord = input("\nChoose your answer: ")

    word_copie = myWord.upper()
    print(word_copie)

    if word_copie == secret_word:
        print("You won!")
        break

    if word_copie not in word_list:
        print("Please enter a valid word!")
        continue
    elif len(word_copie) < len(secret_word) or len(word_copie) > len(secret_word):
        print("The word is 5 letters long, please write a valid word!")
        continue

    for i in word_copie:
        #check right letter if in right place
        for j in secret_word:
            if i == j:
                print(f"{i} : {secret_word.index(j)}")

        # if i in letters:
        #     letter_count = word_copie.count(i)
        #     word_copie = word_copie.replace(i, '')
        # else:
        #     print("Please enter a letter!")
        
        # if letter_count == 0:
        #     continue
        # else:
        #     letters_count_dict.update({i:letter_count})
        
    

