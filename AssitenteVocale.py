import speech_recognition as sr
import os
import pyttsx3
engine = pyttsx3.init()
recognizer_instance = sr.Recognizer()


nome_assistente = input("scegli il nome dell'assitente ")

def assistente():
    while True:
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            audio = recognizer_instance.listen(source)

        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            print(f'[+] testo: {text}')
            if text.lower().startswith(nome_assistente):
                testo = text.lower().replace(f'{nome_assistente} ', '')
                print(f'[+] testo pulito: {testo}')
                if testo.lower() == 'ciao' or testo.lower() == 'buongiorno':
                    engine.say('buongiorno')
                    print('buongiorno')
                    engine.runAndWait()
                elif testo.lower().startswith('apri'):
                    da_aprire = testo.lower().replace('apri ', '')
                    try:
                        os.system(f'start {da_aprire}')
                    except Exception as e:
                        engine.say(f'impossibile trovare il programma')
                        engine.runAndWait
                elif testo.lower() == 'esci' or testo.lower() == 'chiudi':
                    exit()
        except Exception as e:
            print(e)

assistente()