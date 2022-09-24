# __MODULES__
import time
import multiprocessing
import keyboard


def spammer(spamTxt):
    keyboard.write(spamTxt)
    keyboard.press_and_release("enter")


# __MAIN__
if __name__ == '__main__':
    counter = int(input("[!] How many texts to send >>> "))
    text = input("[!] Enter the text to spam >>> ")
    time.sleep(2)
    jobs = []

    start = time.time()
    for spam in range(counter):
        p = multiprocessing.Process(target=spammer, args=(text, ))
        p.start()
        jobs.append(p)

        for proc in jobs:
            proc.join()

    print(f"\n[+] {counter} texts were sent successfully!\n"
          f"[!] It took {time.time()-start} seconds")
