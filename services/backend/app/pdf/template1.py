from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import io
import random


class TemplateCv1:
    def __init__(self, buffer):
        self.buffer = buffer
        self.doc = SimpleDocTemplate(self.buffer, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.flowables = []
    
    def add_name(self, name):
        title_style = self.styles['Title']
        title_style.textColor = colors.darkblue
        self.flowables.append(Paragraph(name, title_style))
        self.flowables.append(Spacer(1, 12))

    def add_career_objectives(self, objectives):
        heading_style = self.styles['Heading1']
        heading_style.textColor = colors.black
        self.flowables.append(Paragraph("Career Objectives", heading_style))
        self.flowables.append(Spacer(1, 12))

        body_style = self.styles['BodyText']
        self.flowables.append(Paragraph(objectives, body_style))
        self.flowables.append(Spacer(1, 24))

    def add_work_experience(self, work_experience):
        heading_style = self.styles['Heading1']
        heading_style.textColor = colors.black
        self.flowables.append(Paragraph("Work Experience", heading_style))
        self.flowables.append(Spacer(1, 12))

        work_exp_table_data = [["Position", "Company", "Date"]]
        for exp in work_experience:
            work_exp_table_data.append([exp["position"], exp["company"], exp["date"]])

        work_exp_table = Table(work_exp_table_data)
        work_exp_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        self.flowables.append(work_exp_table)
        self.flowables.append(Spacer(1, 24))

    def add_education(self, education):
        heading_style = self.styles['Heading1']
        heading_style.textColor = colors.black
        self.flowables.append(Paragraph("Education", heading_style))
        self.flowables.append(Spacer(1, 12))

        education_table_data = [["School", "Date"]]
        for edu in education:
            education_table_data.append([edu["school"], edu["date"]])

        education_table = Table(education_table_data)
        education_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        self.flowables.append(education_table)
        self.flowables.append(Spacer(1, 24))

    def build_pdf(self, data):
        self.add_name(data.get("name", ""))
        self.add_career_objectives(data.get("career_objectives", ""))
        self.add_work_experience(data.get("work_experience", []))
        self.add_education(data.get("education", []))
        self.doc.build(self.flowables)
        self.buffer.seek(0)

# Example usage ----------------------------
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
 

# Create the filename using the template "template1_" + name + "_" + id
user_id = random.randint(1000, 9999)  # Example ID
filename = f"template1_{data['name'].replace(' ', '_')}_{user_id}.pdf"

# Create a file-like buffer for the PDF
buffer = io.BytesIO()

# Create the CV PDF using the class
cv = TemplateCv1(buffer)
cv.build_pdf(data)

# Write the buffer to a file
with open(filename, 'wb') as f:
    f.write(buffer.getvalue())

buffer.close()
