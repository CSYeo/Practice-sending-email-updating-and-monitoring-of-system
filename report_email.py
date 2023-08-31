
#!/usr/bin/env python3
import sys
import os
import datetime
import reports
import emails

folder = "{}/supplier-data/descriptions".format(os.getcwd())

def report(f):
  name_weight_list = []
  for txt in os.listdir(f):
    filepath = "{}/{}".format(f, txt)

    with open(filepath, 'r') as data:
            lines = data.readlines()
    #lines now will read one line at a time
            name_weight_list.append("{}\n{}\n".format(lines[0],lines[1]))
  name_weight = "\n".join(name_weight_list)
  return name_weight

today = datetime.datetime.now()
formatted_date = today.strftime("%B  %d, %Y")
title = "Processed Update on {}".format(formatted_date)

def main():
  data = report(folder)
  print(data)
  reports.generate_report("/tmp/processed.pdf",title, data)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)

if __name__ == "__main__":
    main()
