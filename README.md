# CS166 Team11 Final Project 

This repository contains two Python scripts that were utilized to perform data wrangling on the result data obtained from a Honeypot.


## trackingSourceIP.py

The code reads a JSON file containing session data, groups the data by the 'source_ip' column, calculates the count of attacks for each source IP, sorts the results in descending order, selects the top 5 rows, and finally prints the source IP and its corresponding attack count.

```bash
python3 trackingSourceIP.py
```


## wrangleData.py

The code reads a JSON file containing session data, groups the data by various columns, sorts it by attack count, adds a column to display the count, and finally prints the sorted results.

```bash
python3 wrangleData.py
```
