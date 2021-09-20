# Hangman game by Filip Hostinsky


with open("added_words_log", "w") as file:
    file.write("test")
from New_Defs import *

word_list = words()
check = str(input("Please check if your word is in the library: \n"))

with open("added_words_log", "r+") as f:
    s = ""
    if 0 == word_list.count(check):
        c = f.read()
        c = re.sub("[^\w]", " ", c).split()
        c.append(check)
        c = set(c)
        c = list(c)
        for word in c:
            s += word + " "
        with open("added_words_log", "w") as file:
            file.write(s + " ")

if 0 != word_list.count(check):
    print("The word is in the library, the length is {}".format(len(check)))
else:
    print("The word has been added to the library, the length is {}".format(len(check)))
    word_list.append(check)

word_list, word_list_b, lose_rules, numx, st, list, numbers, asked_correctly = sorted(word_list), "", 0, 0, 0, [], "", 0
word_len = len_word()
game_still_going = True
# Now the program will ask for E in the word and it's place   ----    E
used, ff, uu, = "", "e", 0
while game_still_going:
    asking_letter = ff[0]
    a = "Is there {} in the word? [y/n] \n".format(asking_letter)

    pos, mn, x, word_e_ask = 0, 0, 1, ""
    # Asks for {} in the word
    word_e_ask, mn, askTrue = ask(a, mn, word_e_ask)
    # -----------Ask E
    num2 = 0
    if word_e_ask == "y":
        num2 = 1
    # -----------Ask place;
    if mn == 0:
        pos = wh_place(num2, pos, word_len, asked_correctly)
    else:
        pos = mn - 1
        num2 = 1

    print("---------- ---------- ---------- ---------- \nLet's continue:  ")
    most_com, position_most_c_letter = "", ""
    used = used + " " + asking_letter
    print("Asked were:", used)

    print("asking letter was:", asking_letter)
    word_list_new, word_list_b = "", []

    # SORTING
    word_list_new, word_len, pos, asking_letter, num2, word_list, word_listb, used, lose_rules, asked_correctly = sort(
        word_list_new,
        word_len, pos,
        asking_letter,
        num2, word_list,
        word_list_b, used,
        lose_rules,
        asked_correctly)

    print("Possible words:", word_listb)
    if lose_rules < 100:
        if lose_rules < 3:
            print("Score: {}/3".format(lose_rules))
        elif lose_rules:
            print("I have lost")
            lose_rules += 100
    print("\n")
    list, st, numbers = places(word_len, pos, asking_letter, askTrue, st, list, numbers)
    print("\n")

    if len(word_list_b) == 1:
        print(word_listb[0], "- Your word has been discovered! \nI have won")
        game_still_going = False
        break
    try:
        ff = collections.Counter(word_list_new).most_common(1)[0]
        print(ff)
        print("The most common letter is {}".format(ff[0]))
    except(ValueError, IndexError):
        print("Your word has not been discovered.")
        game_still_going = False
        break

input("Please press ENTER to exit   ")
