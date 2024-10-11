from collections import defaultdict
def minimize_cash_flow(transactions):
    net_balance = defaultdict(int)
    for debtor, creditor, amount in transactions:
        net_balance[debtor] -= amount
        net_balance[creditor] += amount

    creditors = []
    debtors = []

    for person, balance in net_balance.items():
        if balance > 0:
            creditors.append((person, balance))
            debtors.append((person, -balance))
    result = []
    while creditors and debtors:
        creditor, credit_amount = creditors[0]
        debtor, debt_amount = debtors[0]
        settled_amount = min(credit_amount, debt_amount)
        result.append((debtor, creditor, settled_amount))
        creditors[0] = (creditor, credit_amount - settled_amount)
        debtors[0] = (debtor, debt_amount - settled_amount)
        if creditors[0][1] == 0:
            creditors.pop(0)
        if debtors[0][1] == 0:
            debtors.pop(0)

    return result
transactions = [
    ('A', 'B', 50),
    ('B', 'C', 30),
    ('C', 'A', 20),
    ('A', 'C', 10)
]

minimized_transactions = minimize_cash_flow(transactions)
for debtor, creditor, amount in minimized_transactions:
    print(f"{debtor} pays {creditor} ${amount}")
