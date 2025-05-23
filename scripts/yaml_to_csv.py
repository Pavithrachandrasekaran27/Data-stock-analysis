import os
import yaml
import pandas as pd

def yaml_to_csv(yaml_root_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    symbol_data = {}
    for month_folder in os.listdir(yaml_root_path):
        month_path = os.path.join(yaml_root_path, month_folder)
        if os.path.isdir(month_path):
            for file in os.listdir(month_path):
                if file.endswith('.yaml') or file.endswith('.yml'):
                    with open(os.path.join(month_path, file), 'r') as f:
                        data = yaml.safe_load(f)
                        for record in data:
                            symbol = record['symbol']
                            if symbol not in symbol_data:
                                symbol_data[symbol] = []
                            symbol_data[symbol].append(record)

    for symbol, records in symbol_data.items():
        df = pd.DataFrame(records)
        df.to_csv(os.path.join(output_dir, f"{symbol}.csv"), index=False)

if __name__ == "__main__":
    yaml_to_csv("data/yaml_data", "data/csv_output")
