![image](https://user-images.githubusercontent.com/47895671/178503283-f519a8a6-3227-4940-bee8-087f8f6280f5.png)


# Resume Creator
This python script creates PDF resumes using variables from `vars.yaml`.

The script puts the pieces in the `layout` folder together and replaces the variable names with their values in `vars.yaml`.

If, for example, you have 3 links in your resume and want to add a 4th link, you can just add the 4th link to the `links` array in `vars.yaml`.

The layout can be modified to use more variables if needed.

# Install requirements
The script uses `pdfkit` which depends on `wkhtmltopdf`.

Install wkhtmltopdf:

Debian/Ubuntu:
```
$ sudo apt-get install wkhtmltopdf
```

macOS:
```
$ brew install homebrew/cask/wkhtmltopdf
```
If you are using Windows, I don't know, search for how to install wkhtmltopdf.

Now, installing the required libraries
```
pip install -r requirements.txt
```
or pip3 for python3

# Run
1. Add the data you want to display in the resume to `vars.yaml`
```yaml
full name: Full Name


job title: Job Title


links:
  - GitHub: https://github.com/MoWafy001
  - LinkedIn: https://linkedin.com/in/mohamedwafy
  - wafy123445@gmail.com: mailto:wafy123445@gmail.com


skills:
  - Python
  - Flask
  - Web Scrapping


experience:
  - Position, Company:
    - start date - end date
    - |
      description


education:
  - Degree, University:
    - start date - end date
    - |
      description

```
2. run the script
```
python script.py
```
or
```
python3 script.py
```

# Output
The name of the output file is the `full name` of the user followed by an `_` followed by the `job title`.
```
Full_Name_Job_Title.pdf
```
