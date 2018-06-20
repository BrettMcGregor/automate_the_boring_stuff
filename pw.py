#! python3
# 20/6/18 cannot get this to work from command line: ModuleNotFoundError: No module named 'pyperclip'
# password manager program
import sys
import pyperclip


passwords = {"email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
             "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
             "luggage": "12345"}


if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # first command line argument is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account named {account}")
