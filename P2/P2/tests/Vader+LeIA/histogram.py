import matplotlib.pyplot as plt

# Compounds values for Leia and Vader from the provided data
leia_compounds = [
    -0.9919, -0.8391, -0.9992, -0.9991, -0.9989, -0.9991, -0.9941, -0.9998,
    -0.9996, -0.9994, -0.9984, -0.9993, -0.9995, -0.9996, -0.9999, -0.9998, -0.9995
]
vader_compounds = [
    0.9995, -0.9862, 0.8985, -0.9964, 0.9999, 0.9998, 0.9997, 0.9961,
    0.9282, 0.9996, 0.9965, 0.9996, 0.9987, 0.9993, -0.9997, 0.9996, 0.9993
]

# Creating the histogram
plt.figure(figsize=(10, 6))
analysis_range = range(1, 18)  # 17 analyses

plt.bar(analysis_range, leia_compounds, width=0.4, label='Leia', align='center')
plt.bar(analysis_range, vader_compounds, width=0.4, label='Vader', align='edge')

plt.xlabel('Capitulo')
plt.ylabel('Compound Score')
plt.title('Compounds do LeIA e Vader por capitulo')
plt.xticks(analysis_range)
plt.legend()
plt.grid(axis='y')

plt.show()