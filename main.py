import numpy as np
import networkx as nx


def main():
    pass


def get_data():
    with open('./src/raw/data.txt', 'r') as f:
        data = f.read()
        return data


def load_to_array(data):
    data = data.replace('\n\n', ' ').split()
    return data
    arr_words = []
    # for word in data.split(' '):
    #     if word != '':
    #         arr_words.append(word)
    # return arr_words


def build_graph(data):
    G = nx.DiGraph()

    for i in range(len(data) - 1):
        word, next_word = data[i], data[i + 1]

        if G.has_edge(word, next_word):
            G[word][next_word]["weight"] += 1
        else:
            G.add_edge(word, next_word, weight=1)

    return G


def pass_to_unique(data):
    return list(set(data))


# def pass_to_matriz(data):
#     G = nx.DiGraph()
#     for word in data:
#         G.add_node(word)

#     for i in range(len(data)-1):
#         G.add_edge(data[i], data[i+1])

#     return G

def predict_next_word(graph, word, top_n=3):
    if word not in graph:
        return []

    successors = graph[word]
    sorted_successors = sorted(
        successors.items(), key=lambda x: x[1]['weight'], reverse=True)

    return [w[0] for w in sorted_successors[:top_n]]


data = get_data()
word_array = load_to_array(data)
unique_matriz = pass_to_unique(word_array)
graph = build_graph(data)
# matriz = pass_to_matriz(unique_matriz)

input_word = "ganadoras"
predictions = predict_next_word(graph, input_word)
print(predictions)

# print(np.dot(adj_matrix, adj_matrix))

# print(adj_matrix)
