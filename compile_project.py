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
os.makedirs(c_path + "/interface")
os.makedirs(c_path + "/strategy")

shutil.copytree("windows_commands", c_path + "/" + "windows_commands", dirs_exist_ok=True)

with open(c_path + "/account.json", "w") as file:
    file.write("public key here\nsecret key here")

with open("interface/mainwindow.py", "r") as file:
	contents = file.readlines()

initial_uid_str = None
for i in range(len(contents)):
	if "self.allowed_uid = " in contents[i]:
		initial_uid_str = contents[i]
		str_start = contents[i].split(" = ")[0]
		contents[i] = f"{str_start} = \"{modified_uid}\"\n"

with open("interface/mainwindow.py", "w") as file:
    file.writelines(contents)

shutil.copy("requirements.txt", c_path + "/" + "requirements.txt")
shutil.copy("python-3.12.5-amd64.exe", c_path + "/" + "python-3.12.5-amd64.exe")
shutil.copy("ws_port.txt", c_path + "/" + "ws_port.txt")
	    
for m_dir in ["interface", "strategy"]:
	dir_files = os.listdir(m_dir)
	for filename in dir_files:
		if ".py" in filename and "compile" not in filename:
			print(m_dir + "/" + filename, c_path + "/" + m_dir + "/" + filename)
			shutil.copy(m_dir + "/" + filename, c_path + "/" + m_dir + "/" + filename)

	compileall.compile_dir('./compiled_project/' + m_dir + "/", legacy=True, force=True)

	for filename in dir_files:
		if ".py" in filename:
			os.remove(c_path + "/" + m_dir + "/" + filename)

shutil.make_archive("compiled_project_archive", 'zip', c_path)
rmdir(Path(c_path))

for i in range(len(contents)):
	if "self.allowed_uid = " in contents[i]:
		contents[i] = initial_uid_str

with open("./interface/mainwindow.py", "w") as file:
    file.writelines(contents)
