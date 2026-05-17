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
    pyinstaller_cmd = (
        'python -m PyInstaller --noconsole --onefile '
        '--icon=icon.png '
        '--add-data "icon.png;." '
        '--add-data "dist;dist" '
        '--name "MorgiFile" '
        '--hidden-import "uvicorn.logging" '
        '--hidden-import "uvicorn.loops" '
        '--hidden-import "uvicorn.loops.auto" '
        '--hidden-import "uvicorn.protocols" '
        '--hidden-import "uvicorn.protocols.http" '
        '--hidden-import "uvicorn.protocols.http.auto" '
        '--hidden-import "uvicorn.protocols.websockets" '
        '--hidden-import "uvicorn.protocols.websockets.auto" '
        '--hidden-import "uvicorn.lifespan" '
        '--hidden-import "uvicorn.lifespan.on" '
        'app.py'
    )
    
    if not run_command(pyinstaller_cmd):
        return

    print("\n" + "="*30)
    print("BUILD COMPLETE!")
    print("EXE location: dist/MorgiFile.exe")
    print("="*30)

if __name__ == "__main__":
    build()
