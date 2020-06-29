import glob
import os

dir_to_ignore = 'venv/'

parent_dir = os.path.dirname(os.getcwd())
path = os.path.join(parent_dir,'**','.git')

print(f"Searching in {parent_dir}.")

for rep_file in glob.glob(path):
    repository = os.path.dirname(rep_file)
    base_dir = os.path.basename(repository)
    print(f"Found {base_dir}")
    gitignore = os.path.join(repository,'.gitignore')
    with open(gitignore, 'r+') as file:
        contents = file.read()
        if '\n'+dir_to_ignore not in contents:
            file.write('\n'+dir_to_ignore)
            print(f"Added to {base_dir}")
        elif contents.count('\n'+dir_to_ignore) > 1:
            print(f"Multiple Occurences removed in {base_dir}.")
            with open(gitignore, "w") as dup:
                dup.write(contents.replace('\n'+dir_to_ignore,''))
            file.seek(0,2)
            file.write('\n'+dir_to_ignore)

print("Done.")
