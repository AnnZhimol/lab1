import math

def calculate_shannon_entropy(data, target_column):
    entropy = 0
    total_count = len(data)

    values = data[target_column].value_counts()

    for value_count in values:
        p = value_count / total_count
        entropy -= p * math.log2(p)

    return entropy

def choose_best_attribute(data, target_column, attributes):
    base_entropy = calculate_shannon_entropy(data, target_column)
    information_gain = {}

    for attribute in attributes:
        unique_values = data[attribute].unique()
        weighted_entropy = 0

        for value in unique_values:
            subset = data[data[attribute] == value]
            p = len(subset) / len(data)
            weighted_entropy += p * calculate_shannon_entropy(subset, target_column)

        information_gain[attribute] = - base_entropy + weighted_entropy

    best_attribute = max(information_gain, key=information_gain.get)

    return best_attribute
def build_decision_tree(data, target_column, attributes):
    if len(data[target_column].unique()) == 1:
        return data[target_column].iloc[0]

    if len(attributes) == 0:
        return data[target_column].mode().iloc[0]

    best_attribute = choose_best_attribute(data, target_column, attributes)

    tree = {best_attribute: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attribute]

    for value in data[best_attribute].unique():
        subset = data[data[best_attribute] == value]
        if len(subset) == 0:
            tree[best_attribute][value] = data[target_column].mode().iloc[0]
        else:
            tree[best_attribute][value] = build_decision_tree(subset, target_column, remaining_attributes)

    return tree
def print_decision_tree(tree, indent=""):
    if isinstance(tree, dict):
        attribute = list(tree.keys())[0]
        result = f"{indent}{attribute}:<br>"
        for value, subtree in tree[attribute].items():
            result += f"&nbsp;{indent}  {value}<br>"
            result += print_decision_tree(subtree, indent + "&nbsp;&nbsp;&nbsp;&nbsp;")
        return result
    else:
        return f"{indent}Class: {tree}<br>"



def predict(tree, sample, target):
    if isinstance(tree, dict):
        attribute = list(tree.keys())[0]
        value = sample.get(attribute)
        subtree = tree[attribute].get(value, target)
        return predict(subtree, sample, target)
    else:
        return tree



