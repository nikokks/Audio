from scipy.io import wavfile
import scipy.signal as sps
import argparse
import audioop
import wave
import os


INPUT_PATH_FILES = 'data_pipeline/8000_1/'
OUTPUT_PATH_FILES = 'data_pipeline/16000_1/'
folders = os.listdir(INPUT_PATH_FILES)

for folder in folders:
    if not os.path.isdir('data_pipeline/16000_1/'+folder):
        os.mkdir('data_pipeline/16000_1/'+folder+"/")
    files = elements = os.listdir(INPUT_PATH_FILES+folder)
    for file in files:
        os.system("ffmpeg -i " + INPUT_PATH_FILES + folder + "/" + file +
                  " -ar 8000 -ac 1 -acodec pcm_s16le -y " +
                  INPUT_PATH_FILES + 'temp_' + file)
        os.system("mv " + INPUT_PATH_FILES + 'temp_' + file + ' ' +
                  INPUT_PATH_FILES + folder + "/" + file)
    for file in files:
        print(file)
        audioFile = wave.open(INPUT_PATH_FILES+folder+"/"+file, 'r')
        n_frames = audioFile.getnframes()
        audioData = audioFile.readframes(n_frames)
        originalRate = audioFile.getframerate()
        af = wave.open(OUTPUT_PATH_FILES+folder+'/'+file, 'w')
        af.setnchannels(1)
        af.setparams((1, 2, 16000, 0, 'NONE', 'Uncompressed'))
        converted = audioop.ratecv(audioData, 2, 1, originalRate, 16000,
                                   None)
    af.writeframes(converted[0])
    af.close()
    audioFile.close()

"""
INPUT_PATH_FILES = 'data_pipeline/16000_1/'
OUTPUT_PATH_FILES = 'data_pipeline/8000_1/'
folders = os.listdir(INPUT_PATH_FILES)

for folder in folders:
    if not os.path.isdir('data_pipeline/8000_1/'+folder):
        os.mkdir('data_pipeline/8000_1/'+folder+"/")
    files = elements = os.listdir(INPUT_PATH_FILES+folder)
    for file in files:
        os.system("ffmpeg -i " + INPUT_PATH_FILES + folder + "/" + file +
                  " -ar 16000 -ac 1 -acodec pcm_s16le -y " +
                  INPUT_PATH_FILES + 'temp_' + file)
        os.system("mv " + INPUT_PATH_FILES + 'temp_' + file + ' ' +
                  INPUT_PATH_FILES + folder + "/" + file)
    for file in files:
        print(file)
        audioFile = wave.open(INPUT_PATH_FILES+folder+"/"+file, 'r')
        n_frames = audioFile.getnframes()
        audioData = audioFile.readframes(n_frames)
        originalRate = audioFile.getframerate()
        af = wave.open(OUTPUT_PATH_FILES+folder+'/'+file, 'w')
        af.setnchannels(1)
        af.setparams((1, 2, 8000, 0, 'NONE', 'Uncompressed'))
        converted = audioop.ratecv(audioData, 2, 1, originalRate, 8000,
                                   None)
    af.writeframes(converted[0])
    af.close()
    audioFile.close()
"""
