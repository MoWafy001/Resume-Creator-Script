![image](https://user-images.githubusercontent.com/47895671/183772428-71ee41ec-d5dc-4219-90a9-f91f83a3dd1b.png)


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
template: Compact

# color in hex: rrggbb
primary color: 008080


full name: Mohamed Wafy


job title: Frontend Developer


summary: |
  Frontend Developer, Backend Developer, and Computer Science student with experince with frontend and backend technologies, cloud, linux and teamwork.

links:
  - Portfolio: https://mowafy001.github.io/portfolio/
  - GitHub: https://github.com/MoWafy001
  - LinkedIn: https://linkedin.com/in/mohamedwafy
  - wafy123445@gmail.com: mailto:wafy123445@gmail.com
  - "+201127813978": tel:+201127813978


not_links:
  - Egypt
  - Egypt | Alex
  - Egypt | Cairo


skills:
  - React
  - SASS
  - Bootstrap
  - NodeJS
  - GitHub
  - Linux
  - Cloud
  - Googling
  - CSS
  - JavaScript
  - Python
  - PHP


experience:
  - Intern Backend Developer, Airdonex:
    - Sep 2021 - Dec 2021
    - |
      - Created RESTful APIs
      - Created a login system
      - Managed a PostgreSQL Database

      Highlighted skills: Django - PostgreSQL

  - Fullstack Developer, freelance:
    - Mar 2021 - May 2021
    - |
      - Created a Speech-To-Text API
      - Another API to convert file formats
      - Created a Systemd service to automate
      - processes on a Linux server
      - Created a flask app to render DZI images

      Highlighted skills: Linux - Flask - Python - API Development

  - Member of The Google Developer Student Club - GDSC Damanhour University:
    - Aug 2021 - Jun 2022
    - |
      - Teaching fellow students coding, Node JS in particular.
      - Creating a course and find materials.
      - Giving online session, and doing projects.

      Highlighted skills: Team Work - NodeJS



education:
  - React Developement Cross-Skilling Nanodegree, Udacity:
    - "2022"
    - |
      Highlighted skills:
      ReactJS
      Redux

  - Advanced Web Development Nano Degree, Udacity:
    - "2021"
    - |
      Highlighted skills:
      Flask
      API Development
      Backend Developement
      Model View Controller Model

  - Web Development Professional Nano Degree, Udacity:
    - "2020"
    - |
      Highlighted skills:
      NodeJS
      Building responsive pages
      Integrating APIs

  - Intermediate Python, DataCamp:
    - "2022"
    - |
      Highlighted skills:
      Python
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
