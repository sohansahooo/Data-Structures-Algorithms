import os

def merge_python_files(source_folder, output_file):
    folder_name = os.path.basename(source_folder)  # Extract the folder name
    with open(output_file, "w") as outfile:
        outfile.write(f"# Source folder: {folder_name}\n\n")  # Write the folder name
        for filename in os.listdir(source_folder):
            if filename.endswith(".py"):
                with open(os.path.join(source_folder, filename), "r") as infile:
                    content = infile.read()
                    outfile.write(f"# {filename}\n")
                    outfile.write(content)
                    outfile.write("\n\n")


source_folder = r"C:\Users\sohan\Desktop\Start Over\Gain Knowledge\Software Engineering\00 Foundational Knowledge\Data Structures & Algorithms\DSA Problems and Solution\06 Circular Doubly LLs Probs"
output_file = "merged_assignment.py"

merge_python_files(source_folder, output_file)
