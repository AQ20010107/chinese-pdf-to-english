---
name: chinese-pdf-to-english
description: Translate complete Chinese PDF documents into polished English PDF deliverables while preserving report structure, tables, images, captions, page numbering, and disclaimers. Use when a user asks to translate a Chinese PDF, Chinese inspection report, test certificate, technical document, or scanned/text-encoded Chinese PDF into English and wants a new PDF file.
---

# Chinese PDF to English

Create a complete English PDF from a Chinese PDF. Treat this as a document-production task, not just text extraction.

## Workflow

1. Locate the input PDF and determine its page count, text layer quality, page dimensions, and whether it contains tables, photographs, diagrams, or scanned pages.
2. Render the source pages to PNG before translating. Prefer the bundled Poppler `pdftoppm`; use `scripts/render_pdf.py` when the runtime path is inconvenient. Visually inspect representative pages so corrupted font encoding is not mistaken for missing content.
3. Extract text with `pdfplumber` or `pypdf` as a draft only. If extracted Chinese is garbled, translate from the rendered page images and use OCR or visual reading as needed. Never deliver garbled extracted text.
4. Translate every user-visible item, including titles, labels, table headers and cells, photo captions, footnotes, signatures, warnings, disclaimers, contact information, and end markers. Preserve identifiers, model numbers, dates, units, standards, URLs, email addresses, and pass/fail results exactly unless translation is explicitly requested for those values.
5. Rebuild the document as a new PDF using `reportlab` (or another reliable PDF generator). Use English-capable fonts, wrapped table cells, consistent margins, explicit page breaks, and readable captions. Preserve source photos and diagrams where they carry evidence. Do not overlay English on top of unreadable or still-visible Chinese labels; crop/rebuild captions when necessary.
6. Keep the same logical page order and approximately the same hierarchy. If exact layout cannot be preserved, prioritize complete content, legibility, and faithful grouping over pixel-level imitation.
7. Render the newly generated PDF and inspect every page. Check for clipped text, table overflow, overlapping content, missing images, residual Chinese labels, broken glyphs, incorrect page numbering, and empty or duplicated sections. Iterate until the final render is clean.
8. Save only the final user-facing PDF in the designated output folder and report its path. Keep source files unchanged. Mention if the result is a translation/reconstruction and not an officially certified translation.

## Technical defaults

- Use `pdfplumber`/`pypdf` for inspection and `reportlab` for generation.
- Use ASCII hyphens in generated text unless the source requires a specific symbol; preserve technical notation such as `IP65`, `EN 60529:1991+A1:2000+A2:2013`, `°C`, `RH`, and `±` accurately.
- For tables, convert long strings into wrapped `Paragraph` cells rather than raw strings.
- When reusing source photographs, crop out source-language captions and add translated captions in the rebuilt PDF.
- Include a final visual QA pass after every meaningful layout change.

## Reusable helper

Use `scripts/render_pdf.py` to render all pages of a PDF to PNGs for visual QA. It accepts an input PDF and an output directory and uses the bundled Poppler runtime when available.
