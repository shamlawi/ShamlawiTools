import os
import subprocess

def clone_repositories(urls, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    for url in urls:
        # Strip leading/trailing whitespaces and newline characters
        url = url.strip()

        # Extract the repository name from the URL
        repo_name = url.split("/")[-1].rstrip(".git")

        # Construct the destination path
        destination_path = os.path.join(destination_folder, repo_name)

        # Clone the repository
        subprocess.run(["git", "clone", url, destination_path], check=True)

if __name__ == "__main__":
    # List of Git URLs you want to clone
    git_urls = [
        "https://github.com/fuzzdb-project/fuzzdb",
        "https://github.com/Bo0oM/fuzz.txt",
        '''
        "https://github.com/arbazkiraak/LinksDumper",
       
        "https://github.com/zseano/JS-Scan",
        
        "https://github.com/projectdiscovery/subfinder",
        '''
    ]

    # Folder where you want to clone the repositories
    destination_folder = "/home/kali/Desktop/Hacking Tools/Recon/Fuzzing"

    # Clone the repositories
    clone_repositories(git_urls, destination_folder)

