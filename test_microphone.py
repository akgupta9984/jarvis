import speech_recognition as sr

def test_microphone():
    try:
        with sr.Microphone() as source:
            print("Microphone is working.")
    except Exception as e:
        print("Microphone is not accessible:", e)

if __name__ == "__main__":
    test_microphone()
    