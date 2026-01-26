import csv
from pathlib import Path
from typing import List, Dict

def explore_med_ethic_eval(dataset_path: str) -> None:
    """
    Explore the MedEthicEval dataset structure and content.
    """
    dataset_path = Path(dataset_path)
    print("Exploring MedEthicEval dataset...")
    print(f"Dataset path: {dataset_path}")

    # List all dataset files
    for file in dataset_path.iterdir():
        if file.is_file() and file.suffix == '.csv':
            print(f"\nFound CSV file: {file.name}")

            # Read and display first few lines
            with open(file, 'r', encoding='utf-8') as f:
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
    input_path = Path(input_path)
    output_path = Path(output_path)
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
    dataset_path = Path("../data/MedEthicEval/dataset")
    explore_med_ethic_eval(str(dataset_path))

    # Extract first 100 records from knowledge dataset
    input_file = Path("../data/MedEthicEval/dataset/medical_ethics_knowledge.csv")
    output_file = Path("../med_ethic_eval_sample.csv")
    extract_first_100_records(str(input_file), str(output_file))