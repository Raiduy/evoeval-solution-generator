from typing import List, Tuple

def account_balance(operations: List[Tuple[str, int]], daily_limit: int) -> str:
    balance = 0
    daily_withdrawal = 0
    for (operation, amount) in operations:
        if operation == 'deposit':
            balance += amount
        elif operation == 'withdrawal':
            if amount > daily_limit:
                return 'Daily limit exceeded'
            if daily_withdrawal + amount > daily_limit:
                return 'Daily limit exceeded'
            daily_withdrawal += amount
            balance -= amount
        if balance < 0:
            return 'Balance below zero'
    return 'All operations successful'