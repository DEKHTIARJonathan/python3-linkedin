call venv\Scripts\activate.bat
python setup.py sdist
python setup.py bdist_wheel
python setup.py bdist_wheel --universal
python setup.py egg_info
PAUSE;