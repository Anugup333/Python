from atm_exception import DepositError,WithdrawError,InSufficientFundError
bal = 500
def withdraw():
    global bal
    with_bal = float(input("Enter the Withdraw Balance: "))
    if with_bal <=0:
        raise WithdrawError
    elif (with_bal +500) > bal:
        raise InSufficientFundError
    else:
        bal -= with_bal
        print("="*50)
        print(f"\t Successfully Withdraw the Balance : {with_bal}",)
        print("="*50)
        print(f"\t Now Updated Balance : {bal}")
        
def deposit():
    dep_bal = float(input("Enter the Deposit Balance: "))
    if dep_bal <=0:
        raise DepositError
    else:
        global bal
        bal += dep_bal
        print("="*50)
        print(f"\t Successfully Withdraw the Balance : {dep_bal}",)
        print("="*50)
        print(f"\t Now Updated Balance : {bal}")

def balance():
    print("="*50)
    print(f"\t Balance : {bal}")
        