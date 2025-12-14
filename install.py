import subprocess

def sync_packages():
    subprocess.run(["pacman", "-Sy"])
    

def main():
    sync_packages()

main()