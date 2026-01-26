import csv
import os
from typing import List, Dict

def explore_med_safety_bench(dataset_path: str) -> None:
    """
    Explore the med-safety-bench dataset structure and content.
    """
    # Check dataset structure
    print("Exploring med-safety-bench dataset...")
    print(f"Dataset path: {dataset_path}")
    
    # List all files in the dataset
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"\nFound CSV file: {file_path}")
                
                # Read and display first few lines
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    headers = reader.fieldnames
                    print(f"Headers: {headers}")
                    
                    # Show first 2 rows
                    for i, row in enumerate(reader):
                        if i < 2:
                            print(f"Row {i+1}:")
                            print(f"  Harmful request: {row['harmful_medical_request'][:100]}...")
                            print(f"  Safe response: {row['safe_response'][:100]}...")
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
    dataset_path = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/ref/med-safety-bench/datasets"
    explore_med_safety_bench(dataset_path)
    
    # Extract first 100 records from test set
    input_file = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/ref/med-safety-bench/datasets/test/gpt4/med_safety_demonstrations_category_1.csv"
    output_file = "/Users/heyujie/Documents/cuhksz-all-sync/code/CSS5120_HW/Computational-Linguistics-Data-Collection/Data/YujieHe_MedSatetyEthics/med_safety_bench_sample.csv"
    extract_first_100_records(input_file, output_file)