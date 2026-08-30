from pypdf import PdfReader
import re
import os



def extract_text_from_pdf(file_path):
    text = ""

    try:
        reader = PdfReader(file_path)

        print(f"PDF found successfully!")
        print(f"Number of pages: {len(reader.pages)}")

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"
            else:
                print(f"Warning: No text found on page {page_number}")

        return text

    except FileNotFoundError:
        print("ERROR: resume.pdf was not found!")
        return ""

    except Exception as e:
        print("ERROR:", e)
        return ""


def clean_text(text):
    # Convert everything to lowercase
    text = text.lower()

    # Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end
    text = text.strip()

    return text


# --------------------------------
# MAIN PROGRAM
# --------------------------------

print("================================")
print("   AI RESUME ANALYZER")
print("================================")

# Check current folder
print("Current folder:")
print(os.getcwd())

# Check whether PDF exists
if not os.path.exists("resume.pdf"):
    print("\nERROR: resume.pdf does not exist in this folder.")
    print("Please put resume.pdf in the same folder as App.py")
else:
    print("\nresume.pdf found!")

    # Extract text
    resume_text = extract_text_from_pdf("resume.pdf")

    print("\n--- RAW TEXT ---")
    print(resume_text)

    # Clean text
    cleaned_text = clean_text(resume_text)

    print("\n--- CLEANED TEXT ---")
    print(cleaned_text)

    print("\n================================")
    print("PDF PROCESSING COMPLETED")
    print("================================")