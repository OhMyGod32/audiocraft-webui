import os

def modify_config_files(py310_path, venv_path):
    venv_cfg_path = os.path.join(venv_path, 'pyvenv.cfg')
    activate_path = os.path.join(venv_path, 'Scripts', 'activate')
    activate_bat_path = os.path.join(venv_path, 'Scripts', 'activate.bat')

    # 修改pyvenv.cfg文件
    with open(venv_cfg_path, 'r') as f:
        lines = f.readlines()

    with open(venv_cfg_path, 'w') as f:
        for line in lines:
            if line.startswith('home'):
                line = f'home = {py310_path}\n'
            f.write(line)

    # 修改activate文件
    with open(activate_path, 'r') as f:
        lines = f.readlines()

    with open(activate_path, 'w') as f:
        for line in lines:
            if line.startswith('VIRTUAL_ENV='):
                line = f'VIRTUAL_ENV="{venv_path}"\n'
            f.write(line)

    # 修改activate.bat文件
    with open(activate_bat_path, 'r') as f:
        lines = f.readlines()

    with open(activate_bat_path, 'w') as f:
        for line in lines:
            if line.startswith('set "VIRTUAL_ENV='):
                line = f'set "VIRTUAL_ENV={venv_path}"\n'
            f.write(line)

# 获取当前目录
current_dir = os.getcwd()

# 获取py310文件夹路径
py310_dir = os.path.join(current_dir, 'py310')

# 获取venv文件夹路径
venv_dir = os.path.join(current_dir, 'venv')

# 修改配置文件
modify_config_files(py310_dir, venv_dir)