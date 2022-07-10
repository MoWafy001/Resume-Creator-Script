![](.not-important/demo.png)

# Resume Creator
This a python script that create a PDF resume, using the variables in `vars.yaml`.

The script puts the pieces in the `layout` folder together and replaces the variable names with their values in `vars.yaml`.

If, for example, you have 3 links in your resume and want to add a 4th link, you can just add the 4th link to the `links` array in `vars.yaml`.

The layout can be modified to use more variables if needed.

# Install requirements
To install the required python libararies to run the script.
```
pip install -r requirements.txt
```

# Run
1. Add the data you need to display in the resume to `vars.yaml`
2. run the script
```
python script.py
```
or
```

python3 script.py
```

# Output
A pdf file names `out.pdf` will be created when the script is run.