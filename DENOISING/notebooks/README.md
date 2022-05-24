# DENOISED AGLOS TESTS

## folder infos
### data folder
contains: noisy audios, clean audios and denoised audios processed once with each algos
### data_pipeline
contains: noisy audios, clean audios denoised audios processed once with each algos and denoised audios from combination of 2 different algos (pipeline) 
### DTLN folder
contains the entire codes and models saved by the DTLN algorithm
### MODELS_SAVED folder
contains the pickle models saved of various desnoing algos
### sudo_rm_rf folder 
contains the entire code and models saved from sudo_rm_rf desnoising models
### wavelet folder
contains the entire code of the wavelet denoising algo

## files infos
### converter_sample_rate.py 
- python script wich allows to convert WAV audios in a folder from 8000Hz to 16000Hz sample rate and from 16000Hz to 8000 Hz sample rate
- to run it modify INPUT_PATH_FILES where wav audios to process are and where OUTPUT_PATH_FILES is the output of wav files converted
- just tested on WAV files
- to convert from 8000Hz to 16000Hz just use the first part of the code
- to convert from 16000Hz to 8000Hz use the code commented in the script
### Converter_sample_rate.ipynb notebook
- python notebook which convert WAV audios in a folder from a certain sample rate to another
- actual code is prepared to convert from 48000Hz sample rate WAV files to 16000Hz
- audio files must be in WAV format
### ConvTasNet_Libri1Mix_8k_and_16k.ipynb notebook
- python notebook allowing to denoise audio wav file with ConvTasNet_Libri1Mix_enhsingle_1 algo
- be carefull with the input sample rate files ! if 16kHz is the sample rate input audio use the convtasnet designed for 16kHz audio files. Else if 8KHz input WAV audio select the 8kHz model
- the audio files input must be in WAV format at 16kHz sample rate or WAV 8KHz
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 8KHz sample rate format or 16KHz: use converter_sample_rate.py
- the model can be loaded from pickle model file format for both 16KHZ and 8KHz models (offline)
### ConvTasNet_Libri2Mix_16k.ipynb notebook
- python notebook allowing to denoise audio WAV file with ConvTasNet_Libri2Mix_16k algo
- be carefull with the input sample rate files ! 
- the audio files input must be in WAV format at 16kHz sample rate
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 16KHz sample rate format: use converter_sample_rate.py
- the model can be loaded from pickle file (offline)
- model just available in 16KHz sample rate wav audio file input
### DPRNNTasNet_LibriMix_16k.ipynb notebook
- python notebook allowing to denoise audio wav file with DPRNNTasNet_LibriMix_16k algo
- be carefull with the input sample rate files !
- the audio files input must be in WAV format at 16kHz sample rate
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 16KHz sample rate format: use converter_sample_rate.py
- the model can be loaded from pickle file (offline)
### DPTNet_libri1Mix_16k.ipynb notebook
- python notebook allowing to denoise audio wav file with DPTNet_libri1Mix_16k algo
- be carefull with the input sample rate files ! 
- the audio files input must be in WAV format at 16kHz sample rate
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 16KHz sample rate format: use converter_sample_rate.py
- the model can be loaded from the pickle file
### DTLN_16k_WHAM_WHAMR.ipynb notebook
- python notebook allowing to denoise audio wav file with DTLN_16k_WHAM_WHAMR algo
- be carefull with the input sample rate files !
- the audio files input must be in WAV format at 16kHz sample rate.
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 16KHz sample rate format: use converter_sample_rate.py
- 3 variant models of DTLN can be used and are presented in the differents cells
- the code is done in manner to call script with certain args
- it converts multiple wav audio files from an input folder containing them
### SUDO_RM_RF_8k.ipynb notebook
- do not forget to download the models by running bash script download_pretrained_models.sh in Audio/DENOISING/notebooks/sudo_rm_rf/pretrained_models/ and put the save file models at the root of the script download_pretrained_models.sh 
- before run the notebook, you'll have to clone the repo https://github.com/etzinis/sudo_rm_rf at the root of this notebook
- python notebook allowing to denoise 8KHz audio wav file with SUDO_RM_RF_8k algos
- be carefull with the input sample rate files !
- the audio files input must be in WAV format at 8kHz sample rate
- if the audio files are note in WAV format: convert them to WAV format
- if the WAV audio file is not in 8KHz sample rate format: use converter_sample_rate.py
- 4 variant models of SUDO_RM_RF can be used and are presented
- it converts multiple wav audio files from an input folder containing them

### Test_performances.ipynb notebook
- python notebook to test the different denoising performances of the different algos
- the metrics to test performances are STOI and SI-SNR wihch are Short-Time Objective Intelligibility (STOI) and Scale-Invariant Signal-to-Noise Ratio (SI-SNR)
- the use of these metrics are not optimized for large dataset
- to run faster the time compute of metrics use thse torch functions (on GPU):
https://torchmetrics.readthedocs.io/en/latest/audio/short_time_objective_intelligibility.html
https://torchmetrics.readthedocs.io/en/latest/audio/scale_invariant_signal_noise_ratio.html




## RESULTS

### DPTNet
- fast to compute
- good fit in RAM
- desnoied results seems to be good

### DPRNNTasNet
- very slow
- not optimized for fit in RAM
- the denoised audio seems to be good but the performances seems worst than DPTNet

### DTLN
- VERY FAST !
- good fit in RAM
- the denoised performances of this algo seem to be good


### SUDO RM RF
- fast
- good fit in RAM
- desnoied results seems to be quite good but not as DPTNet or DTLN desnoised algos


## FINAL RESULTS

- see in Test_performances.ipynb notebook
- the use of DPTNet at first time then the use of DTLNet give the best results on this small dataset
- the dataset of test is very small so the performances shown for the different desnoising models on this dataset are not absolute. 
It would be better to test these models on a more confident dataset and on the specific data in question
