# Server Log Analyzer

A beginner-friendly Python project that analyzes server log files and
generates a summary report of log levels and common HTTP error codes.

## Features

- Counts non-empty log entries.
- Counts INFO, WARNING, ERROR, and CRITICAL log levels.
- Counts HTTP 404 and 500 codes in ERROR entries.
- Collects and displays CRITICAL messages.
- Prints a summary report in the terminal.
- Saves the report to `report.txt`.

## Requirements

- Python 3
- No third-party Python packages required

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run:

   ```bash
   python analyzer.py


## Example Output
```
========================================
    SERVER LOG ANALYSIS REPORT
========================================
Total Logs : 9
INFO : 3
WARNING : 1
ERROR : 3
404 Errors : 2
500 Errors : 1
CRITICAL : 2

Critical Messages:
- CRITICAL Database Connection Lost
- CRITICAL Disk Full
```

## Log Format

Each line must start with the log level, followed by the message:

```
ERROR 404 Page Not Found
```
