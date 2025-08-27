# document_loader.py
from PyPDF2 import PdfReader

class DocumentLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        reader = PdfReader(self.filepath)
        text = "\n".join((page.extract_text() or "") for page in reader.pages)

        entries = text.strip().split("Title:")
        books = []
        for entry in entries[1:]:
            lines = entry.strip().splitlines()
            title = lines[0].strip()
            summary = " ".join(lines[1:-1]).strip()
            themes_line = lines[-1].strip().replace("Themes:", "")
            raw = [t.strip() for t in themes_line.split(",") if t.strip()]
            themes = [t.rstrip(".,;:!?") for t in raw]
            books.append({"title": title, "summary": summary, "themes": themes})
        return books
