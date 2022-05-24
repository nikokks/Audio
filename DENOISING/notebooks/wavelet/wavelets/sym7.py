""" Symlet 7 wavelet """


class Symlet7:
    """
    Properties
    ----------
     near symmetric, orthogonal, biorthogonal

    All values are from http://wavelets.pybytes.com/wavelet/sym7/
    """
    __name__ = "Symlet Wavelet 7"
    __motherWaveletLength__ = 14  # length of the mother wavelet
    __transformWaveletLength__ = 2  # minimum wavelength of input signal

    # decomposition filter
    # low-pass
    decompositionLowFilter = [
        0.002681814568257878,
        -0.0010473848886829163,
        -0.01263630340325193,
        0.03051551316596357,
        0.0678926935013727,
        -0.049552834937127255,
        0.017441255086855827,
        0.5361019170917628,
        0.767764317003164,
        0.2886296317515146,
        -0.14004724044296152,
        -0.10780823770381774,
        0.004010244871533663,
        0.010268176708511255,
    ]

    # high-pass
    decompositionHighFilter = [
        -0.010268176708511255,
        0.004010244871533663,
        0.10780823770381774,
        -0.14004724044296152,
        -0.2886296317515146,
        0.767764317003164,
        -0.5361019170917628,
        0.017441255086855827,
        0.049552834937127255,
        0.0678926935013727,
        -0.03051551316596357,
        -0.01263630340325193,
        0.0010473848886829163,
        0.002681814568257878,
    ]

    # reconstruction filters
    # low pass
    reconstructionLowFilter = [
        0.010268176708511255,
        0.004010244871533663,
        -0.10780823770381774,
        -0.14004724044296152,
        0.2886296317515146,
        0.767764317003164,
        0.5361019170917628,
        0.017441255086855827,
        -0.049552834937127255,
        0.0678926935013727,
        0.03051551316596357,
        -0.01263630340325193,
        -0.0010473848886829163,
        0.002681814568257878,
    ]

    # high-pass
    reconstructionHighFilter = [
        0.002681814568257878,
        0.0010473848886829163,
        -0.01263630340325193,
        -0.03051551316596357,
        0.0678926935013727,
        0.049552834937127255,
        0.017441255086855827,
        -0.5361019170917628,
        0.767764317003164,
        -0.2886296317515146,
        -0.14004724044296152,
        0.10780823770381774,
        0.004010244871533663,
        -0.010268176708511255,
    ]
