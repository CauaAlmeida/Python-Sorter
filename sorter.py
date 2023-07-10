import os
from datetime import datetime

def merge_sort(names, scores):
    if len(names) <= 1:
        return names, scores

    mid = len(names) // 2
    left_names, left_scores = merge_sort(names[:mid], scores[:mid])
    right_names, right_scores = merge_sort(names[mid:], scores[mid:])

    return merge(left_names, right_names, left_scores, right_scores)


def merge(left_names, right_names, left_scores, right_scores):
    merged_names = []
    merged_scores = []
    left_index = 0
    right_index = 0

    while left_index < len(left_names) and right_index < len(right_names):
        print(f"Battle: {left_names[left_index]} vs {right_names[right_index]}")
        choice = input("Enter your preferred name (1 or 2): ")

        if choice == '1':
            merged_names.append(left_names[left_index])
            merged_scores.append(left_scores[left_index])
            left_index += 1
        elif choice == '2':
            merged_names.append(right_names[right_index])
            merged_scores.append(right_scores[right_index])
            right_index += 1
        else:
            print("Invalid choice. Try again.")

    # Append remaining names and scores
    merged_names.extend(left_names[left_index:])
    merged_scores.extend(left_scores[left_index:])
    merged_names.extend(right_names[right_index:])
    merged_scores.extend(right_scores[right_index:])

    return merged_names, merged_scores


filename = input("Enter the name of the file (without extension): ")
filepath = f"./names/{filename}.txt"

# Read names from file
with open(filepath, "r") as file:
    names = [line.strip() for line in file]

scores = [0] * len(names)

sorted_names, sorted_scores = merge_sort(names, scores)

if not os.path.exists("results"):
    os.makedirs("results")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"{timestamp} - {filename}.txt"
output_filepath = os.path.join("results", output_filename)

with open(output_filepath, "w") as file:
    for name in sorted_names:
        file.write(name + "\n")

rounds_left = len(sorted_names) - 1
print(f"Sorting complete. Sorted names saved to '{output_filename}'.")