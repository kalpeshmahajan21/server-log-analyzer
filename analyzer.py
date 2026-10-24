def analyze_logs(file_path):

    counts = {
        "total": 0,
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0,
        "404": 0,
        "500": 0,
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
                
                level = parts[0]



                if level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
                    counts[level] += 1



                if level == "ERROR":

                    if "404" in parts[1:]:
                        counts["404"] += 1

                    if "500" in parts[1:]:
                        counts["500"] += 1

                if level == "CRITICAL":
                    counts["critical_messages"].append(line)

    except FileNotFoundError:
        print(f"Error: {file_path} was not found.")
        return None

    return counts


# PRINT HEADER


def print_header():

    print("=" * 40)
    print("    SERVER LOG ANALYSIS REPORT")
    print("=" * 40)


# PRINT REPORT

def print_report(counts):
    print_header()

    print(f"Total Logs : {counts['total']}")

    print(f"INFO : {counts['INFO']}")

    print(f"WARNING : {counts['WARNING']}")

    print(f"ERROR : {counts['ERROR']}")

    print(f"404 Errors : {counts['404']}")

    print(f"500 Errors : {counts['500']}")

    print(f"CRITICAL : {counts['CRITICAL']}")


    print("\nCritical Messages:")


    for message in counts["critical_messages"]:
        print(f"- {message}")


# SAVE REPORT


def save_report(counts):
    with open("report.txt", "w") as file:

        file.write("SERVER LOG ANALYSIS REPORT\n")

        file.write("=" * 40 + "\n")

        file.write(f"Total Logs : {counts['total']}\n")

        file.write(f"INFO : {counts['INFO']}\n")

        file.write(f"WARNING : {counts['WARNING']}\n")

        file.write(f"ERROR : {counts['ERROR']}\n")

        file.write(f"404 Errors : {counts['404']}\n")

        file.write(f"500 Errors : {counts['500']}\n")

        file.write(f"CRITICAL : {counts['CRITICAL']}\n")

        file.write("\nCritical Messages:\n")

        for message in counts["critical_messages"]:
            file.write(f" - {message}\n")

# MAIN PROGRAM
if __name__ == "__main__":
    counts = analyze_logs("sample.log")
    if counts is None:
        raise SystemExit(1)

    print_report(counts)
    save_report(counts)
