# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
from pydub import AudioSegment
from phonemes_class import Phonemes
import ffmpeg
import os;
import ffmpy
from ffmpeg_util_class import Ffmpeg_Util
import file_util


# The text that you want to convert to audio
mytext = 'Welcome to Romania! The weather is nice and all the country is waiting for the Euro Cup!'

para = [ "Lucerne Cottage Cheese, 16 ounces, is on sale for 2 for 5 dollars at the member price." ,
       "Open Nature Almond Beverage, half gallon, or Florida's Natural Orange or Grapefruit Juice, 52 ounces, are available for 2 for 6 dollars at the member price." ,
       "Lucerne Flavored Creamer, 32 ounces, is on sale for 2 for 7 dollars at the member price." ,
       "Clover Organic Milk, half gallon, is priced at 4.99 dollars at the member price." ,
       "Signature SELECT Frozen Fruit, 8 to 16 ounces, is available for 3.99 dollars at the member price." ,
       "Bertolli Pasta Sides, 48 ounces, are priced at 6.99 dollars at the member price." ,
       "Restaurant Style French Fries or Rings, 16 to 28 ounces, are available for 2 for 9 dollars at the member price." ,
       "El Monterey Burritos or Chimichangas Family Pack, 30.4 to 32 ounces, are priced at 4.99 dollars at the member price." ,
       "Rao's Entrée, 8.5 to 9 ounces, is on sale for 4.99 dollars at the member price." ,
       "Totino's Pizza Rolls, 50 count, or Screamin' Sicilian Pizza, 22 to 25 ounces, are priced at 5.99 dollars at the member price."]

language = "en"
def ads_to_mp3(ad_text, folder_path_word_files, speed_low_pitch, variable_speed_flag):
       '''

       :param ad_text: text to transform in mp3. Pre-processing: remove  commas, periods and digits
       :param out_file:
       :param speed_low_pitch:
       :return:
       '''
       processed_text = ad_text.replace(",", " ")
       processed_text = processed_text.replace(".", " ")

       words = processed_text.split()
       pho = Phonemes()
       i=0

       for word in words:

            i += 1
            print("CRT WORD: ", word)

            # reset speed
            speed = 1

            # Variable speed is only for the low pitch words
            if (variable_speed_flag == True):
                speed = 1
                if (pho.is_low_pitched_word(word) == True):
                    speed = speed_low_pitch
            #all words have the same speed
            else:
                speed = speed_low_pitch

            print("Word=", word,  " Speed: ", speed)

            myobj = gTTS(text=word + " ", lang=language, slow=False)

            # Saving the converted audio in a mp3 file
            tmp_file = folder_path_word_files + "word_" + str(word) + ".wav"
            myobj.save(tmp_file)
            output_word_file = folder_path_word_files + str(i) + "wout_" +  str(word) + ".wav"
            out_filters = "atempo=" + str(speed)

            ff = ffmpy.FFmpeg(inputs={tmp_file: None}, outputs={output_word_file: ['-filter:a', out_filters]} )
            ff.run()

def ads_to_wav_at_const_speed(text, out_file, speed):
    '''
    Record a file at a certain uniform speed
    :param text: 
    :param out_file: 
    :param speed: 
    :return: 
    '''
    myobj = gTTS(text + " ", lang=language, slow=False)
    tmp_file = "tmp_file.wav"
    myobj.save(tmp_file)

    ff = ffmpy.FFmpeg(inputs={tmp_file: None}, outputs={out_file: ["-filter:a", "atempo=" + str(speed)]})
    ff.run()


def compile_ad_file(text, folder_path, out_file, speed, variable_speed_flag):
    ads_to_mp3(text, folder_path, speed, variable_speed_flag)
    fc = Ffmpeg_Util()
    fc.compile_files("/Path/To/audio_files2/",out_file)

'''
Try the class - testing only
'''
if __name__ == "__main__":
    folder = "/Path/To/audio_files2/"
    speed = 2
    out_f = "one_ad_constant_2.0.wav"
    single_text = ' '.join(para)

    #Produce a wav file at variable or constant speed
    #Remove files from folder

    compile_ad_file(para[3], folder, out_f, speed, False)


