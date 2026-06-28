\# Mutual Fund Analysis Project



\## Day 1: Data Ingestion



\### Completed Tasks



\- Created project folder structure

\- Loaded mutual fund CSV datasets using Pandas

\- Checked:

&#x20; - Shape

&#x20; - Data types

&#x20; - First 5 rows

&#x20; - Missing values



\- Fetched live NAV data using mfapi.in API



Funds included:



\- HDFC Top 100 Direct

\- SBI Bluechip

\- ICICI Bluechip

\- Nippon Large Cap

\- Axis Bluechip

\- Kotak Bluechip



\### Tools Used



\- Python

\- Pandas

\- NumPy

\- Requests

\- Jupyter Notebook

\- Git \& GitHub





\## Day 2: Data Cleaning \& Exploratory Data Analysis (EDA)



\### Overview

In Day 2 of the project, the focus was on preparing raw mutual fund datasets for analysis and performing Exploratory Data Analysis (EDA). The raw CSV files were cleaned, validated, and transformed into structured datasets suitable for visualization and insights generation.



\### Tasks Completed



\### 1. Data Cleaning



\#### NAV History Dataset

\- Converted date columns into proper datetime format

\- Sorted data by scheme code and date

\- Removed duplicate records

\- Handled missing NAV values using forward filling for non-trading days

\- Validated that all NAV values are positive

\- Created cleaned NAV dataset for analysis



\#### Transaction Dataset

\- Standardized transaction types:

&#x20; - SIP

&#x20; - Lumpsum

&#x20; - Redemption

\- Converted transaction dates into correct format

\- Validated transaction amounts

\- Checked KYC status consistency

\- Removed invalid records



\#### Performance Dataset

\- Cleaned scheme performance data

\- Verified return-related columns

\- Prepared dataset for fund performance comparison



\---



\## 2. Exploratory Data Analysis (EDA)



Performed analysis to understand mutual fund trends and investor behavior.



\### NAV Trend Analysis

\- Analyzed daily NAV movement across mutual fund schemes

\- Created time-series visualizations to identify:

&#x20; - Growth periods

&#x20; - Market corrections

&#x20; - Long-term performance trends



\### Expense Ratio Analysis

\- Compared expense ratios across schemes

\- Identified cost differences between funds

\- Studied relationship between fund cost and performance



\### Investor Transaction Analysis

Analyzed:

\- SIP vs Lumpsum vs Redemption distribution

\- Investment amount patterns

\- Investor activity trends



\---



\## 3. Data Visualizations Created



Visual analysis was performed using:



\- Matplotlib

\- Seaborn

\- Plotly



Created charts including:

\- NAV growth trends

\- Expense ratio comparison

\- Transaction distribution charts

\- Performance comparison plots



\---



\## Tools \& Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Plotly

\- Jupyter Notebook



\---



\## Project Progress



✅ Raw data loading

✅ Data cleaning pipeline

✅ Data validation

✅ Exploratory Data Analysis

✅ Visualization preparation



Next Steps:

\- Build final insights dashboard

\- Generate investment recommendations

\- Deploy analysis results





\# Mutual Fund Analysis - EDA Project



\## Project Overview



This project performs Exploratory Data Analysis (EDA) on mutual fund data.



The objective is to analyze:



\- NAV movement

\- Fund performance

\- Investor transactions

\- Expense ratios

\- Scheme-level investment behavior





\## Dataset



The project uses cleaned CSV datasets:



\### NAV History



Columns:



\- scheme\_code

\- date

\- nav





\### Performance



Columns:



\- scheme\_code

\- expense\_ratio





\### Transactions



Columns:



\- transaction\_id

\- scheme\_code

\- transaction\_type

\- amount

\- date





\## Tools Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Plotly

\- Jupyter Notebook





\## EDA Analysis Performed





\### 1. NAV Trend Analysis



Analyzed daily NAV movement across mutual fund schemes.





\### 2. NAV Return Correlation



Calculated daily returns and visualized correlation between schemes.





\### 3. Transaction Analysis



Analyzed:



\- Buy transactions

\- Sell transactions

\- Scheme-wise investment amounts





\### 4. Monthly Transaction Trend



Studied investment activity over time.





\### 5. Expense Ratio Analysis



Compared expense ratios across schemes.





\## Project Structure







\## Key Findings



\- NAV values show daily movement across schemes.

\- Return analysis helps understand fund volatility.

\- Transaction patterns show investor activity.

\- Expense ratios vary across schemes.

\- Combined analysis provides fund behavior insights.





\## Author



VARAN SINGH SODHI



\## Visualizations





\### NAV Trend



!\[NAV Trend](screenshots/nav\_trend.png)





\### Correlation Heatmap



!\[Correlation](screenshots/nav\_correlation.png)





\### Expense Ratio



!\[Expense Ratio](screenshots/expense\_ratio.png)





\### Transaction Analysis



!\[Transactions](screenshots/transaction\_type.png)





\# Mutual Fund Analysis



\## Objective



Analyze 40 mutual funds using NAV history and performance metrics.



\## Analysis



\- Data Cleaning

\- Exploratory Data Analysis

\- NAV Trend Analysis

\- Daily Returns

\- CAGR Analysis

\- Sharpe Ratio

\- Sortino Ratio

\- Alpha Beta Regression

\- Maximum Drawdown

\- Fund Ranking Scorecard

\- Benchmark Comparison



\## Metrics



\- CAGR

\- Risk Adjusted Returns

\- Market Sensitivity

\- Drawdown Risk



\## Tools



Python

Pandas

NumPy

Matplotlib

SciPy



\## Outputs



\- fund\_scorecard.csv

\- alpha\_beta.csv

\- benchmark\_comparison.png





