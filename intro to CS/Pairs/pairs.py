import re

# καθαρίζει το κείμενο απο ειδικούς χαρακτήρες και σημεία στιξεις
# κρατάει μόνο τα γράμματα
# σπάει το κέιμενο σε λίστα όπου το κάθε στοιχείο είναι μια λέξη
def clean_text(text):
    text_ascii = re.sub('[^a-zA-Z]+', ' ', text)
    text_ascii = text_ascii.split(" ")
    text_ascii = remove_empty_values(text_ascii)
    return(text_ascii)


#αφαιρεί τα κενα στοιχεία-λέξεις από την παραπάνω λίστα
def remove_empty_values(lst):
    return [value for value in lst if value != ""]


def main(text_ascii):
    end_of_pairs = False
    i = 0
    
    while i < len(text_ascii):
        if end_of_pairs == True:
            break

        found = False
        j = 0
        # για κάθε στοιχείο της λίστας γίνεται έλγχος με κάθε άλλο στοιχείο της λίστα
        # για το αν το άθροισμα των χαρακτήρων τους είναι ίσο με 20
        # αν ισχύει αυτό τα δύο στοιχεία αφαιρούνται απο την λίστα και η διαδικασία 
        # επαναλαμβάνεται για τα επόμενα στοιχεία
        while found == False:
            if j>=len(text_ascii):
                break
            sum = len(text_ascii[i])+len(text_ascii[j])
            
            if sum == 20:
                print(text_ascii[i],text_ascii[j],len(text_ascii))
                try:
                    del text_ascii[i]
                    del text_ascii[j]
                except IndexError:
                    pass
                found = True

            j = j+1
        if found ==False:
            i = i+1
    

if __name__ == "__main__":
    text = open("sampletext.txt", "r",encoding='utf-8')
    text_ascii = clean_text(text.read())
    print("length of the starting text",len(text_ascii))
    main(text_ascii)
    print(text_ascii)
    print("length of the ending text",len(text_ascii))
