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
        print(i)
        new = i.removesuffix(".tif")
        new = new.removeprefix(path)
        new = new.replace("-", "_")
        new = path+new.removesuffix("_0") + ".tif"
        print(new)
        os.rename(i, new)
    print("Files renamed.")
else:
    print("Operation cancelled.")
