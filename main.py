from fzfmenus import menu
import os, subprocess
import shutil
def move_files_to_plugin_folder():
    source_folder = os.path.expanduser("~/fuziontemp")
    target_folder = os.path.expanduser('~/.config/fuzion/plugins')
    os.makedirs(target_folder, exist_ok=True)
    files_to_move = os.listdir(source_folder)
    for file_name in files_to_move:
        if file_name == ".git":
            continue
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        shutil.move(source_path, target_path)
os.system("rm -rf ~/fuziontemp")
os.system("mkdir ~/fuziontemp")
os.system("git clone -n --depth=1 --filter=tree:0  https://github.com/Zeviraty/fuzionplug-plugin-repo ~/fuziontemp")
files = subprocess.check_output("cd ~/fuziontemp && git ls-tree --full-name --name-only -r HEAD | head", shell=True, universal_newlines=True).strip().split("\n")
plugins = []
if not os.path.exists(os.path.expanduser('~/.config/fuzion/plugins/pluglib.py')) or not os.path.exists(os.path.expanduser('~/.config/fuzion/plugins/_fzfmenus.py')):
    os.system(f"cd ~/fuziontemp && git sparse-checkout set --no-cone _fzfmenus.py pluglib.py && git checkout")
    os.system("mkdir ~/fuziontemp")
    move_files_to_plugin_folder()
    os.system("rm -rf ~/fuziontemp")
    exit
for i in files:
    if i.endswith(".py") and not i in ("_fzfmenus.py", "pluglib.py"):
        plugins.append(i[:-3])
plug = menu(plugins) + ".py"

os.system(f"cd ~/fuziontemp && git sparse-checkout set --no-cone {plug} _fzfmenus.py pluglib.py && git checkout")
move_files_to_plugin_folder()
os.system("rm -rf ~/fuziontemp")
