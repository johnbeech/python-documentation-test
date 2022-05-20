from markdown_toolkit import MarkdownDocument

doc = MarkdownDocument()

with doc.heading("Title"):
    doc.paragraph("Example Paragraph.")

print(doc.render())
