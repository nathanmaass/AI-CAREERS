# Audit Confirmation Drafting Assistant
# Collects user input and generates a draft confirmation letter.
# The script is written for beginners and includes comments for clarity.

import textwrap
from datetime import datetime

try:
    from docx import Document
except ImportError:
    Document = None


def collect_input():
    """Prompt the user for all required fields and return them as a dictionary."""
    data = {}
    data["confirmation_type"] = input("Type of confirmation (Bank, Legal, Accounts Receivable, etc.): ")
    data["auditor_firm"] = input("Auditor's firm name: ")
    data["client_name"] = input("Audit client name: ")
    data["contact_person"] = input("Contact person at the confirming party: ")
    data["contact_info"] = input("Contact information (address, email, phone): ")
    data["request_details"] = input("Specific request details (e.g., balance confirmation, contingent liabilities): ")
    date_str = input("Confirmation date (YYYY-MM-DD, leave blank for today): ")
    data["confirmation_date"] = date_str or datetime.today().strftime("%Y-%m-%d")
    data["additional_notes"] = input("Additional notes or disclosures (optional): ")
    return data


def generate_letter(data):
    """Generate a formatted confirmation letter based on user input."""
    template = f"""
{data['confirmation_date']}

{data['contact_person']}
{data['contact_info']}

Subject: {data['confirmation_type']} Confirmation Request

Dear {data['contact_person']},

We are the auditors for {data['client_name']}. As part of our audit procedures, we are requesting confirmation of the following information:

{data['request_details']}

Please provide the requested information at your earliest convenience. If you have any questions, feel free to contact us.

Sincerely,
{data['auditor_firm']}
"""
    if data["additional_notes"]:
        template += f"\nAdditional Notes:\n{data['additional_notes']}\n"
    # Wrap the text to keep it readable when displayed in the terminal
    return textwrap.dedent(template).strip()


def save_to_txt(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved draft to {filename}")


def save_to_docx(text, filename):
    if Document is None:
        print("python-docx is not installed. Please run 'pip install python-docx' to save as .docx")
        return
    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(filename)
    print(f"Saved draft to {filename}")


def main():
    data = collect_input()
    letter = generate_letter(data)
    print("\nGenerated Confirmation Letter:\n")
    print(letter)

    print("\nWould you like to save the letter?")
    print("1 - Save as .txt")
    print("2 - Save as .docx")
    print("3 - Do not save")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        filename = input("Enter filename (e.g., confirmation.txt): ")
        if not filename:
            filename = "confirmation.txt"
        save_to_txt(letter, filename)
    elif choice == "2":
        filename = input("Enter filename (e.g., confirmation.docx): ")
        if not filename:
            filename = "confirmation.docx"
        save_to_docx(letter, filename)
    else:
        print("Letter not saved.")


if __name__ == "__main__":
    main()
