import numpy as np
import networkx as nx


def get_data():
    with open('./src/raw/data.txt', 'r', encoding='utf-8') as f:
        return f.read()


def load_to_array(data):
    return data.split()


def build_graph(data):
    G = nx.DiGraph()

    for i in range(len(data) - 1):
        word, next_word = data[i], data[i + 1]

        if G.has_edge(word, next_word):
            G[word][next_word]["weight"] += 1
        else:
            G.add_edge(word, next_word, weight=1)

    return G


def predict_next_word(graph, word):
    if word not in graph:
        return []

    successors = graph[word]
    sorted_successors = sorted(
        successors.items(), key=lambda x: x[1]['weight'], reverse=True)

    return sorted_successors


data = get_data()
word_array = load_to_array(data)
graph = build_graph(word_array)

while True:
    input_word = input("Ingresa palabra: ")
    predictions = predict_next_word(graph, input_word)

    print(f"{input_word} {predictions}")
