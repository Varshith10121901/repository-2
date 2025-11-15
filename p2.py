from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

# Output path
output_path = "/home/kali/Downloads/ReportLab_Story_225pages.pdf"

# Create canvas
pdf = canvas.Canvas(output_path, pagesize=A4)

# Attractive story paragraph
story_text = """
Once upon a time in a quiet village surrounded by silver-lined mountains,
there lived a curious young explorer named Arion. Unlike others, he believed
that the universe whispered secrets only a brave heart could hear.

Night after night, Arion would sit beneath the glowing sky, watching the stars.
But one evening, everything changed. A streak of brilliant violet light cut
across the heavens, falling behind the mountains with an echo that only he heard.

Following that light led Arion to a shimmering portal of cosmic colors—opening
the path to worlds untouched by time, filled with creatures sculpted from
stardust, ancient guardians, and civilizations living in harmony with the universe.

And so began Arion’s greatest adventure...
"""

# Repeat the story for long content
story_full = story_text * 50  # one page ≈ 1 full story block

# Page formatting
width, height = A4
left_margin = 60
top_margin = height - 60
line_height = 18

# Set fonts
pdf.setFont("Helvetica-Bold", 22)
pdf.drawString(left_margin, top_margin, "✨ The Chronicles of Arion ✨")

pdf.setFont("Helvetica", 14)

# Starting position for text
y = top_margin - 40

# Split into lines
lines = story_full.split("\n")

page_count = 1
target_pages = 225

for page in range(target_pages):
    
    if page > 0:
        pdf.setFont("Helvetica-Bold", 22)
        pdf.drawString(left_margin, top_margin, f"✨ The Chronicles of Arion (Page {page+1}) ✨")
        pdf.setFont("Helvetica", 14)
        y = top_margin - 40

    for i in range(35):  # approx lines per page
        # If story ends, we still continue filling until 225 pages
        text = lines[(page * 35 + i) % len(lines)]
        pdf.drawString(left_margin, y, text)
        y -= line_height

    pdf.showPage()  # create next page

# Save PDF
pdf.save()
print("PDF generated successfully at:", output_path)
