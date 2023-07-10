## Python Sorter

This repository contains a Python script that implements the merge sort algorithm to sort a list of names. The script prompts the user to compare pairs of names and choose their preferred one until the entire list is sorted.

The merge sort algorithm used in this script is a divide-and-conquer algorithm that recursively divides the list into smaller sublists, sorts them, and then merges them back together to obtain the final sorted list. It has a time complexity of O(n log n), making it efficient for sorting large lists.

# How to Use
Clone the Repository: Start by cloning this repository to your local machine using Git or any Git client of your choice.

`git clone <repository_url>`

**Prepare Input:** Create a text file containing the names you want to sort, with each name on a separate line. Save the file in the names directory within the cloned repository.

**Run the Script:** Open a terminal or command prompt, navigate to the cloned repository's directory, and run the following command:

```python sorter.py```

**Follow the Prompts:** The script will prompt you to compare pairs of names and choose your preferred name. Enter '1' or '2' to indicate your choice. Repeat this process until all the names are sorted.

**View the Results:** Once the sorting is complete, the sorted names will be saved in a timestamped text file in the results directory.

# File Structure
The repository has the following structure:

├── names/

│   └── <filename>.txt

├── results/

├── sorter.py

└── README.md

**names/:** This directory contains the input text files with the names to be sorted.
**results/:** This directory will store the output files with the sorted names.
**merge_sort.py:** The Python script that implements the merge sort algorithm.
**README.md:** The README file you are currently reading.

# Contributing
Contributions to this repository are welcome. If you find any issues or want to propose improvements, feel free to create a pull request or submit an issue.

VIRAL PUBLIC LICENSE
Copyleft (ɔ) All Rights Reversed

This WORK is hereby relinquished of all associated ownership, attribution and copy rights, and redistribution or use of any kind, with or without modification, is permitted without restriction subject to the following conditions:

1. Redistributions of this WORK, or ANY work that makes use of ANY of the contents of this WORK by ANY kind of copying, dependency, linkage, or ANY other possible form of DERIVATION or COMBINATION, must retain the ENTIRETY of this license.
2. No further restrictions of ANY kind may be applied.
