import compileall
import shutil
import os
from pathlib import Path

def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()

uid = input("Введите разрешёный uid:")
uid = str(uid)
modified_uid = str(int("1" + "0"*len(uid)) - int(uid))

c_path = './compiled_project' 
if os.path.exists(c_path):
	rmdir(Path(c_path))

os.makedirs(c_path)

shutil.copytree("configs", c_path + "/" + "configs", dirs_exist_ok=True)

with open(c_path + "/account.json", "w") as file:
    file.write("public key here\nsecret key here")

with open("mainwindow.py", "r") as file:
	contents = file.readlines()

initial_uid_str = None
for i in range(len(contents)):
	if "self.allowed_uid = " in contents[i]:
		initial_uid_str = contents[i]
		str_start = contents[i].split(" = ")[0]
		contents[i] = f"{str_start} = \"{modified_uid}\"\n"

with open("mainwindow.py", "w") as file:
    file.writelines(contents)

shutil.copy("run_bot.bat", c_path + "/" + "run_bot.bat")

dir_files = os.listdir()
for filename in dir_files:
	if ".py" in filename:
		shutil.copy(filename, c_path + "/" + filename)

compileall.compile_dir('./compiled_project', legacy=True, force=True)

for filename in dir_files:
	if ".py" in filename:
		os.remove(c_path + "/" + filename)

shutil.make_archive("compiled_project_archive", 'zip', c_path)
rmdir(Path(c_path))

for i in range(len(contents)):
	if "self.allowed_uid = " in contents[i]:
		initial_uid_str = contents[i]
		contents[i] = initial_uid_str

with open("mainwindow.py", "w") as file:
    file.writelines(contents)