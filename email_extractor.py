"""CodeAlpha Python Internship - Task 3: Task Automation
Extracts all email addresses from a .txt file and saves them to another file."""
import re
import sys

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # unique emails, original order preserved
    emails = list(dict.fromkeys(re.findall(EMAIL_PATTERN, text)))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique email(s). Saved to '{output_file}'.")
    return emails


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "sample_input.txt"
    dst = sys.argv[2] if len(sys.argv) > 2 else "extracted_emails.txt"
    try:
        extract_emails(src, dst)
    except FileNotFoundError:
        print(f"Error: '{src}' not found.")
