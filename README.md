\# 📊 Command-Line Data Analysis Tool



A Python-based command-line data analysis tool developed as part of \*\*VEDA Technology Level 2 – Task 30\*\*.



The application allows users to analyze CSV datasets directly from the terminal using \*\*Python, Pandas, and argparse\*\*.



\---



\## 🚀 Features



\- 📂 Load any CSV file through a command-line argument

\- 📋 Display dataset summary

\- 🔍 Inspect columns and data types

\- ⚠️ Detect missing values

\- 🔎 Filter records using comparison operators

\- 📊 Group data by selected columns

\- 📈 Calculate numeric averages

\- 📉 Generate descriptive statistics

\- ✅ Validate requested columns

\- 🛡️ Handle invalid files and input values

\- 💻 Built-in command-line help

\- 🔄 Reusable with different CSV datasets

\- 🚫 No hardcoded input filename



\---



\## 🛠️ Technologies Used



\- \*\*Python\*\*

\- \*\*Pandas\*\*

\- \*\*argparse\*\*

\- \*\*CSV\*\*

\- \*\*Git\*\*

\- \*\*GitHub\*\*

\- \*\*PowerShell\*\*



\---



\## 📁 Project Structure



```text

task30-cli-data-analysis-tool/

│

├── data/

│   └── sample\_data.csv

│

├── cli\_tool.py

├── README.md

├── requirements.txt

├── sample\_output.txt

├── .gitignore

└── venv/

⚙️ Installation



Clone the repository:



git clone https://github.com/Mahima2005-shetty/task30-cli-data-analysis-tool.git



Navigate to the project:



cd task30-cli-data-analysis-tool



Create a virtual environment:



python -m venv venv



Activate it:



.\\venv\\Scripts\\Activate.ps1



Install dependencies:



pip install -r requirements.txt

▶️ Usage

1\. Display Help

python cli\_tool.py --help

2\. Display Dataset Summary

python cli\_tool.py --file data/sample\_data.csv --summary



The summary displays:



Number of rows

Number of columns

Column names

Data types

Missing values

3\. Filter Data



Example: Find employees with salary greater than 70,000.



python cli\_tool.py --file data/sample\_data.csv --filter-column salary --operator ">" --value 70000



Supported operators:



>

<

>=

<=

==

!=

4\. Group Data



Group employees by department:



python cli\_tool.py --file data/sample\_data.csv --group department



The tool displays:



Record count for each group

Numeric averages for each group

5\. Generate Statistical Report

python cli\_tool.py --file data/sample\_data.csv --stats



The report includes:



Count

Mean

Standard deviation

Minimum

25th percentile

Median

75th percentile

Maximum

6\. Run Multiple Analyses

python cli\_tool.py --file data/sample\_data.csv --summary --group department --stats

📊 Sample Dataset



The included dataset contains employee information with the following fields:



Column	Description

employee\_id	Unique employee identifier

name	Employee name

department	Employee department

experience\_years	Years of experience

salary	Employee salary

sales	Sales amount



The sample dataset contains 15 records and 6 columns.



📈 Sample Results



The tool successfully analyzed the sample dataset.



Dataset Summary

Rows    : 15

Columns : 6

Missing Values: 0

Department Record Counts

Finance    3

HR         3

IT         5

Sales      4

Overall Statistics

Average Experience : 4.40 years

Average Salary     : 64666.67

Average Sales      : 162666.67

🛡️ Error Handling



The application handles common input errors including:



File not found

Empty CSV files

Invalid CSV format

Missing columns

Invalid filter values

Incomplete filter arguments

Empty datasets

🧪 Testing



The following features were tested:



Feature	Status

CLI Help	✅ Passed

CSV Loading	✅ Passed

Dataset Summary	✅ Passed

Missing Value Detection	✅ Passed

Data Filtering	✅ Passed

Grouping	✅ Passed

Numeric Averages	✅ Passed

Statistical Analysis	✅ Passed

Error Handling	✅ Passed

Combined Analysis	✅ Passed

🎯 Learning Outcomes



This project provided practical experience in:



Python command-line application development

argparse

Pandas data analysis

CSV processing

Data filtering

Data grouping

Descriptive statistics

Input validation

Exception handling

Git and GitHub workflow

👩‍💻 Author



Mahima M.



Information Science Engineering Student

The Oxford College of Engineering, Bengaluru



🏆 VEDA Technology



Developed as part of the VEDA Technology Level 2 Internship – Task 30.



🔗 Repository



GitHub Repository



