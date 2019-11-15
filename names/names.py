import time
import sys
sys.path.append('../datastructures')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst = BinarySearchTree("Skyelar Carroll")

# Insert all names into bst
for name_1 in names_1:
    bst.insert(name_1)

# Compare current name to name in bst
for name_2 in names_2:
    if bst.contains(name_2):
        # Append duplicate name to duplicates list
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

