import numpy as np

# STEP 1: Define the Scoring Rules
MATCH_SCORE = 1
MISMATCH_PENALTY = -2

# STEP 2: Digitize Sequences
def encode_sequence(dna_string):
    """Converts a DNA string into a numerical NumPy array."""
    nucleotide_map = {'A': 1, 'T': 2, 'C': 3, 'G': 4, 'N': 0}
    # Convert string to list of numbers
    numeric_list = [nucleotide_map.get(base, 0) for base in dna_string]
    return np.array(numeric_list)

# STEP 3: Vectorization and Building the Scoring Algorithm
def calculate_mutation_score(target_arr, test_arr):
    """Compares two numerical arrays and calculates a score without loops."""
    if len(target_arr) != len(test_arr):
        raise ValueError("Sequences must be the same length to compare.")
    score_array = np.where(target_arr == test_arr, MATCH_SCORE, MISMATCH_PENALTY)
    
    # Sum the entire array instantly to get the final score
    total_score = np.sum(score_array)
    return total_score

# STEP 4: Test Edge Cases
if __name__ == "__main__":
    # Define a target (perfect) sequence
    target_dna = "ATCGGCTA"
    target_arr = encode_sequence(target_dna)
    
    # Define test sequences with varying mutations
    test_cases = {
        "Perfect Match": "ATCGGCTA",
        "One Mutation (Off-target)": "ATCGTCTA", # G changed to T
        "Total Mismatch": "TAGCCGAT" 
    }
    
    print(f"Target Sequence: {target_dna}\n" + "-"*30)
    
    # Score each case
    results = {}
    for name, seq in test_cases.items():
        test_arr = encode_sequence(seq)
        score = calculate_mutation_score(target_arr, test_arr)
        results[name] = score
        print(f"Test: {name}")
        print(f"Sequence: {seq} | Score: {score}\n")