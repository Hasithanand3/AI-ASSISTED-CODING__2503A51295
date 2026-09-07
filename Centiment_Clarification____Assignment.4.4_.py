from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, HRFlowable
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
import os, re

out = "/mnt/data/Prompt_Engineering_Lab_Assignment.pdf"

# Register a broadly available Unicode font if present.
font_regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if os.path.exists(font_regular):
    pdfmetrics.registerFont(TTFont("DV", font_regular))
    pdfmetrics.registerFont(TTFont("DVB", font_bold))
    BASE, BOLD = "DV", "DVB"
else:
    BASE, BOLD = "Helvetica", "Helvetica-Bold"

NAVY = HexColor("#17365D")
BLUE = HexColor("#2F75B5")
TEAL = HexColor("#0F766E")
LIGHT_BLUE = HexColor("#EAF3FA")
LIGHT_TEAL = HexColor("#E8F5F3")
LIGHT_GOLD = HexColor("#FFF6D8")
DARK = HexColor("#243447")
GRAY = HexColor("#667085")
WHITE = colors.white

styles = getSampleStyleSheet()
title = ParagraphStyle("title", fontName=BOLD, fontSize=22, leading=27, textColor=NAVY,
                       alignment=TA_CENTER, spaceAfter=10)
subtitle = ParagraphStyle("subtitle", fontName=BASE, fontSize=10.5, leading=15,
                          textColor=GRAY, alignment=TA_CENTER)
h1 = ParagraphStyle("h1", fontName=BOLD, fontSize=16, leading=20, textColor=WHITE,
                    spaceBefore=4, spaceAfter=8)
h2 = ParagraphStyle("h2", fontName=BOLD, fontSize=12.5, leading=16, textColor=NAVY,
                    spaceBefore=8, spaceAfter=5)
body = ParagraphStyle("body", fontName=BASE, fontSize=9.4, leading=14,
                      textColor=DARK, spaceAfter=6)
small = ParagraphStyle("small", fontName=BASE, fontSize=8.4, leading=12,
                       textColor=DARK)
prompt = ParagraphStyle("prompt", fontName=BASE, fontSize=8.8, leading=13,
                        textColor=DARK)
output = ParagraphStyle("output", fontName=BOLD, fontSize=9.2, leading=13,
                        textColor=TEAL)
cover_meta = ParagraphStyle("cover_meta", fontName=BASE, fontSize=10, leading=17,
                            textColor=DARK, alignment=TA_CENTER)

doc = SimpleDocTemplate(
    out, pagesize=A4, rightMargin=16*mm, leftMargin=16*mm,
    topMargin=17*mm, bottomMargin=17*mm
)

story = []

def P(text, style=body):
    return Paragraph(text, style)

def section_bar(text):
    t = Table([[P(text, h1)]], colWidths=[178*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("LEFTPADDING", (0,0), (-1,-1), 9),
        ("RIGHTPADDING", (0,0), (-1,-1), 9),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("BOX", (0,0), (-1,-1), 0.5, NAVY),
    ]))
    return t

def info_box(label, text, bg=LIGHT_BLUE):
    t = Table([[P(f"<b>{label}</b>", small), P(text, small)]],
              colWidths=[30*mm, 148*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.6, BLUE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

def data_table(headers, rows, widths):
    data = [[P(f"<b>{x}</b>", small) for x in headers]]
    for row in rows:
        data.append([P(str(x), small) for x in row])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLUE),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("GRID", (0,0), (-1,-1), 0.45, HexColor("#B8C4D0")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_BLUE]),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    return t

