# Vertical Dataset Research

This repository contains synthetic data generators and sample datasets for various industry verticals. It is designed to help with research, prototyping, and testing data-driven applications across multiple domains.

## Project Structure

- `scripts/` — Main directory containing CSV datasets and Python scripts for data generation.
- `scripts/data_generators/` — Subdirectories for each industry vertical, each with its own data generator script and sample CSV files.
  - `banking/`
  - `ecommerce/`
  - `education/`
  - `energy/`
  - `healthcare/`
  - `hospitality/`
  - `insurance/`
  - `manufacturing/`
  - `real_estate/`
  - `retail/`
  - `supply_chain/`
  - `telecom/`
  - `transportation/`

## Usage

1. Navigate to the `scripts/` directory.
2. Run the desired data generator script (e.g., `python generate_banking_data.py`) to produce or update the corresponding CSV files.
3. Use the generated CSV files for analytics, machine learning, or application development.

## Example

```bash
cd scripts
python generate_banking_data.py
```

## Requirements
- Python 3.x
- (Optional) Additional dependencies may be required for specific data generators. Check the script headers for details.

## License
This project is intended for research and educational purposes.
