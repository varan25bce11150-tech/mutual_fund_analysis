CREATE TABLE dim_fund(

fund_id INTEGER PRIMARY KEY,
fund_name TEXT,
amfi_code INTEGER

);


CREATE TABLE dim_date(

date_id INTEGER PRIMARY KEY,
date DATE,
year INTEGER,
month INTEGER

);



CREATE TABLE fact_nav(

id INTEGER PRIMARY KEY,
fund_id INTEGER,
date_id INTEGER,
nav REAL

);



CREATE TABLE fact_transactions(

transaction_id INTEGER PRIMARY KEY,
fund_id INTEGER,
amount REAL,
transaction_type TEXT

);



CREATE TABLE fact_performance(

id INTEGER PRIMARY KEY,
fund_id INTEGER,
return_value REAL,
expense_ratio REAL

);



CREATE TABLE fact_aum(

id INTEGER PRIMARY KEY,
fund_id INTEGER,
aum REAL

);