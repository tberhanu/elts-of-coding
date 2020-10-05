def generate_all_binary_trees_driver(N):
    result = ["Root"]
    collector = []
    return generate_all_binary_trees(N - 1, result, collector)

def generate_all_binary_trees(N, result, collector):
    if N == 0:
        collector.append(result)

    else:
        generate_all_binary_trees(N - 1, result + ["Left"], collector)
        generate_all_binary_trees(N - 1, result + ["Right"], collector)

    return collector

if __name__ == "__main__":
    result = generate_all_binary_trees_driver(3)
    print(result)