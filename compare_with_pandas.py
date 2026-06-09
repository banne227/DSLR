import pandas as pd
import sys


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python compare_with_pandas.py <csv_file>")
		sys.exit(1)
	
	file = sys.argv[1]
	
	# Charger les données avec pandas
	df = pd.read_csv(file)
	
	# Afficher describe() - cela montre Count, Mean, Std, Min, 25%, 50%, 75%, Max
	print("=== Pandas describe() ===")
	print(df.describe())
	print("\n") 
	
	## Optionnel : afficher aussi le type de chaque colonne
	#print("=== Types de données ===")
	#print(df.dtypes)
