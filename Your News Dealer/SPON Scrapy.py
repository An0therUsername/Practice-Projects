import requests
from bs4 import BeautifulSoup
from datetime import date
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file = 'email_template.html'

url = 'https://www.spiegel.de/schlagzeilen/tops/'
today = date.today()
links = []
headlineIntros = []
headlines = []
txtContents = ''
htmlContents = ''

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
headlineIntro_spon = soup.findAll('span', attrs = {'class':"headline-intro"})
headline_spon = soup.findAll('span', attrs = {'class':"headline"})
headlineLinks_spon = soup.findAll('a', attrs = {'class':"more-link"})

for link in headlineLinks_spon:
        links.append('https://www.spiegel.de' + link.get('href'))

for line in headlineIntro_spon:
    headlineIntros.append(line.text.encode('utf-8'))

for line in headline_spon:
    headlines.append(line.text.encode('utf-8'))
    
    
a = headlineIntros[1:len(headlineIntros)]
b = headlines[1:len(headlines)]

#Generate Txt Version

for i, j in zip(a,b):
    txtContents += i.decode('utf-8') + ':\n' + j.decode('utf-8') + '\n\n'     

#Generate HTML Version
    
html1 = """\
<html>
    <meta charset="utf-8">
      <body>
        <p style="font-size:130%">Die Schlagzeilen heute: </p>
         
"""

html2 = """\
        </span>
  </body>
</html>"""
        
with open(file, 'w', encoding='utf-8') as f:
    f.write(html1)
    for i in range(len(a)):    
        f.write('<em>' + (a[i]).decode('utf-8') + ': </em><br>')
        f.write((b[i]).decode('utf-8') + ' > ')
        f.write('<a href="' + str(links[i]) + '">mehr... </a><br><br>')
    f.write(html2)


with open(file, 'r', encoding='utf-8') as f:
    htmlContents = f.read()

  
#Email Settings
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "yournewsdealer@gmail.com"
password = 'kukbad-jomnU5-bugrom'
receiver_email = ["jramdohr23@gmail.com", "bernd.ramdohr@gmail.com", "doris.ramdohr@gmail.com"]

message = MIMEMultipart("alternative")
message["Subject"] = "Schlagzeilen - " + today.strftime("%A, %d/%m/%y")
message["From"] = "Ihr Nachrichtendienst"
message["To"] = ' ,'.join(receiver_email)

# Turn these into plain/html MIMEText objects
part1 = MIMEText(txtContents, "plain")
part2 = MIMEText(htmlContents, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
