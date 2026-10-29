import os

folder = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(folder, "input.txt")
output_file = os.path.join(folder, "output.txt")

try:
   
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    
    total_lines = len(lines)
    print(f"Total number of lines: {total_lines}")

    
    extracted_lines = lines[:2]

   
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(extracted_lines)

    print(f"First two lines written to: {output_file}")

except FileNotFoundError:
    print(f"Error: Input file not found: {input_file}")

except OSError as e:
    print(f"File error: {e}")
