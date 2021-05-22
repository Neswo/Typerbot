import requests, os, time

print(".-') _                 _ (`-.    ('-.  _  .-') .-. .-')                .-') _    \n(  OO) )               ( (OO  ) _(  OO)( \( -O )\  ( OO )              (  OO) )   \n/     '._  ,--.   ,--._.`     \(,------.,------. ;-----.\  .-'),-----. /     '._  \n|'--...__)  \  `.'  /(__...--'' |  .---'|   /`. '| .-.  | ( OO'  .-.  '|'--...__) \n'--.  .--'.-')     /  |  /  | | |  |    |  /  | || '-' /_)/   |  | |  |'--.  .--' \n   |  |  (OO  \   /   |  |_.' |(|  '--. |  |_.' || .-. `. \_) |  |\|  |   |  |    \n   |  |   |   /  /\_  |  .___.' |  .--' |  .  '.'| |  \  |  \ |  | |  |   |  |    \n   |  |   `-./  /.__) |  |      |  `---.|  |\  \ | '--'  /   `'  '-'  '   |  |    \n   `--'     `--'      `--'      `------'`--' '--'`------'      `-----'    `--'  ")
print(" #-----------------------------------------------------------------------------#")
url1 = input("(?) Id of the channel you want to annoy: ")
token = input("(?) Your token: ")
url = str('https://discord.com/api/v9/channels/'+url1+'/typing')

headers = {
    'authorization': token,
}

requestnbr = 1

while True:
    os.system("cls")
    print(".-') _                 _ (`-.    ('-.  _  .-') .-. .-')                .-') _    \n(  OO) )               ( (OO  ) _(  OO)( \( -O )\  ( OO )              (  OO) )   \n/     '._  ,--.   ,--._.`     \(,------.,------. ;-----.\  .-'),-----. /     '._  \n|'--...__)  \  `.'  /(__...--'' |  .---'|   /`. '| .-.  | ( OO'  .-.  '|'--...__) \n'--.  .--'.-')     /  |  /  | | |  |    |  /  | || '-' /_)/   |  | |  |'--.  .--' \n   |  |  (OO  \   /   |  |_.' |(|  '--. |  |_.' || .-. `. \_) |  |\|  |   |  |    \n   |  |   |   /  /\_  |  .___.' |  .--' |  .  '.'| |  \  |  \ |  | |  |   |  |    \n   |  |   `-./  /.__) |  |      |  `---.|  |\  \ | '--'  /   `'  '-'  '   |  |    \n   `--'     `--'      `--'      `------'`--' '--'`------'      `-----'    `--'  ")
    print(" #-----------------------------------------------------------------------------#")
    
    print("(>) Sending request to: "+url)

    response = requests.post(url, headers=headers)

    print("(#) Response: "+str(response))

    if str(response) == "<Response [204]>":
        print("(>) The request number "+str(requestnbr)+" has been successfully sent")
    else:
        print("/!\ The request number "+str(requestnbr)+" has been declined for some reason (are you sure that you entered the right token or channel id ?")

    requestnbr += 1
    time.sleep(8)