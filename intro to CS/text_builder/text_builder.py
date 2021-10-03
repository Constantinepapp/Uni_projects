import random
import re


# καθαρίζει το κείμενο απο σημεία στιξης και ειδικούς χαρακτήρες
# σπάει το κείμενο σε μια ίστα όπου κάθε στοιχείο είναι μια λέξη
def clean_text(text):
    text_ascii = re.sub('[^a-zA-Z]+', ' ', text)
    text_ascii = text_ascii.split(" ")
    text_ascii = remove_empty_values(text_ascii)
    return(text_ascii)

# αφαιρει τα άδεια στοιχεία λίστας απο το κείμενο
def remove_empty_values(lst):
    return [value for value in lst if value != ""]


def search_triades(last_words,triades):
    for i in range(0,len(triades)):
        if triades[i][0] == last_words[0]:
            if triades[i][1] == last_words[1]:
                return triades[i][2]
    return "not found"


def main(text_ascii):
    triades = []

    # δημιυργούμε μια λίστα οπου κάθε στοιχείο είναι μια λίστα 3 συνεχόμενων λέξεων
    for i in range(0,len(text_ascii)):
        if i < len(text_ascii) -2:
            triada = [text_ascii[i],text_ascii[i+1],text_ascii[i+2]]
            triades.append(triada)


    x = random.randrange(0,len(triades))

    # αρψικοποιούμε το τελικό κείμενο με μια τυχαία τριάδα λέξεων
    final_text = []
    triada = triades[x]
    for item in triada:
        final_text.append(item)

    while len(final_text)<200:
        next_word = search_triades(final_text[-2:],triades)
        if triada == "not found":
            print("can't create more combinations")
        final_text.append(next_word)
    


    print(" ".join(final_text),"\n" )
    print(len(final_text)," words printed")





if __name__ == "__main__":
    text = open("startingtext.txt", "r",encoding='utf-8')
    text_ascii = clean_text(text.read())
    main(text_ascii)


