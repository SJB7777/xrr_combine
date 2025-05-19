@echo off
SET venv_path=.\.venv

REM .venv 디렉토리가 존재하는지 확인
IF EXIST %venv_path%\ (
    echo Virtual environment already exists.
    GOTO activate_and_run
)

REM .venv 디렉토리가 없을 경우: 생성 및 모듈 설치
echo Creating virtual environment in %venv_path%...
REM 시스템에 파이썬이 설치되어 있고 PATH에 추가되어 있어야 합니다.
python -m venv %venv_path%
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create virtual environment.
    echo Make sure Python is installed and accessible in your system's PATH.
    PAUSE
    EXIT /B 1
)
echo Virtual environment created successfully.

echo Installing dependencies from requirements.txt into %venv_path%...
IF NOT EXIST requirements.txt (
    echo WARNING: requirements.txt not found. Skipping dependency installation.
) ELSE (
    REM 새로 생성된 venv의 pip 사용
    %venv_path%\Scripts\pip install -r requirements.txt
    IF %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install dependencies from requirements.txt.
        PAUSE
        EXIT /B 1
    )
    echo Dependencies installed successfully.
)

:activate_and_run
REM venv 활성화
echo Activating virtual environment...
CALL %venv_path%\Scripts\activate

REM 활성화 성공 여부 확인 (선택 사항이지만 권장)
IF NOT DEFINED VIRTUAL_ENV (
    echo ERROR: Failed to activate virtual environment.
    PAUSE
    EXIT /B 1
)

REM 메인 스크립트 실행
echo Running main script (main.py)...
python main.py

REM 스크립트 실행 후 창 자동 닫기 (PAUSE 제거됨)
REM 만약 스크립트 실행 중 에러 발생 시 창을 유지하고 싶다면 아래 PAUSE 줄의 REM을 제거하세요.
REM IF %ERRORLEVEL% NEQ 0 PAUSE

REM 스크립트의 종료 코드를 반환하며 배치 파일 종료
EXIT /B %ERRORLEVEL%