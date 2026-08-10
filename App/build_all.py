import os
import subprocess
import shutil

def run_command(command, cwd=None):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        return False
    return True

def build():
    # 1. Build Vue Dashboard
    print("--- Building Vue Dashboard ---")
    dashboard_path = os.path.join(os.getcwd(), "Dashboard")
    if not run_command("npm run build", cwd=dashboard_path):
        return

    # 2. Copy dist to App folder
    print("--- Copying dist folder ---")
    dist_source = os.path.join(dashboard_path, "dist")
    dist_dest = os.path.join(os.getcwd(), "dist")
    
    if os.path.exists(dist_dest):
        shutil.rmtree(dist_dest)
    shutil.copytree(dist_source, dist_dest)

    # 3. Run PyInstaller
    print("--- Running PyInstaller ---")
    import sys
    python_cmd = "python" if sys.platform == "win32" else "python3"
    sep = ";" if sys.platform == "win32" else ":"
    
    pyinstaller_cmd = (
        f'{python_cmd} -m PyInstaller --noconsole --onefile '
        f'--icon=icon.png '
        f'--add-data "icon.png{sep}." '
        f'--add-data "dist{sep}dist" '
        f'--name "MorgiFile" '
        f'--hidden-import "uvicorn.logging" '
        f'--hidden-import "uvicorn.loops" '
        f'--hidden-import "uvicorn.loops.auto" '
        f'--hidden-import "uvicorn.protocols" '
        f'--hidden-import "uvicorn.protocols.http" '
        f'--hidden-import "uvicorn.protocols.http.auto" '
        f'--hidden-import "uvicorn.protocols.websockets" '
        f'--hidden-import "uvicorn.protocols.websockets.auto" '
        f'--hidden-import "uvicorn.lifespan" '
        f'--hidden-import "uvicorn.lifespan.on" '
        f'app.py'
    )
    
    if not run_command(pyinstaller_cmd):
        return

    print("\n" + "="*30)
    print("BUILD COMPLETE!")
    print("EXE location: dist/MorgiFile.exe")
    print("="*30)

if __name__ == "__main__":
    build()
