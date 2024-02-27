import os
import glob

path = os.getcwd()
print("Current Path: ", path)
print("Reading files...")

searchcrit = path + "/*.tif"
files = glob.glob(searchcrit)

print("Files found:")
for i in files:
    temp = i
    print(temp.removeprefix(path))

proceed = input("Proceed with renaming? (y/n): ")
if proceed == "y":
    for i in files:
        temp = i
        os.rename(i, i.removesuffix("_0.tif") + ".tif")
    print("Files renamed.")
else:
    print("Operation cancelled.")
