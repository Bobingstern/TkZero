:: Will need to install pdoc via:
:: pip install pdoc3
pdoc --html TkZero --output-dir docs --force
move docs\TkZero\* docs
rmdir docs\TkZero