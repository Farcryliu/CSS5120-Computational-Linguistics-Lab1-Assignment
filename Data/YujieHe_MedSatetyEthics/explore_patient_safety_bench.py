import json
from pathlib import Path
from typing import List, Dict

def explore_patient_safety_bench(dataset_path: str) -> None:
    """
    Explore the PatientSafetyBench dataset structure and content.
    """
    dataset_path = Path(dataset_path)
    print("Exploring PatientSafetyBench dataset...")
    print(f"Dataset path: {dataset_path}")

    # Read and display first few lines
    with open(dataset_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 5:
                data = json.loads(line)
                print(f"\nRecord {i+1}:")
                print(f"  ID: {data['id']}")
                print(f"  Category: {data['category']}")
                print(f"  Content: {data['content']}")
                print(f"  Judge Score: {data['judge_score']}")
            else:
                break

def extract_first_100_records(input_path: str, output_path: str) -> None:
    """
    Extract first 100 records from a JSONL file and save to new file.
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile):
            if i < 100:
                outfile.write(line)
            else:
                break

    print(f"\nExtracted first 100 records to: {output_path}")

if __name__ == "__main__":
    # Explore dataset
    dataset_path = Path("data/PatientSafetyBench/patientsafetybench.jsonl")
    explore_patient_safety_bench(str(dataset_path))

    # Extract first 100 records
    output_file = Path("patient_safety_bench_sample.jsonl")
    extract_first_100_records(str(dataset_path), str(output_file))