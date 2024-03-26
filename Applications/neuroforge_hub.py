import os
import subprocess

def open_simulation_experiments_folder():
    """Open the Simulation_Experiments folder."""
    folder_path = os.path.abspath("Simulation_Experiments")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

def open_neuromorphic_hardware_designs_folder():
    """Open the Neuromorphic_Hardware_Designs folder."""
    folder_path = os.path.abspath("Neuromorphic_Hardware_Designs")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

def open_cognitive_computing_algorithms_folder():
    """Open the Cognitive_Computing_Algorithms folder."""
    folder_path = os.path.abspath("Cognitive_Computing_Algorithms")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

def open_brain_inspired_architectures_folder():
    """Open the Brain_Inspired_Architectures folder."""
    folder_path = os.path.abspath("Brain_Inspired_Architectures")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

def open_collaborative_projects_folder():
    """Open the Collaborative_Projects folder."""
    folder_path = os.path.abspath("Collaborative_Projects")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

def open_training_and_education_folder():
    """Open the Training_and_Education folder."""
    folder_path = os.path.abspath("Training_and_Education")
    subprocess.Popen(f'explorer.exe "{folder_path}"')

if __name__ == "__main__":
    while True:
        print("Welcome to NeuroForge Hub!")
        print("Select a folder to open:")
        print("1 - Simulation Experiments")
        print("2 - Neuromorphic Hardware Designs")
        print("3 - Cognitive Computing Algorithms")
        print("4 - Brain-Inspired Architectures")
        print("5 - Collaborative Projects")
        print("6 - Training and Education")
        print("7 - Exit")

        option = input("Enter your selection (1-7): ")

        if option == "1":
            open_simulation_experiments_folder()
        elif option == "2":
            open_neuromorphic_hardware_designs_folder()
        elif option == "3":
            open_cognitive_computing_algorithms_folder()
        elif option == "4":
            open_brain_inspired_architectures_folder()
        elif option == "5":
            open_collaborative_projects_folder()
        elif option == "6":
            open_training_and_education_folder()
        elif option == "7":
            break
        else:
            print("Invalid selection, please try again.")

        input("Press any key to continue...")
    print("Goodbye!")
