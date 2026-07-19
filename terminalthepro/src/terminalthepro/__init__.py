import time
import subprocess
def modeNL():
    terma = input("Terminal: ")
    subprocess.run(f"{terma}", shell=True)
def modeL():
    terma = input("Terminal: ")
    print("reading code...")
    time.sleep(6)
    print("Done!")
    subprocess.run(f"{terma}", shell=True)
def test():
    print("done code 0")
