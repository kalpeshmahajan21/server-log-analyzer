import argparse

def analyze_logs(file_path):

    counts = {
        "total": 0,
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0,
        "4xx": 0,
        "5xx": 0,
        "http_status_codes": {},
        "critical_messages": []
    }


    try:

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()


                if not line:
                    continue


                counts["total"] += 1

                parts = line.split()

                # Find the severity label near the start of the line.
                # This supports lines with timestamps before the log level.
                levels = ("INFO", "WARNING", "ERROR", "CRITICAL")
                level_index = next(
                    (index for index, part in enumerate(parts[:8]) if part in levels),
                    None
                )

                level = parts[level_index] if level_index is not None else None


                if level in levels:
                    counts[level] += 1



                if level == "ERROR":
                    message_parts = parts[level_index + 1:]

                    for token in message_parts[:1]:
                        token = token.strip(".,:;()[]{}")

                        if len(token) != 3 or not token.isdigit():
                            continue

                        status_code = int(token)

                        if 400 <= status_code <= 499:
                            counts["4xx"] += 1
                        elif 500 <= status_code <= 599:
                            counts["5xx"] += 1
                        else:
                            continue

                        code_text = str(status_code)
                        status_counts = counts["http_status_codes"]
                        status_counts[code_text] = (
                            status_counts.get(code_text, 0) + 1
                        )


                if level == "CRITICAL":
                    counts["critical_messages"].append(line)


    except FileNotFoundError:
        print(f"Error: {file_path} was not found.")
        return None

    return counts




# BUILD REPORT

def build_report(counts):
    lines = [
        "=" * 40,
        "    SERVER LOG ANALYSIS REPORT",
        "=" * 40,
        f"Total Logs : {counts['total']}",
        f"INFO : {counts['INFO']}",
        f"WARNING : {counts['WARNING']}",
        f"ERROR : {counts['ERROR']}",
        f"4xx Errors : {counts['4xx']}",
        f"5xx Errors : {counts['5xx']}",
        f"404 Errors : {counts['http_status_codes'].get('404', 0)}",
        f"500 Errors : {counts['http_status_codes'].get('500', 0)}",
        f"CRITICAL : {counts['CRITICAL']}",
        "",
        "HTTP Status Code Breakdown:",
    ]

    for code, amount in sorted(counts["http_status_codes"].items()):
        lines.append(f"- {code}: {amount}")

    lines.extend(["", "Critical Messages:"])

    for message in counts["critical_messages"]:
        lines.append(f"- {message}")

    return "\n".join(lines)


# PRINT REPORT

def print_report(report_text):
    print(report_text)


# SAVE REPORT

def save_report(report_text):
    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report_text + "\n")


# MAIN PROGRAM
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze a server log file."
    )
    parser.add_argument(
        "log_file",
        nargs="?",
        default="sample.log",
        help="Path to the log file (default: sample.log)",
    )

    args = parser.parse_args()
    counts = analyze_logs(args.log_file)

    if counts is None:
        raise SystemExit(1)

    report_text = build_report(counts)

    print_report(report_text)
    save_report(report_text)