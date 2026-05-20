from pathlib import Path

import PyPDF2


# =========================================================
# TXT EXTRACTION
# =========================================================

def extract_text_from_txt(
    file_path: str
) -> str:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# =========================================================
# PDF EXTRACTION
# =========================================================

def extract_text_from_pdf(
    file_path: str
) -> str:

    extracted_text = ""

    with open(file_path, "rb") as file:

        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

    return extracted_text


# =========================================================
# UNIVERSAL EXTRACTION
# =========================================================

def extract_document_text(
    file_path: str
) -> str:

    path = Path(file_path)

    extension = path.suffix.lower()

    # TXT
    if extension == ".txt":

        return extract_text_from_txt(
            file_path
        )

    # PDF
    elif extension == ".pdf":

        return extract_text_from_pdf(
            file_path
        )

    else:

        raise ValueError(
            f"Unsupported file type: {extension}"
        )