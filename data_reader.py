import pickle

with open("binary.bzn", "rb") as file:
    data = pickle.load(file)
print(data)