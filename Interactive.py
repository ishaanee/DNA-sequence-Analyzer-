from DNA_seqInfo import *

def get_DNASeq():
    while True:
        DNA_seq = input("Please enter a DNA sequence (A, T, C, G): ").upper().strip()
        if seq_check(DNA_seq):
            return DNA_seq
        else:
            print("Invalid sequence. Please enter a valid DNA sequence!(A, T, C, G)")

def nucFreq_chart(freq):
    print("\nNucleotide Frequency Chart:")
    for nt, count in freq.items():
        print(f"{nt}: {'*' * count} ({count})")

def seqInfo(seq):
    print("\nDNA Sequence Information:")
    print("-" * 40)
    print(f"• Sequence: {seq}")
    print(f"• Sequence length: {len(seq)}")
    print(f"• DNA --> RNA Transcription: {transcription(seq)}")
    print(f"• Complement: {complement(seq)}")
    print(f"• Reverse Complement: {reverseComplement(seq)}")
    print("-" * 40)
    print("DNA string + Complement:")
    print (f"5'{seq} 3'")
    print(f"  {''.join(['|' for _ in range(len(seq))])}")
    print(f"3'{complement(seq)} 5'\n")

    freq = countNucFreq(seq)
    print(f'Nucleotide Frequency: {freq}')
    nucFreq_chart(freq)


def main():
    print("Welcome to the DNA Sequence Information Tool!")
    
    DNASeq = get_DNASeq()
    
    while True:
        print("\nPlease choose from the following:")
        print("1. View your sequence information")
        print("2. Enter a new DNA sequence")
        print("3. Exit")
        
        choice = input("Enter your choice (Please choose from 1/2/3): ")
        
        if choice == '1':
            seqInfo(DNASeq)
        elif choice == '2':
            DNASeq = get_DNASeq()
        elif choice == '3':
            print("Thank you for using my tool!")
            break
        else:
            print("Invalid choice. Please try again with a valid response.")

if __name__ == "__main__":
    main()
