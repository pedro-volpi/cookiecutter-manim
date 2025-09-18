import subprocess
import os

print("Setting up git repository...")

try:
    # Initialize git repo
    subprocess.run(['git', 'init'], check=True, capture_output=True)
    
    # Add all files
    subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
    
    # Make initial commit
    subprocess.run(['git', 'commit', '-m', 'Initial project setup from cookiecutter'], 
                  check=True, capture_output=True)
    
    print("✅ Git repository initialized with initial commit!")
    
except subprocess.CalledProcessError:
    print("⚠️  Git setup failed - you may need to run 'git init' manually")
except FileNotFoundError:
    print("⚠️  Git not found - install Git to enable automatic repository setup")
