import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_city(zip_code):
    z = str(zip_code)
    if z.startswith('727'): return "Siloam Springs"
    if z.startswith('606'): return "Chicago"
    if z.startswith('752'): return "Dallas"
    if z.startswith('770'): return "Houston"
    if z.startswith('850') or z.startswith('853'): return "Phoenix"
    if z.startswith('331'): return "Miami"
    if z.startswith('1'): return "New York Area"
    return "Other"

def run_value_visualization():
    # 1. Load your Hadoop Value Results
    results_path = 'results/value_results.txt'
    if not os.path.exists(results_path):
        print("Error: value_results.txt not found in results/ folder.")
        return

    df = pd.read_csv(results_path, sep='\t', names=['ZipCode', 'PricePerSqFt'])
    
    # 2. Map Cities and Create Labels
    df['City'] = df['ZipCode'].apply(get_city)
    df['Label'] = df['City'] + " (" + df['ZipCode'].astype(str) + ")"

    # 3. Set visual style
    sns.set_theme(style="whitegrid")

    # --- PLOT: TOP 10 HIGHEST $/SQFT ---
    plt.figure(figsize=(14, 8))
    # Sort by value to find the most "expensive" space
    top_10_value = df.sort_values(by='PricePerSqFt', ascending=False).head(10)
    
    sns.barplot(x='Label', y='PricePerSqFt', data=top_10_value, hue='City', palette='mako', dodge=False)
    
    plt.title('Investment Value Analysis: Top 10 Highest Price per Square Foot', fontsize=16)
    plt.ylabel('Price per Square Foot ($)')
    plt.xlabel('Market Area (City & Zip)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('results/top_value_sqft_cities.png')
    print("Success: results/top_value_sqft_cities.png generated.")

if __name__ == "__main__":
    run_value_visualization()