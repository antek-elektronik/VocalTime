#text to speech in python! 

# import required modules
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
from time import sleep

def getHourPath(hour): 
    if(hour == 1):
        hourPath = "pierwsza"
    elif(hour == 2):
        hourPath = "druga"
    elif(hour == 3):
        hourPath = "trzecia"
    elif(hour == 4):
        hourPath = "czwarta"
    elif(hour == 5):
        hourPath = "piata"
    elif(hour == 6):
        hourPath = "szosta"
    elif(hour == 7):
        hourPath = "siodma"
    elif(hour == 8):
        hourPath = "osma"
    elif(hour == 9):
        hourPath = "dziewiata"
    elif(hour == 10):
        hourPath = "dziesiata"
    elif(hour == 11):
        hourPath = "jedenasta"
    elif(hour == 12):
        hourPath = "dwunasta"
    elif(hour == 13):
        hourPath = "trzynasta"
    elif(hour == 14):
        hourPath = "czternasta"
    elif(hour == 15):
        hourPath = "pietnasta"
    elif(hour == 16):
        hourPath = "szesnasta"
    elif(hour == 17):
        hourPath = "siedemnasta"
    elif(hour == 18):
        hourPath = "osiemnasta"
    elif(hour == 19):
        hourPath = "dziewietnasta"
    elif(hour == 20):
        hourPath = "dwudziesta"
    elif(hour == 21):
        hourPath = "dwudziestapierwsza"
    elif(hour == 22):
        hourPath = "dwudziestadruga"
    elif(hour == 23):
        hourPath = "dwudziestatrzecia"
    elif(hour == 24):
        hourPath = "dwudziestaczwatra"
    elif(hour == 00):
        hourPath = "polnoc"

    return f"resources/{hourPath}.wav"

def getUnitsPath(number):
    number = int(number)
    numberPath = ""
    if(number == 1):
        numberPath = "jeden"
    elif(number == 2):
        numberPath = "dwa"
    elif(number == 3):
        numberPath = "trzy"
    elif(number == 4):
        numberPath = "cztery"
    elif(number == 5):
        numberPath = "piec"
    elif(number == 6):
        numberPath = "szesc"
    elif(number == 7):
        numberPath = "siedem"
    elif(number == 8):
        numberPath = "osiem"
    elif(number == 9):
        numberPath = "dziewiec"
    elif(number == 10):
        numberPath = "dziesiec"
    elif(number == 11):
        numberPath = "jedenascie"
    elif(number == 12):
        numberPath = "dwanascie"
    elif(number == 13):
        numberPath = "trzynascie"
    elif(number == 14):
        numberPath = "czternascie"
    elif(number == 15):
        numberPath = "pietnascie"
    elif(number == 16):
        numberPath = "szesnascie"
    elif(number == 17):
        numberPath = "siedemnascie"
    elif(number == 18):
        numberPath = "osiemnascie"
    elif(number == 19):
        numberPath = "dziewietnascie"

    return f"resources/{numberPath}.wav"

def getTensPath(number):
    number = int(number)
    path = ""
    if(number == 2):
        path = "dwadziescia"
    elif(number == 3):
        path = "trzydziesci"
    elif(number == 4):
        path = "czterdziesci"
    elif(number == 5):
        path = "piecdziesiat"

    return f"resources/{path}.wav"
    


def getMinuteSound(minute):
    if(int(minute) < 20):
        return AudioSegment.from_wav(getUnitsPath(minute))
    elif(int(minute) >= 20):
        minute = str(minute)
        result = AudioSegment.from_wav(getTensPath(minute[0:1]))
        if(minute[1:2] != "0"):
            segment2 = AudioSegment.from_wav(getUnitsPath(minute[1:2]))
            result = result + segment2
        return result


print('playing sound using  pydub')


while True:
    now = datetime.now()

    startSound = AudioSegment.from_wav("resources/jestgodzina.wav")
    hourSound = AudioSegment.from_wav(getHourPath(now.hour))
    audio = startSound + hourSound

    minute = now.minute
    if(minute != 0):
        minuteSound = getMinuteSound(minute)
        audio = audio + minuteSound
    play(audio)
    sleep(60)