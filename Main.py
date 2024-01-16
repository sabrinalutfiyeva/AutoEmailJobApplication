import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import csv
import os 


#Email server setup 
my_email = "sabrinalutfiyeva@gmail.com"
password_key= "nviq ewpb iyqm qgyc"

gmail_server = "smtp.gmail.com"
gmail_port = 587

my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.starttls()
my_server.login(my_email, password_key)

text_content = """
Hello {recruiter_name}, I hope you are doing well. I’m Sabrina, a software engineering graduate with an BS. in Computer Science and a specialization in statistical analysis. 

I wanted to connect regarding open roles in {job_role} at {organization}. I have 2 years of experience in software testing engineering and exciting projects I've worked on in my own time; I developed a comprehensive full-stack bug tracking system designed to streamline the process of reporting, tracking, and resolving software bugs. This project showcases my skills in both front-end and back-end development, as well as my ability to integrate and manage databases.

 I’m excited to have an opportunity to apply my skills and learn more about {organization}


I have attached my resume below. Looking forward to hearing from you.

Thanks,
Sabrina Lutfiyeva   
"""


# Paths to your attachment
resume_file_path = "/Users/sabrinalutfiyeva/AutoEmailApplication/SabrinaLutfiyevaResume.pdf"


# Read CSV and send emails
with open("job_contacts.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Personalize the email content
        personalized_content = text_content.format(
            recruiter_name=row["Recruiter Name"],
            job_role=row["Job Role"],
            organization=row["Organization Name"],
        )

        # Create the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Job Application"
        message["From"] = my_email
        message["To"] = row["Recruiter Email"]

        # Attach text content
        message.attach(MIMEText(personalized_content, "plain"))

        # Attach resume
        with open(resume_file_path, 'rb') as f:
            resume = MIMEApplication(f.read(), name=os.path.basename(resume_file_path))
            resume['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_file_path)}"'
            message.attach(resume)

        # Send the email
        my_server.sendmail(my_email, row["Recruiter Email"], message.as_string())

# Close the server connection
my_server.quit()