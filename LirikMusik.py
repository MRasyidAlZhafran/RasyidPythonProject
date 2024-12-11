import sys
import time
def lirik():
    lirik = [
        ("Secret I have held in my heart", 0.1),
        ("Are Harder To Hide Than I Thought", 0.1),
        ("Maybe I Just Wanna Be Yours", 0.1),
        ("I Wanna Be Yours", 0.1),
        ("I Wanna Be Yours", 0.1),
        ("Wanna Be Yours", 0.1),
        ("Wanna Be Yours", 0.1),
        ("Wanna Be Yours", 0.1),
    ]

    delay = [0.4, 0.4, 0.5, 0.5, 1.8, 2.1, 2.2, 2]
    print("\n+=Wanna Be Yours=+")
    time.sleep(2)
    for i, (barisan_lagu, delay_kata) in enumerate(lirik):
        for b in barisan_lagu:
            print(b, end = "")
            sys.stdout.flush()
            time.sleep(delay_kata)
        time.sleep(delay[i])
        print("")

lirik()