
#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, name_weight):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  to_build = [report_title, empty_line]
  #added to_build variable as the report.buld fundtion can
  #only take a list and not a list of lists
  count = 1
  for para in name_weight:
    lines = Paragraph(para, styles["BodyText"])
    to_build.append(lines)
    if count % 2 == 0:
      to_build.append(empty_line)
    count += 1
  report.build(to_build)
