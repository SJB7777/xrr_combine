import os, sys, shutil, subprocess

def run(cmd):
    print(f"[CMD] {' '.join(cmd)}")
    subprocess.check_call(cmd)

def main():
    # 1. uv 확인
    if shutil.which("uv") is None:
        print("[INFO] uv not found. Installing via pip...")
        run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        run([sys.executable, "-m", "pip", "install", "uv"])
    else:
        print("[INFO] uv is already installed.")

    # 2. venv 생성
    if not os.path.isdir(".venv"):
        print("[INFO] Creating virtual environment with uv (Python 3.13)...")
        run(["uv", "venv", ".venv", "--python", "3.13"])

    # 3. requirements 설치
    if os.path.exists("requirements.txt"):
        print("[INFO] Installing dependencies from requirements.txt...")
        run(["uv", "pip", "install", "-r", "requirements.txt"])

    # 4. main.py 실행
    print("[INFO] Running main.py...")
    run(["uv", "run", "python", "main.py"])

if __name__ == "__main__":
    main()
