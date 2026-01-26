import csv
import os
from typing import List, Dict

def explore_med_ethic_eval(dataset_path: str) -> None:
    """
    Explore the MedEthicEval dataset structure and content.
    """
    print("Exploring MedEthicEval dataset...")
    print(f"Dataset path: {dataset_path}")
    
    # List all dataset files
    for file in os.listdir(dataset_path):
        if file.endswith('.csv'):
            file_path = os.path.join(dataset_path, file)
            print(f"\nFound CSV file: {file}")
            
            # Read and display first few lines
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                print(f"Headers: {headers[:10]}...")  # Show first 10 headers
                
                # Show first 2 rows
                for i, row in enumerate(reader):
                    if i < 2:
                        print(f"Row {i+1}:")
                        if 'query' in row:
                            print(f"  Query: {row['query'][:100]}...")
                        elif 'scenario' in row:
                            print(f"  Scenario: {row['scenario'][:100]}...")
                        if 'answer' in row:
                            print(f"  Answer: {row['answer']}")
                    else:
                        break

def extract_first_100_records(input_path: str, output_path: str) -> None:
    """
    Extract first 100 records from a CSV file and save to new file.
    """
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        writer.writeheader()
        
        for i, row in enumerate(reader):
            if i < 100:
                writer.writerow(row)
            else:
                break
    
    print(f"\nExtracted first 100 records to: {output_path}")

if __name__ == "__main__":
    # Explore dataset
    dataset_path = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/ref/MedEthicEval/dataset"
    explore_med_ethic_eval(dataset_path)
    
    # Extract first 100 records from knowledge dataset
    input_file = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/ref/MedEthicEval/dataset/medical_ethics_knowledge.csv"
    output_file = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/Computational-Linguistics-Data-Collection/Data/YujieHe_MedSatetyEthics/med_ethic_eval_sample.csv"
    extract_first_100_records(input_file, output_file)