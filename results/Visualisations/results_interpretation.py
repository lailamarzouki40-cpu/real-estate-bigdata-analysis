import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_city(zip_code):
    """Maps Zip Code prefix to City name."""
    z = str(zip_code)
    if z.startswith('727'): return "Siloam Springs"
    if z.startswith('606'): return "Chicago"
    if z.startswith('752'): return "Dallas"
    if z.startswith('770'): return "Houston"
    if z.startswith('850') or z.startswith('853'): return "Phoenix"
    if z.startswith('331'): return "Miami"
    if z.startswith('1'): return "New York Area"
    return "Other"

def run_visualization():
    # 1. Load your Hadoop Results
    results_path = 'results/affordability_results.txt'
    if not os.path.exists(results_path):
        print(f"Error: {results_path} not found.")
        return

    df = pd.read_csv(results_path, sep='\t', names=['ZipCode', 'PricePerBed'])
    
    # 2. Process Data
    df['City'] = df['ZipCode'].apply(get_city)
    # Create a Label: "Houston (77019)"
    df['Label'] = df['City'] + " (" + df['ZipCode'].astype(str) + ")"

    # Set the style
    sns.set_theme(style="whitegrid")

    # --- PLOT 1: TOP 10 MOST EXPENSIVE NEIGHBORHOODS ---
    # This chart proves the "Outliers" and "City Overlap"
    plt.figure(figsize=(14, 7))
    top_10 = df.sort_values(by='PricePerBed', ascending=False).head(10)
    
    sns.barplot(x='Label', y='PricePerBed', data=top_10, hue='City', palette='flare', dodge=False)
    
    plt.title('Top 10 Most Expensive Neighborhoods (Price per Bedroom)', fontsize=16)
    plt.ylabel('Average Price per Bed ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('results/top_expensive_neighborhoods.png')
    print("Saved: results/top_expensive_neighborhoods.png")

    # --- PLOT 2: HOUSTON VARIANCE (THE "REPEATED" EXPLAINER) ---
    # This chart specifically shows why Houston appeared multiple times
    plt.figure(figsize=(12, 6))
    houston_df = df[df['City'] == 'Houston'].sort_values(by='PricePerBed', ascending=False).head(10)
    
    sns.barplot(x='ZipCode', y='PricePerBed', data=houston_df, color='teal')
    
    plt.title('Houston Neighborhood Comparison: Drastic Variance within One City', fontsize=16)
    plt.ylabel('Avg Price per Bed ($)')
    plt.xlabel('Houston Zip Codes')
    plt.tight_layout()
    plt.savefig('results/houston_variance_breakdown.png')
    print("Saved: results/houston_variance_breakdown.png")

if __name__ == "__main__":
    run_visualization()