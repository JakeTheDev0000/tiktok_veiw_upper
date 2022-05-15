import webbrowser
import time, os

def main():
    how_many_times = int(input("how many times do you want the program to watch the video\n(the higher it is the more ram and CPU power it will take)\n>>>"))
    link = str(input("enter the link to the video\n>>>"))

    for i in range(how_many_times):
        webbrowser.open(link)
    pass
    time.sleep(how_many_times / 0.3)
    os.system("taskkill /F /IM chrome.exe /T > nul")
    os.system("Taskkill /F /IM msedge.exe /T > nul")


if __name__ == "__main__":
    main()