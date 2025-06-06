from atm_menu import atmmenu
import sys
from atm_exception import WithdrawError,DepositError,InSufficientFundError
from atm_operations import deposit,withdraw,balance

def sbi():
    atmmenu()
    while True:
        try:
            print("="*50)
            ch = int(input("Enter the Choice : "))
            match(ch):
                case 1:
                    try:
                        deposit()
                    except DepositError:
                        print("="*50)
                        print("\t Don't Enter the Deposit Value less than equal to zero")
                    except ValueError:
                        print("="*50)
                        print("\t Don't Enter the str / Special Symbol: ")
                case 2:
                    try:
                        withdraw()
                    except DepositError:
                        print("="*50)
                        print("\t Don't Enter the Withdraw Balance less than equal to zero")
                    except InSufficientFundError:
                        print("="*50)
                        print("\t Can't Withdraw the Balance Greater than Sufficient Balance")
                    except ValueError:
                        print("="*50)
                        print("\t Don't Enter the str / Special Symbol: ")
                case 3:
                    balance()
                case 4:
                    print("\t Thank you for Using This Atm App ")
                    sys.exit()
                case _:
                    print("="*50)
                    print("\t Enter the Correct Choice: ")
        except ValueError:
            print("="*50)
            print("\t Don't Enter the str / Special Symbol: ")