def prompt_box(label, text, bg=LIGHT_TEAL, border=TEAL):
    t = Table([[P(f"<b>{label}</b>", small)], [P(text, prompt)]], colWidths=[178*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.7, border),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

def add_question(num, title_text, scenario, input_headers, input_rows,
                 zero_input, zero_output, one_example, one_input, one_output,
                 few_examples, few_input, few_output, comparison,
                 observation, conclusion):
    story.append(section_bar(f"Q{num}. {title_text}"))
    story.append(Spacer(1, 4))
    story.append(P("<b>Scenario</b>", h2))
    story.append(P(scenario))
    story.append(P("<b>Input</b>", h2))
    story.append(data_table(input_headers, input_rows, [12*mm, 105*mm, 61*mm]))
    story.append(Spacer(1, 7))

    story.append(P("Zero-Shot Prompting", h2))
    story.append(prompt_box("PROMPT", zero_input))
    story.append(Spacer(1, 4))
    story.append(info_box("Input", zero_input.split("\n")[-1] if "\n" in zero_input else zero_input, LIGHT_GOLD))
    story.append(Spacer(1, 3))
    story.append(info_box("Output", zero_output, LIGHT_TEAL))

    story.append(P("One-Shot Prompting", h2))
    story.append(prompt_box("PROMPT + EXAMPLE", one_example))
    story.append(Spacer(1, 3))
    story.append(info_box("Input", one_input, LIGHT_GOLD))
    story.append(Spacer(1, 3))
    story.append(info_box("Output", one_output, LIGHT_TEAL))

    story.append(P("Few-Shot Prompting", h2))
    story.append(prompt_box("PROMPT + MULTIPLE EXAMPLES", few_examples))
    story.append(Spacer(1, 3))
    story.append(info_box("Input", few_input, LIGHT_GOLD))
    story.append(Spacer(1, 3))
    story.append(info_box("Output", few_output, LIGHT_TEAL))

    story.append(P("Comparison", h2))
    story.append(data_table(["Technique", "Input", "Output"], comparison,
                             [30*mm, 108*mm, 40*mm]))
    story.append(P("Observation", h2))
    story.append(P(observation))
    story.append(P("Conclusion", h2))
    story.append(info_box("Conclusion", conclusion, LIGHT_BLUE))
    story.append(PageBreak())

# Q1
add_question(
1, "Sentiment Classification for Customer Reviews",
"An e-commerce platform wants to analyze customer reviews and classify them into Positive, Negative, or Neutral sentiments using prompt engineering.",
["No.", "Customer Review", "Expected Output"],
[
("1","The product quality is excellent and I am very happy.","Positive"),
("2","The product arrived damaged.","Negative"),
("3","The product arrived on time and works as described.","Neutral"),
("4","I love this product. It is better than expected.","Positive"),
("5","The product stopped working after two days.","Negative"),
("6","The package arrived on time.","Neutral")],
"Classify the sentiment of the following customer review as Positive, Negative, or Neutral. Return only the sentiment label.\nInput: The product quality is excellent and I am very happy.",
"Positive",
"Classify the sentiment as Positive, Negative, or Neutral.\n\nExample:\nInput: I am extremely happy with this product.\nOutput: Positive\n\nNow classify:\nInput: The product arrived damaged.",
"The product arrived damaged.","Negative",
"Classify the sentiment as Positive, Negative, or Neutral.\n\nExample 1:\nInput: I love this product.\nOutput: Positive\n\nExample 2:\nInput: The product arrived broken.\nOutput: Negative\n\nExample 3:\nInput: The product arrived on time and works as described.\nOutput: Neutral\n\nNow classify:\nInput: I am very satisfied with my purchase.",
"I am very satisfied with my purchase.","Positive",
[("Zero-Shot","The product quality is excellent and I am very happy.","Positive"),
 ("One-Shot","The product arrived damaged.","Negative"),
 ("Few-Shot","I am very satisfied with my purchase.","Positive")],
"Zero-Shot works well for simple cases. One-Shot provides additional guidance through one example. Few-Shot provides multiple examples and generally gives more consistent results.",
"Few-Shot prompting is generally more reliable because multiple examples help the model understand different sentiment categories."
)

# Q2
add_question(
2, "Email Priority Classification",
"A company wants to automatically prioritize incoming emails into High Priority, Medium Priority, or Low Priority.",
["No.", "Email Message", "Expected Output"],
[
("1","The production server is down and customers cannot access the website.","High Priority"),
("2","Please review the project report before tomorrow's meeting.","Medium Priority"),
("3","Here is the monthly company newsletter.","Low Priority"),
("4","The payment system has stopped working for all customers.","High Priority"),
("5","Please send me the updated project schedule.","Medium Priority"),
("6","Here is the monthly announcement.","Low Priority")],
"Classify the following email as High Priority, Medium Priority, or Low Priority. Return only the priority level.\nInput: The production server is down and customers cannot access the website.",
"High Priority",
"Classify emails as High Priority, Medium Priority, or Low Priority.\n\nExample:\nInput: The payment system is unavailable for all customers.\nOutput: High Priority\n\nNow classify:\nInput: Please review the project report before tomorrow's meeting.",
"Please review the project report before tomorrow's meeting.","Medium Priority",
"Classify emails as High Priority, Medium Priority, or Low Priority.\n\nExample 1:\nInput: The company website is down for all users.\nOutput: High Priority\n\nExample 2:\nInput: Please review the project report before tomorrow.\nOutput: Medium Priority\n\nExample 3:\nInput: Here is the monthly newsletter.\nOutput: Low Priority\n\nNow classify:\nInput: The payment system has stopped working for all customers.",
"The payment system has stopped working for all customers.","High Priority",
[("Zero-Shot","The production server is down.","High Priority"),
 ("One-Shot","Please review the project report before tomorrow's meeting.","Medium Priority"),
 ("Few-Shot","The payment system has stopped working for all customers.","High Priority")],
"Zero-Shot can classify obvious emails correctly. One-Shot provides additional context. Few-Shot gives examples for different priority levels and improves consistency.",
"Few-Shot prompting is the most reliable technique because the examples clearly demonstrate High, Medium, and Low Priority categories."
)

# Q3
add_question(
3, "Student Query Routing System",
"A university chatbot must route student queries to Admissions, Exams, Academics, or Placements.",
["No.", "Student Query", "Expected Output"],
[
("1","How can I apply for university admission?","Admissions"),
("2","When will the semester examination timetable be released?","Exams"),
("3","Can I change my elective subject?","Academics"),
("4","When will the campus placement drive begin?","Placements"),
("5","What documents are required for admission?","Admissions"),
("6","How can I register for my upcoming examination?","Exams")],
"Classify the following student query into Admissions, Exams, Academics, or Placements. Return only the department name.\nInput: When will the campus placement drive begin?",
"Placements",
"Route student queries to Admissions, Exams, Academics, or Placements.\n\nExample:\nInput: How can I apply for university admission?\nOutput: Admissions\n\nNow classify:\nInput: Can I change my elective subject?",
"Can I change my elective subject?","Academics",
"Route student queries to Admissions, Exams, Academics, or Placements.\n\nExample 1:\nInput: How can I apply for admission?\nOutput: Admissions\n\nExample 2:\nInput: When is the semester examination?\nOutput: Exams\n\nExample 3:\nInput: Can I change my elective?\nOutput: Academics\n\nExample 4:\nInput: When will placement drives start?\nOutput: Placements\n\nNow classify:\nInput: How can I register for my upcoming examination?",
"How can I register for my upcoming examination?","Exams",
[("Zero-Shot","When will the campus placement drive begin?","Placements"),
 ("One-Shot","Can I change my elective subject?","Academics"),
 ("Few-Shot","How can I register for my upcoming examination?","Exams")],
"Zero-Shot works well for straightforward queries. One-Shot provides an example of the expected routing. Few-Shot provides examples from multiple departments and reduces ambiguity.",
"Few-Shot prompting improves classification accuracy because the model receives examples representing different university departments."
)

# Q4
add_question(
4, "Chatbot Question Type Detection",
"A chatbot must identify whether a user query is Informational, Transactional, Complaint, or Feedback.",
["No.", "User Query", "Expected Output"],
[
("1","What are your customer support hours?","Informational"),
("2","I want to cancel my order.","Transactional"),
("3","My order arrived damaged.","Complaint"),
("4","The new website design is very easy to use.","Feedback"),
("5","What payment methods do you accept?","Informational"),
("6","Please change my delivery address.","Transactional")],
"Classify the following chatbot query as Informational, Transactional, Complaint, or Feedback. Return only the question type.\nInput: My order arrived damaged.",
"Complaint",
"Classify chatbot queries as Informational, Transactional, Complaint, or Feedback.\n\nExample:\nInput: What payment methods do you accept?\nOutput: Informational\n\nNow classify:\nInput: Please change my delivery address.",
"Please change my delivery address.","Transactional",
"Classify chatbot queries as Informational, Transactional, Complaint, or Feedback.\n\nExample 1:\nInput: What are your support hours?\nOutput: Informational\n\nExample 2:\nInput: I want to cancel my order.\nOutput: Transactional\n\nExample 3:\nInput: My package arrived damaged.\nOutput: Complaint\n\nExample 4:\nInput: The new website is easy to use.\nOutput: Feedback\n\nNow classify:\nInput: Please change my delivery address.",
"Please change my delivery address.","Transactional",
[("Zero-Shot","My order arrived damaged.","Complaint"),
 ("One-Shot","Please change my delivery address.","Transactional"),
 ("Few-Shot","Please change my delivery address.","Transactional")],
"Zero-Shot handles clear queries but may have difficulty with ambiguous cases. One-Shot provides additional guidance. Few-Shot provides examples of different question types and improves consistency.",
"Few-Shot prompting provides better classification because multiple examples clearly demonstrate the different question types."
)

# Q5
add_question(
5, "Emotion Detection in Text",
"A mental-health chatbot needs to detect emotions as Happy, Sad, Angry, Anxious, or Neutral.",
["No.", "Text", "Expected Output"],
[
("1","I got excellent marks and I am very happy today!","Happy"),
("2","I feel disappointed because I could not attend the event.","Sad"),
("3","I am extremely frustrated with this service.","Angry"),
("4","I am worried about tomorrow's examination.","Anxious"),
("5","I went to the library and studied for two hours.","Neutral"),
("6","I am excited about my upcoming vacation.","Happy")],
"Identify the emotion in the following text.\nChoose one: Happy, Sad, Angry, Anxious, Neutral.\nReturn only the emotion.\nInput: I am worried about tomorrow's examination.",
"Anxious",
"Identify the emotion as Happy, Sad, Angry, Anxious, or Neutral.\n\nExample:\nInput: I am excited about my success.\nOutput: Happy\n\nNow classify:\nInput: I am extremely frustrated with this service.",
"I am extremely frustrated with this service.","Angry",
"Identify the emotion as Happy, Sad, Angry, Anxious, or Neutral.\n\nExample 1:\nInput: I got excellent marks and I am very happy.\nOutput: Happy\n\nExample 2:\nInput: I feel disappointed about missing the event.\nOutput: Sad\n\nExample 3:\nInput: I am extremely frustrated with this service.\nOutput: Angry\n\nExample 4:\nInput: I am worried about tomorrow's examination.\nOutput: Anxious\n\nExample 5:\nInput: I went to the library and studied for two hours.\nOutput: Neutral\n\nNow classify:\nInput: I am nervous about my upcoming presentation.",
"I am nervous about my upcoming presentation.","Anxious",
[("Zero-Shot","I am worried about tomorrow's examination.","Anxious"),
 ("One-Shot","I am extremely frustrated with this service.","Angry"),
 ("Few-Shot","I am nervous about my upcoming presentation.","Anxious")],
"Zero-Shot can identify clear emotions without examples. One-Shot provides guidance through one example. Few-Shot provides multiple emotional examples and handles similar emotions more consistently.",
"Few-Shot prompting generally performs better because the model receives examples representing multiple emotional categories."
)

# Overall comparison
story.append(section_bar("Overall Comparison"))
story.append(Spacer(1, 7))
story.append(data_table(
    ["Prompting Technique", "Examples", "Context", "Reliability"],
    [("Zero-Shot","0","Low","Good"),("One-Shot","1","Medium","Better"),("Few-Shot","3–5","High","Best")],
    [55*mm, 28*mm, 42*mm, 53*mm]
))
story.append(Spacer(1, 10))
story.append(P("Final Conclusion", h2))
story.append(P("Few-Shot Prompting generally produces the most reliable results among the three techniques."))
story.append(P("The additional examples provide more context and help the AI understand the expected relationship between the input and output categories."))
story.append(info_box("Key Idea", "<b>Zero-Shot → One-Shot → Few-Shot</b><br/>This represents an increase in contextual guidance and generally improves classification consistency.", LIGHT_GOLD))

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    if doc.page > 1:
        canvas.setFillColor(NAVY)
        canvas.rect(0, h-8*mm, w, 8*mm, fill=1, stroke=0)
        canvas.setFont(BOLD, 7.5)
        canvas.setFillColor(WHITE)
        canvas.drawString(16*mm, h-5.3*mm, "PROMPT ENGINEERING LAB ASSIGNMENT")
    canvas.setStrokeColor(HexColor("#D0D5DD"))
    canvas.line(16*mm, 11*mm, w-16*mm, 11*mm)
    canvas.setFont(BASE, 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawString(16*mm, 7*mm, "Prompt Engineering Lab")
    canvas.drawRightString(w-16*mm, 7*mm, f"Page {doc.page}")
    canvas.restoreState()

# Cover page at the beginning
cover = []
cover.append(Spacer(1, 38*mm))
cover.append(P("PROMPT ENGINEERING", title))
cover.append(P("LAB ASSIGNMENT", ParagraphStyle("cover2", parent=title, fontSize=25, textColor=BLUE)))
cover.append(Spacer(1, 6*mm))
cover.append(HRFlowable(width="65%", thickness=2, color=TEAL, hAlign="CENTER"))
cover.append(Spacer(1, 8*mm))
cover.append(P("Sentiment Classification • Email Priority • Query Routing<br/>Question Type Detection • Emotion Detection", subtitle))
cover.append(Spacer(1, 28*mm))

meta = Table([
    [P("<b>Student Name</b>", small), P("______________________________", small)],
    [P("<b>Roll Number</b>", small), P("______________________________", small)],
    [P("<b>Section</b>", small), P("______________________________", small)],
    [P("<b>Course / Subject</b>", small), P("Prompt Engineering Lab", small)],
    [P("<b>Academic Year</b>", small), P("2026–2027", small)],
], colWidths=[48*mm, 120*mm])
meta.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),LIGHT_BLUE),
    ("BOX",(0,0),(-1,-1),0.8,BLUE),
    ("INNERGRID",(0,0),(-1,-1),0.4,HexColor("#C9D6E3")),
    ("LEFTPADDING",(0,0),(-1,-1),9),
    ("RIGHTPADDING",(0,0),(-1,-1),9),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
]))
cover.append(meta)
cover.append(Spacer(1, 30*mm))
cover.append(P("Prepared for Academic Submission", subtitle))
cover.append(PageBreak())

# Insert cover before main story.
final_story = cover + story

doc.build(final_story, onFirstPage=header_footer, onLaterPages=header_footer)

print(f"Created: {out}")
