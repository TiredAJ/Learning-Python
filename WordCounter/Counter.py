import os
from os import listdir
from pathlib import Path

CurrentDir = Path(os.getcwd());
Contents = []

Contents = listdir(CurrentDir.parent.absolute())

for F in Contents:
    print(F)

#scrapped for testing C#'s ConcurrentBag