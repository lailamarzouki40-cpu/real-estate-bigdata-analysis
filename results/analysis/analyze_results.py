import pandas as pd
import os

# Create results folder if it doesn't exist
if not os.path.exists('results'):
    os.makedirs('results')

def manual_interpretation():
    # 1. Load the Hadoop Results
    # Note: Using sep='\t' because Hadoop outputs are Tab-Separated
    try:
        afford_df = pd.read_csv('results/affordability_results.txt', sep='\t', names=['ZipCode', 'PricePerBed'])
        value_df = pd.read_csv('results/value_results.txt', sep='\t', names=['ZipCode', 'PricePerSqFt'])
    except FileNotFoundError:
        print("Error: Could not find result files in the results/ folder.")
        return

    # 2. Merge them so we can compare $/Bed and $/SqFt for the same Zip Code
    master_analysis = pd.merge(afford_df, value_df, on='ZipCode')

    print("\n" + "="*50)
    print("      REAL ESTATE BIG DATA MARKET REPORT")
    print("="*50)

    # 3. Find Luxury Markets (Highest Price per SqFt)
    luxury = master_analysis.sort_values(by='PricePerSqFt', ascending=False).head(5)
    print("\n[ TOP 5 LUXURY / HIGH-VALUE ZIP CODES ]")
    print("These areas have the highest cost per square foot (Investors pay more here).")
    print(luxury[['ZipCode', 'PricePerSqFt']].to_string(index=False))

    # 4. Find Family Bargains (Lowest Price per Bedroom)
    bargains = master_analysis.sort_values(by='PricePerBed', ascending=True).head(5)
    print("\n[ TOP 5 FAMILY BARGAIN ZIP CODES ]")
    print("These areas are the most affordable to add bedrooms (Best for families).")
    print(bargains[['ZipCode', 'PricePerBed']].to_string(index=False))

    # 5. Find "Hidden Gems" (Low Price per SqFt but Good Quality)
    # We look for the bottom 10% of PricePerSqFt
    gems = master_analysis.sort_values(by='PricePerSqFt', ascending=True).head(5)
    print("\n[ TOP 5 UNDERVALUED / RURAL ZIP CODES ]")
    print("These areas give you the most physical house for your dollar.")
    print(gems[['ZipCode', 'PricePerSqFt']].to_string(index=False))
    
    print("\n" + "="*50)

if __name__ == "__main__":
    manual_interpretation()