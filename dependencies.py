import importlib.metadata
import subprocess
import sys

with open("dependencies.txt") as depends:
    REQUIRED:set[str] ={line.strip() for line in depends}
installed = {pkg.metadata["Name"].lower() for pkg in importlib.metadata.distributions()}
missing = REQUIRED - installed

if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])