def calculate_progressive_tax(income: float, deductions=0) -> float:
    taxable_income = income - deductions
    tax = 0
    if taxable_income > 130000:
        tax += (taxable_income - 130000) * 0.3
        taxable_income = 130000
    if taxable_income > 60000:
        tax += (taxable_income - 60000) * 0.25
        taxable_income = 60000
    if taxable_income > 10000:
        tax += (taxable_income - 10000) * 0.15
    return tax