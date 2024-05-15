from pyo3_bond_pricing import SimpleBond

bond1 = SimpleBond(1000, 0.04, 2, 10, 0.04584, 0)
bond2 = SimpleBond(1000, 0.04, 2, 10, 0, 953.57)
print(f"bond price is {round(bond1.solve_price(), 2)} USD")
print(
    f"bond yield is {round(bond2.solve_yield_to_maturity(0.01, 1000, 0.00001, 0.00000001), 4)}"
)
