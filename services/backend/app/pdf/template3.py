from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from io import BytesIO

class TemplateCv3:
    def __init__(self, buffer):
        self.buffer = buffer
        self.doc = SimpleDocTemplate(self.buffer, pagesize=A4, topMargin=30, bottomMargin=30, leftMargin=40, rightMargin=40)
        self.styles = getSampleStyleSheet()
        self.flowables = []

        # Define custom styles using default fonts
        self.styles.add(ParagraphStyle(name='Name', fontName='Helvetica-Bold', fontSize=24, textColor=colors.HexColor("#2C3E50"), spaceAfter=12))
        self.styles.add(ParagraphStyle(name='Section', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor("#2980B9"), spaceBefore=12, spaceAfter=6))
        self.styles.add(ParagraphStyle(name='CustomNormal', fontName='Helvetica', fontSize=10, textColor=colors.HexColor("#34495E"), spaceAfter=6))
        self.styles.add(ParagraphStyle(name='Right', fontName='Helvetica', fontSize=10, textColor=colors.HexColor("#34495E"), alignment=TA_RIGHT))

    def add_name(self, name):
        self.flowables.append(Paragraph(name, self.styles['Name']))

    def add_career_objectives(self, objectives):
        self.flowables.append(Paragraph("Career Objectives", self.styles['Section']))
        self.flowables.append(Paragraph(objectives, self.styles['CustomNormal']))

    def add_work_experience(self, work_experience):
        self.flowables.append(Paragraph("Work Experience", self.styles['Section']))
        for exp in work_experience:
            data = [
                [Paragraph(exp["position"], self.styles['CustomNormal']), Paragraph(exp["date"], self.styles['Right'])],
                [Paragraph(exp["company"], self.styles['CustomNormal']), ""]
            ]
            table = Table(data, colWidths=[350, 150])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            self.flowables.append(table)
            self.flowables.append(Spacer(1, 6))

    def add_education(self, education):
        self.flowables.append(Paragraph("Education", self.styles['Section']))
        for edu in education:
            data = [
                [Paragraph(edu["school"], self.styles['CustomNormal']), Paragraph(edu["date"], self.styles['Right'])]
            ]
            table = Table(data, colWidths=[350, 150])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            self.flowables.append(table)
            self.flowables.append(Spacer(1, 6))

    def build_pdf(self, data):
        self.add_name(data.get("name", ""))
        self.add_career_objectives(data.get("career_objectives", ""))
        self.add_work_experience(data.get("work_experience", []))
        self.add_education(data.get("education", []))
        self.doc.build(self.flowables)
        self.buffer.seek(0)

# Example usage
data = {
    "name": "Joe Doe",
    "career_objectives": "Seeking a challenging role in data science where I can utilize my skills to contribute to organizational success.",
    "work_experience": [
        {"position": "Data Analyst", "company": "DataCorp", "date": "2019 - Present"},
        {"position": "Junior Data Scientist", "company": "Tech Solutions", "date": "2017 - 2019"}
    ],
    "education": [
        {"school": "University of Data Science", "date": "2013 - 2017"},
        {"school": "San Joseph High School", "date": "2010 - 2012"}
    ]
}

# To use:

buffer = BytesIO()
cv = TemplateCv3(buffer)
cv.build_pdf(data)
buffer.seek(0)
with open('modern_cv.pdf', 'wb') as f:
    f.write(buffer.getvalue())
