import csv

def find_min_max_loan_amount(csv_path):
    """
    Reads the CSV file and prints the minimum and maximum loan_amnt values.
    Handles $ signs, commas, blank values, and text issues.
    """
    loan_values = []

    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            print("Headers:", reader.fieldnames)

            if not reader.fieldnames:
                print("CSV appears to be empty or missing a header.")
                return

            colname = "loan_amnt"  # confirmed from your headers

            for row in reader:
                raw = (row.get(colname) or "").strip()
                if not raw or raw.lower() in {"na", "n/a", "null", "none", "nan"}:
                    continue

                # remove $, commas, and random spaces
                cleaned = raw.replace(",", "").replace("$", "").strip()

                # only keep digits or decimals
                cleaned = ''.join(c for c in cleaned if (c.isdigit() or c == '.'))

                if cleaned == "":
                    continue

                try:
                    val = float(cleaned)
                    loan_values.append(val)
                except ValueError:
                    continue

    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if not loan_values:
        print("No valid loan_amnt values found. Check column formatting.")
        return

    min_val = min(loan_values)
    max_val = max(loan_values)

    print("\n✅ RESULTS:")
    print(f"Min loan_amnt: {int(min_val) if min_val.is_integer() else min_val}")
    print(f"Max loan_amnt: {int(max_val) if max_val.is_integer() else max_val}")

if __name__ == "__main__":
    find_min_max_loan_amount(
        r"C:\Users\henry\OneDrive\INFO INFRAS\User-defined Functions\LoansDataset.csv"
    )
