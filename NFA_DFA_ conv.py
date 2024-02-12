# Sample delta dictionary
delta = {('q0', 'l'): {'q1', 'q2', 'q3'},
         ('q1', 'a'): {'q4', 'q5'},
         ('q2', 'b'): {'q6', 'q7'},
         # ... more entries
         }

# Element to find in Q'
s = 'q5'

# Forming set Q' from delta using regular sets
Q_prime = set()

for value_set in delta.values():
    Q_prime.add(tuple(value_set))  # Convert the set to a tuple to make it hashable

# Find and store the set containing 's' in S'
S_prime = set()
for set_item in Q_prime:
    if s in set_item:
        S_prime.add(set_item)
# Sample sets F
F = {'q1', 'q5'}

# Forming set F' that contains the elements of Q' with at least one element of F
F_prime = set()
for set_item in Q_prime:
    if any(item in F for item in set_item):
        F_prime.add(set_item)
# Print the resulting sets
print("Q' =", Q_prime)
print("S' =", S_prime)
print("F' =", F_prime)
