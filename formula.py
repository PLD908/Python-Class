import re

class FormulaError(Exception):
    #Exception raised for errors in the chemical formula.
    pass

def parse_formula(formula, periodic_table):
    """
    Parses a chemical formula into a list of [symbol, quantity] lists.

    Parameters:
        formula (str): The chemical formula to parse.
        periodic_table (dict): The periodic table dictionary for validation.

    Returns:
        list: A list of [symbol, quantity] lists.
    """
    # Regular expression to match elements and their quantities
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    
    symbol_quantity_list = []
    
    for (symbol, qty) in matches:
        if symbol not in periodic_table:
            raise FormulaError(f"Unknown element symbol: {symbol}")
        quantity = int(qty) if qty else 1
        symbol_quantity_list.append([symbol, quantity])
    
    return symbol_quantity_list
