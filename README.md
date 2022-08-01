# PasswordVulnerabilities

This repository contains my main presentation, side project and code for the pyperclip attack (one of 3 attacks I preformed on the password managers).

---------------------------------------------------------------------------------------------------------------------------------------------------------

PYPERCLIP ATTACK 

Goal: utilize the password manager’s clipboard feature to email the attacker any passwords that have been copied/pasted.  

Steps: 

1. Configure attacker’s Gmail: security --> signing into google –> app passwords (2 factor authentication must already be set up for this to work!).  

2. Create a new app password labeled “python” and save the password it generates.   

3. Download helper.py and pyperclipAttack.py on to victim’s computer

4. In helper.py, set the variable “password” as whatever password step 2 generated.  

5. Replace the email sender and receiver in helper.py  

6. Install pyperclip with python3 –m pip install pyperclip    

7. Run the script in the terminal with python3 pyperclipAttack.py & (the & symbol makes the attack harder to detect on the victim’s side) 

 

Note: this code is not mine. Most of the code came from this website: https://medium.com/@jubin3424/clipboard-hijacking-attack-and-vulnerability-to-this-in-current-financial-services-2175e1ac6105    

The main difference is I’ve changed parts of the code to work with Gmail’s 2022 security update. There are still a couple bugs, but for the most part it works. 
