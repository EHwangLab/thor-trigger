# Arduino Thor Trigger and Python-based TK GUI

## Push [arduino_thor_trigger.sketch](arduino_thor_trigger.sketch) to Arduino board

## Use thor_trigger.exe in Releases

### To create _dist/thor_trigger.exe_ locally

    pip install pyserial pyinstaller
    pyinstaller.exe -w -i FaceValueDog50.ico -F --clean --add-data "FaceValueDog50.png;." thor_trigger.py