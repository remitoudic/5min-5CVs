import clr
clr.AddReference("Spire.Doc")
from Spire.Doc import Document
from Spire.Doc.Documents import Paragraph, ParagraphStyle
from Spire.Doc.Fields import TextRange
from Spire.Doc.Formatting import TextAlignment

class TemplateCv1:
    def __init__(self, filename):
        self.filename = filename
        self.doc = Document()

        # Define styles
        self.title_style = self.create_style("TitleStyle", 24, True)
        self.heading_style = self.create_style("HeadingStyle", 18, True)
        self.body_style = self.create_style("BodyStyle", 12, False)

    def create_style(self, style_name, font_size, bold):
        style = ParagraphStyle(self.doc)
        style.Name = style_name
        style.CharacterFormat.FontSize = font_size
        style.CharacterFormat.Bold = bold
        style.CharacterFormat.TextColor = clr.System.Drawing.Color.Black
        self.doc.Styles.Add(style)
        return style

    def add_name(self, name):
        para = self.doc.AddSection().AddParagraph()
        para.AppendText(name)
        para.ApplyStyle("TitleStyle")
        para.Format.AfterSpacing = 12

    def add_career_objectives(self, objectives):
        para = self.doc.LastSection.AddParagraph()
        para.AppendText("Career Objectives")
        para.ApplyStyle("HeadingStyle")
        para.Format.AfterSpacing = 12

        para = self.doc.LastSection.AddParagraph()
        para.AppendText(objectives)
        para.ApplyStyle("BodyStyle")
        para.Format.AfterSpacing = 24

    def add_work_experience(self, work_experience):
        para = self.doc.LastSection.AddParagraph()
        para.AppendText("Work Experience")
        para.ApplyStyle("HeadingStyle")
        para.Format.AfterSpacing = 12

        table = self.doc.LastSection.AddTable(True)
        table.ResetCells(len(work_experience) + 1, 3)
        # Set the first row (header)
        row = table.Rows[0]
        row.Cells[0].AddParagraph().AppendText("Position")
        row.Cells[1].AddParagraph().AppendText("Company")
        row.Cells[2].AddParagraph().AppendText("Date")
        # Add the work experience
        for i, exp in enumerate(work_experience):
            row = table.Rows[i + 1]
            row.Cells[0].AddParagraph().AppendText(exp["position"])
            row.Cells[1].AddParagraph().AppendText(exp["company"])
            row.Cells[2].AddParagraph().AppendText(exp["date"])
        table.Format.AfterSpacing = 24

    def add_education(self, education):
        para = self.doc.LastSection.AddParagraph()
        para.AppendText("Education")
        para.ApplyStyle("HeadingStyle")
        para.Format.AfterSpacing = 12

        table = self.doc.LastSection.AddTable(True)
        table.ResetCells(len(education) + 1, 2)
        # Set the first row (header)
        row = table.Rows[0]
        row.Cells[0].AddParagraph().AppendText("School")
        row.Cells[1].AddParagraph().AppendText("Date")
        # Add the education details
        for i, edu in enumerate(education):
            row = table.Rows[i + 1]
            row.Cells[0].AddParagraph().AppendText(edu["school"])
            row.Cells[1].AddParagraph().AppendText(edu["date"])
        table.Format.AfterSpacing = 24

    def build_doc(self, data):
        self.add_name(data.get("name", ""))
        self.add_career_objectives(data.get("career_objectives", ""))
        self.add_work_experience(data.get("work_experience", []))
        self.add_education(data.get("education", []))
        self.doc.SaveToFile(self.filename, FileFormat.Docx)

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

# Create the filename using the template "template1_" + name + "_" + id
user_id = 123  # Example ID
filename = f"template1_{data['name'].replace(' ', '_')}_{user_id}.docx"

# Create the CV Word document using the class
cv = TemplateCv1(filename)
cv.build_doc(data)
