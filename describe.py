import csv
import sys
from collections import defaultdict

def percentile(data, p):
	"""Calcule le percentile p d'une liste triée"""
	sorted_data = sorted(data)
	idx = (p / 100) * (len(sorted_data) - 1)
	lower = int(idx)
	upper = lower + 1
	if upper >= len(sorted_data):
		return sorted_data[lower]
	weight = idx - lower
	return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight


def describe(file):
	data = defaultdict(list)
	
	with open(file, "r") as f:
		reader = csv.DictReader(f)
		colones_utiles = reader.fieldnames[6:]
		for row in reader:
			for colonne in colones_utiles:
				valeur = row[colonne]
				if valeur != "":  # ignorer les vides
					try:
						val = float(valeur)
						data[colonne].append(val)
					except ValueError:
						continue
	
	for colonne, valeurs in data.items():
		if valeurs:  # vérifier qu'il y a des données
			n = len(valeurs)
			mean = sum(valeurs) / n
			variance = sum((x - mean) ** 2 for x in valeurs) / n
			std_dev = variance ** 0.5
			#print(f"{colonne}: count={n}, mean={mean:.2f}, std_dev={std_dev:.2f}")

	# Construire le tableau
	colonnes = sorted([k for k, v in data.items() if v])
	stats = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
	# Afficher l'en-tête
	header = " " * 10 + " ".join(f"{col:>15}" for col in colonnes)
	print(header)
	# Afficher chaque statistique
	for stat in stats:
		line = f"{stat:<10}"
		for colonne in colonnes:
			valeurs = data[colonne]
			if stat == "Count":
				value = len(valeurs)
			elif stat == "Mean":
				value = sum(valeurs) / len(valeurs)
			elif stat == "Std":
				mean = sum(valeurs) / len(valeurs)
				variance = sum((x - mean) ** 2 for x in valeurs) / len(valeurs)
				value = variance ** 0.5
			elif stat == "Min":
				value = min(valeurs)
			elif stat == "Max":
				value = max(valeurs)
			elif stat == "25%":
				value = percentile(valeurs, 25)
			elif stat == "50%":
				value = percentile(valeurs, 50)
			elif stat == "75%":
				value = percentile(valeurs, 75)
			if stat == "Count":
				line += f"{value:>15.0f}"
			else:
				line += f"{value:>15.6f}"
		print(line)



if __name__ == "__main__":	
	if len(sys.argv) != 2:
		print("Usage: python describe.py <csv_file>")
		sys.exit(1)
	describe(sys.argv[1])