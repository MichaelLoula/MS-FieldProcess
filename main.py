import pandas as pd
import os
import csv
import json
import constructor
from plyer import notification

def create_output_folder():
    user_dir = os.path.expanduser("~")
    output_dir = os.path.join(user_dir, "msField")

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    return output_dir

def file_selected_callback(input_path):

    output_dir = create_output_folder()
    
    inputPath = input_path

    outputPath = os.path.abspath('./Output/')
    if inputPath.endswith(".xlsx"):
        df = pd.read_excel(inputPath, sheet_name=0, header=0, dtype=str)
    elif inputPath.endswith(".csv"):
        df = pd.read_csv(inputPath, sep=";", header=0, dtype=str, encoding="windows-1252")

    df.fillna("", inplace=True)
    
    data = {}

    for _, row in df.iterrows():
        data[row["Nome do Campo"]] = row["Tipo do Dado"].upper()

    json_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(inputPath))[0] + ".json")

    with open(json_file_path, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    json_string = json.dumps(data, indent=4, ensure_ascii=False)

    print("SALVOU O ARQUIVO:", os.path.splitext(os.path.basename(inputPath))[0] + ".json")
    return json_string