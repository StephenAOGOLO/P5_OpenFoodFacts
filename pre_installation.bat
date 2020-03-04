SET HOME=%CD%
cd ..
python -m virtualenv -p python %HOME%
cd %HOME%
cd .\Scripts
cmd /k "activate&cd %HOME%&pip install -r requirements.txt&echo #&echo ### PREINSTALLATION TERMINE ###&echo #"
pause