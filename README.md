# Server Log Analyzer

A small Python command-line tool that reads an application log file, counts recognized log levels and HTTP status-code tokens, and prints and saves a summary report.

## Features

- Counts non-empty log lines.
- Recognizes `INFO`, `WARNING`, `ERROR`, and `CRITICAL` near the beginning of a line, including after common timestamp prefixes.
- Counts 4xx and 5xx status-code tokens found in `ERROR` log messages.
- Reports individual HTTP status codes, such as `404` and `500`.
- Lists `CRITICAL` messages.
- Uses the same generated report text for the terminal and `report.txt`.
- Handles a missing input file without generating a new report.

## Requirements

- Python 3
- No third-party Python packages

## Run the analyzer

Run the included sample file (used by default):

```powershell
python analyzer.py
```

Choose a different input file:

```powershell
python analyzer.py my.log
```

You can also provide a relative or absolute path:

```powershell
python analyzer.py logs/server.log
```

If no filename is supplied, the program uses `sample.log`. The report is saved to `report.txt` in the current working directory.

## Example output

For the included `sample.log`, the report should contain:

```text
========================================
    SERVER LOG ANALYSIS REPORT
========================================
Total Logs : 9
INFO : 3
WARNING : 1
ERROR : 3
4xx Errors : 2
5xx Errors : 1
404 Errors : 2
500 Errors : 1
CRITICAL : 2

HTTP Status Code Breakdown:
- 404: 2
- 500: 1

Critical Messages:
- CRITICAL Database Connection Lost
- CRITICAL Disk Full
```

## How status codes are counted

The analyzer searches for the log severity near the start of each non-empty line. For lines classified as `ERROR`, it checks the first token immediately after the severity label for a three-digit status code from `400` through `599`. It reports aggregate 4xx and 5xx counts, along with counts for each recognized status code.

## Limitations

- This is a learning project, not a universal parser for every server-log format.
- Severity detection searches the first eight whitespace-separated tokens, so unusual log formats may not be recognized correctly.
- HTTP status-code counting currently applies to `ERROR` messages, not every possible access-log format.
- Status-code detection checks only the first token after `ERROR`; codes appearing later in a message are ignored to avoid false matches.
- The output path is currently fixed to `report.txt`; a custom `--output` option is not implemented.

## Future improvements

- Add a command-line option for choosing the report output path.
- Add automated tests for timestamped logs, blank lines, missing files, and status-code parsing.
- Add dedicated parsers for common HTTP access logs and structured JSON logs.
