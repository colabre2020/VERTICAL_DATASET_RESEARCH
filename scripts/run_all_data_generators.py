import subprocess
import os

scripts = [
    'insurance/generate_insurance_data.py',
    'banking/generate_banking_data.py',
    'supply_chain/generate_supply_chain_data.py',
    'healthcare/generate_healthcare_data.py',
    'retail/generate_retail_data.py',
    'telecom/generate_telecom_data.py',
    'education/generate_education_data.py',
    'transportation/generate_transportation_data.py',
    'energy/generate_energy_data.py',
    'hospitality/generate_hospitality_data.py',
    'ecommerce/generate_ecommerce_data.py',
    'manufacturing/generate_manufacturing_data.py',
    'real_estate/generate_real_estate_data.py',
]

base_dir = os.path.join(os.path.dirname(__file__), 'data_generators')

if __name__ == '__main__':
    for script in scripts:
        script_dir = os.path.join(base_dir, os.path.dirname(script))
        script_file = os.path.basename(script)
        print(f'Running {script_file} in {script_dir}...')
        subprocess.run(['python', script_file], cwd=script_dir, check=True)
    print('All data generator scripts executed successfully!')
