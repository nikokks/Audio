import os
import soundfile
from wavelet import *
INPUT_PATH_FILES = "data_pipeline/8000/"
OUTPUT_FILE = "data_pipeline/8000_1/wavelet/"
WAVELET_NAME = "coif1"  # coif1 works vey well
FILES = os.listdir(INPUT_PATH_FILES)

for FILE in FILES:
    INPUT_FILE = INPUT_PATH_FILES + FILE
    info = soundfile.info(INPUT_FILE)  # getting info of the audio
    rate = info.samplerate
    t = FastWaveletTransform(WAVELET_NAME)
    c = VisuShrinkCompressor()
    with soundfile.SoundFile(OUTPUT_FILE + FILE, "w",
                             samplerate=rate, channels=1) as of:
        for block in soundfile.blocks(INPUT_FILE,
                                      int(rate * info.duration * 0.1)):
            if block.ndim > 1:
                block = block.sum(axis=1) / 2

            coefficients = t.wavedec(block)
            coefficients = c.compress(coefficients)
            clean = t.waverec(coefficients)

            clean = np.asarray(clean, dtype=np.float_)
            of.write(clean)
