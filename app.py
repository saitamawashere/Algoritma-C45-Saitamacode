import math

# Fungsi untuk menghitung entropy dari suatu himpunan data
def calculate_entropy(data):
    total_count = len(data)
    label_counts = {}
    entropy = 0

    # Menghitung jumlah kemunculan setiap label
    for instance in data:
        label = instance[-1]
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    # Menghitung entropy
    for label in label_counts:
        probability = label_counts[label] / total_count
        entropy -= probability * math.log2(probability)

    return entropy

# Fungsi untuk membagi data berdasarkan nilai atribut tertentu
def split_data(data, attribute_index):
    attribute_values = {}
    
    # Membuat dictionary kosong untuk setiap nilai atribut
    for instance in data:
        attribute_value = instance[attribute_index]
        if attribute_value not in attribute_values:
            attribute_values[attribute_value] = []
            
    # Memasukkan setiap instance data ke dalam dictionary sesuai dengan nilai atributnya
    for instance in data:
        attribute_value = instance[attribute_index]
        attribute_values[attribute_value].append(instance)
    
    return attribute_values

# Fungsi untuk menghitung gain ratio dari suatu atribut
def calculate_gain_ratio(data, attribute_index):
    # Menghitung entropy sebelum pemisahan
    initial_entropy = calculate_entropy(data)

    # Memisahkan data berdasarkan atribut yang dipilih
    attribute_values = split_data(data, attribute_index)

    # Menghitung weighted entropy setelah pemisahan
    weighted_entropy = 0
    intrinsic_value = 0

    for attribute_value in attribute_values:
        subset = attribute_values[attribute_value]
        subset_entropy = calculate_entropy(subset)
        subset_weight = len(subset) / len(data)
        weighted_entropy += subset_weight * subset_entropy
        intrinsic_value -= subset_weight * math.log2(subset_weight)

    # Menghitung gain ratio
    gain = initial_entropy - weighted_entropy
    gain_ratio = gain / intrinsic_value if intrinsic_value != 0 else 0

    return gain_ratio

# Fungsi untuk memilih atribut terbaik berdasarkan gain ratio tertinggi
def choose_best_attribute(data, attributes):
    best_gain_ratio = 0
    best_attribute = None

    for attribute_index in range(len(attributes)):
        gain_ratio = calculate_gain_ratio(data, attribute_index)
        if gain_ratio > best_gain_ratio:
            best_gain_ratio = gain_ratio
            best_attribute = attributes[attribute_index]

    return best_attribute

# Contoh data
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

# Atribut-atribut pada data
attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play']

# Memilih atribut terbaik
best_attribute = choose_best_attribute(data, attributes)
print("Atribut terbaik:", best_attribute)