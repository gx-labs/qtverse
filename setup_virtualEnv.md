# Check Python Version
* make sure you have python 3.7 or above

## Create & Load - Virtual ENV

### Using VSCODE
* Ctrl + Shift + P - in vscode
* Select "Python:Create Environment" - select the requirements.txt file and create one
* Select "Python:Select Interpreter" - select the one created in this repo
* Run Python file

### Manual
```
python -m venv .venv
source./.venv/bin/activate (linux) OR.\.venv\Scripts\Activate.
pip install --upgrade pip
pip install -r requirements.txt
``````
