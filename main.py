import requests

print('WebMan Mod Python Commands By Boxuga')
PS3IP = input('Please enter PS3 IP Address? ')
try:
    PS3TEST = requests.get('http://' + PS3IP)
except requests.ConnectionError:
    print('Connection Failed: PlayStation may be off or not connected')

Options = input('Please select an option? \n 1 - Display System Stats Notification \n 2 - Display a Custom Notification \n 3 - Download File to PS3 \n 4 - Eject Disc \n 5 - Play Game \n 6 - Play Sound \n 7 - Open URL in PS3 Browser \n')

if Options == '1':
    requests.get("http://" + PS3IP + "/popup.ps3")
elif Options == '2':
    CustomNotification = input('What do you want to be displayed in the notification? ')
    requests.get("http://" + PS3IP + "/popup.ps3/" + CustomNotification)
elif Options == '3':
    askforURL = input('What is the URL you would like to grab the file from? ')
    askforFileLocation = input('What directory do you want this file if unsure type (/dev_hdd0/tmp)? ')
    requests.get("http://" + PS3IP + "/download.ps3?to=" + askforFileLocation + "&url=" + askforURL)
elif Options == '4':
    requests.get("http://" + PS3IP + "/eject.ps3")
elif Options == '5':
    requests.get('http://' + PS3IP + '/play.ps3')
elif Options == '6':
    SndSelection = input('What sound do you want to be played \n 0 - Cancel \n 1 - Beep \n 2 - Two Beeps \n 3 - Three Beeps \n 4 - Cursor \n 5 - Trophy Unlocked \n 6 - Decide \n 7 - Option \n 8 - OK \n 9 - system_ng')
    requests.get("http://" + PS3IP + '/buzzer.ps3mapi?snd=' + SndSelection)
elif Options == '7':
    openurlps3 = input('Please paste a URL? ')
    requests.get("http://" + PS3IP + "/browser.ps3?" + openurlps3)
print('Sent Request.')
exit()
