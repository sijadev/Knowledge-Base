from email.message import EmailMessage
from pathlib import Path
from string import Template

path = str(Path(__file__).parent.absolute())

html_file = path + '/files/index.html'
output_file = path + '/files/output.html'

email = EmailMessage()
email['from'] = 'SiJa'
email['to'] = 'anybody@email.com'
email['subject'] = 'Spam emails are the worst of all !'

# Email content als einfacher Text
# email.set_content('Hallo .....')

# Im zweiten Beispiel wird das pathlib modual anstatt des os.path
# verwendet. Der Text vom html wird eingelesen und dem Template
# übergeben. Damit kann die Variable $name im html gesetzt werden.
html = Template(Path(html_file).read_text())
my_content = html.substitute(name='Tim')

# Just for testing
with open(output_file, 'w') as file:
    file.write(my_content)

# html file und müssen das format dafür angeben.

# email.set_content(my_content, 'html')

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('myEmailAccount', 'myPassword')

#     smtp.send_message(email)
