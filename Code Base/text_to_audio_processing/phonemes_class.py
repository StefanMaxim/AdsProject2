import numpy as np
import nltk
from nltk.corpus import cmudict

class Phonemes:
    # Initialize the CMU Pronouncing Dictionary
    d = cmudict.dict()
    low_pitch_phonemes = np.array(["AA1", "AO1", "AE", "AH1", "ER0", "OW"])

    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}


    def test(self):
        # Specify the word for which you want phonemes
        word = ("father")
        # Get the list of phonemes for the word
        phonemes_list = d[word.lower()]

        # Print the phonemes
        print(f"Phonemes for '{word}': {phonemes_list}")

    def low_pithed_count_in_sentence(self, ad_text):
        words = ad_text.split()

        total_words = 0
        low_pitched = 0
        for word in words:
            print ("WORD= ", word)
            if word.isdigit() == False:
                #print ("word= ", word)
                total_words = total_words + 1
                if self.is_low_pitched_word(word) == True:
                    low_pitched = low_pitched + 1

        return (low_pitched / total_words) * 100

    def is_low_pitched_word(self, word):

        if word not in self.d:
            #print("not a word")
            return False

        if word.isdigit() == True:
            #ignore numbers
            return False

        phonemes_list = self.d[word.lower()]
        #print("list=", phonemes_list)

        # Check which elements of array1 are present in array2
        common_elements = np.in1d(self.low_pitch_phonemes, phonemes_list[0])
        #print("common_elements", common_elements)

        # Check if at least one element is True
        at_least_one_true = False
        at_least_one_true = np.any(common_elements)

        if  at_least_one_true:
            return True
        else:
            return  False


# Main program logic
if __name__ == "__main__":
    my_phonemes = Phonemes()

    #word = "dfvbvcxbvxc"
    #print (word, " is low pitched: " , is_low_pitched_word(word))

    #para = "Lucerne Cottage cheese 16 ounces, 1.99 Member price cup"
    para = "Lucerne Cottage Cheese, 16 ounces, is on sale for 2 for 5 dollars at the member price." \
            "Open Nature Almond Beverage, half gallon, or Florida's Natural Orange or Grapefruit Juice, 52 ounces, are available for 2 for 6 dollars at the member price." \
            "Lucerne Flavored Creamer, 32 ounces, is on sale for 2 for 7 dollars at the member price." \
            "Clover Organic Milk, half gallon, is priced at 4.99 dollars at the member price." \
            "Signature SELECT Frozen Fruit, 8 to 16 ounces, is available for 3.99 dollars at the member price." \
            "Bertolli Pasta Sides, 48 ounces, are priced at 6.99 dollars at the member price." \
            "Restaurant Style French Fries or Rings, 16 to 28 ounces, are available for 2 for 9 dollars at the member price." \
            "El Monterey Burritos or Chimichangas Family Pack, 30.4 to 32 ounces, are priced at 4.99 dollars at the member price." \
            "Rao's Entrée, 8.5 to 9 ounces, is on sale for 4.99 dollars at the member price." \
            "Totino's Pizza Rolls, 50 count, or Screamin' Sicilian Pizza, 22 to 25 ounces, are priced at 5.99 dollars at the member price."
    # Remove commas from the sentence
    para_without_commas = para.replace(",", " , ")
    para_without_commas = para_without_commas.replace(".", " . ")
    print (para_without_commas)
    print ( "% low pitch words = ", my_phonemes.low_pithed_count_in_sentence(para_without_commas))



'''
https://www.nltk.org/_modules/nltk/corpus/reader/cmudict
Phonemes: There are 39 phonemes, as shown below:

Phoneme Example Translation    Phoneme Example Translation
------- ------- -----------    ------- ------- -----------
AA      odd     AA D           AE      at      AE T
AH      hut     HH AH T        AO      ought   AO T
AW      cow     K AW           AY      hide    HH AY D
B       be      B IY           CH      cheese  CH IY Z
D       dee     D IY           DH      thee    DH IY
EH      Ed      EH D           ER      hurt    HH ER T
EY      ate     EY T           F       fee     F IY
G       green   G R IY N       HH      he      HH IY
IH      it      IH T           IY      eat     IY T
JH      gee     JH IY          K       key     K IY
L       lee     L IY           M       me      M IY
N       knee    N IY           NG      ping    P IH NG
OW      oat     OW T           OY      toy     T OY
P       pee     P IY           R       read    R IY D
S       sea     S IY           SH      she     SH IY
T       tea     T IY           TH      theta   TH EY T AH
UH      hood    HH UH D        UW      two     T UW
V       vee     V IY           W       we      W IY
Y       yield   Y IY L D       Z       zee     Z IY
ZH      seizure S IY ZH ER
'''
