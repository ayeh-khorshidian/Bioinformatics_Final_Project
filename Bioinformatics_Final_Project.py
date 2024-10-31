# Bioinformatics_Final_Project.py

import os
import re

# Question 1: Extract coding and non-coding regions from a DNA sequence
def extract_exons_introns():
    with open("Q1_dna.txt", "r") as file:
        dna_sequence = file.read().strip()

    exon1 = dna_sequence[:63]
    intron = dna_sequence[63:91]
    exon2 = dna_sequence[91:]

    with open("coding.txt", "w") as coding_file:
        coding_file.write(exon1 + exon2)

    with open("non_coding.txt", "w") as non_coding_file:
        non_coding_file.write(intron)

    # Calculate coding percentage
    coding_length = len(exon1) + len(exon2)
    total_length = len(dna_sequence)
    coding_percentage = (coding_length / total_length) * 100
    print(f"Coding percentage: {coding_percentage:.2f}%")

# Question 2: Generate FASTA files
def create_fasta_files():
    with open("Q2_sequences.txt", "r") as seq_file, open("Q2_AccessionNumbers.txt", "r") as acc_file:
        sequences = [re.sub(r'\W+', '', line.strip().upper()) for line in seq_file]
        accessions = [line.strip() for line in acc_file]

    for accession, sequence in zip(accessions, sequences):
        with open(f"{accession}.txt", "w") as fasta_file:
            fasta_file.write(f">{accession}\n{sequence}\n")

# Question 3: Check reverse complement
def is_reverse_complement(seq1, seq2):
    complement_map = str.maketrans("ATCG", "TAGC")
    reverse_complement = seq1.translate(complement_map)[::-1]
    return reverse_complement == seq2

# Question 4: Population growth prediction
def population_growth():
    start_size = int(input("Starting number of organisms (minimum 2): "))
    daily_increase = float(input("Average daily population increase (%): "))
    days = int(input("Number of days to multiply: "))

    if start_size < 2 or daily_increase < 0 or days < 1:
        print("Invalid inputs.")
        return

    print("Day\tOrganisms")
    print("-" * 15)
    population = start_size
    for day in range(1, days + 1):
        print(f"{day}\t{population:.2f}")
        population += population * (daily_increase / 100)

# Question 5: Store and sort user-entered lines
def sorted_lines():
    lines = []
    while True:
        line = input("Enter a line (or 'quit' to finish): ")
        if line.lower() == "quit":
            break
        lines.append(line)
    print("Sorted lines:", sorted(lines))

# Question 6: Modified sorted lines (with line count and slicing)
def sorted_lines_with_count():
    lines = []
    while True:
        line = input("Enter a line (or 'quit' to finish): ")
        if line.lower() == "quit":
            break
        lines.append(line)
    print(f"Total lines entered: {len(lines)}")
    print("Lines 2 to 4:", lines[1:4])

# Question 7: Sequence length analysis
def analyze_sequence_lengths():
    lengths = input("Enter sequence lengths separated by spaces: ")
    lengths_list = [int(length) for length in lengths.split()]
    total_length = sum(lengths_list)
    average_length = total_length / len(lengths_list)
    print(f"Total length: {total_length}")
    print(f"Average length: {average_length:.2f}")

# Question 8: FASTA sequence analysis with menu
def fasta_analysis_menu():
    filename = input("Enter FASTA file name: ")
    if not os.path.exists(filename):
        print("File not found.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()
        dna_sequence = ''.join(line.strip() for line in lines if not line.startswith(">"))

    def count_nucleotides(sequence):
        return {nucleotide: sequence.count(nucleotide) for nucleotide in "AGCTN"}

    def at_content(sequence):
        return (sequence.count("A") + sequence.count("T")) / len(sequence) * 100

    def gc_content(sequence):
        return (sequence.count("G") + sequence.count("C")) / len(sequence) * 100

    def complement(sequence):
        return sequence.translate(str.maketrans("ATCG", "TAGC"))

    def reverse_complement(sequence):
        return complement(sequence)[::-1]

    options = {
        'A': lambda: print(count_nucleotides(dna_sequence)),
        'B': lambda: print(f"AT content: {at_content(dna_sequence):.2f}%"),
        'C': lambda: print(f"GC content: {gc_content(dna_sequence):.2f}%"),
        'D': lambda: print(f"Complement: {complement(dna_sequence)}"),
        'E': lambda: print(f"Reverse complement: {reverse_complement(dna_sequence)}")
    }

    print("Menu:")
    print("A. Calculate DNA composition")
    print("B. Calculate AT content")
    print("C. Calculate GC content")
    print("D. Complement")
    print("E. Reverse complement")
    choice = input("Choose an option: ").upper()

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice.")

# Main function to call each task
def main():
    extract_exons_introns()
    create_fasta_files()
    seq1 = input("Enter first DNA sequence: ")
    seq2 = input("Enter second DNA sequence: ")
    print("Are reverse complements:", is_reverse_complement(seq1, seq2))
    population_growth()
    sorted_lines()
    sorted_lines_with_count()
    analyze_sequence_lengths()
    fasta_analysis_menu()

if __name__ == "__main__":
    main()

