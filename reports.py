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
  report_info = []
  for para in name_weight:
    para = Paragraph(name_weight, styles["BodyText"])
    report_elements.append(para)
    report_elements.append(empty_line)
  report.build([report_title, empty_line, report_info])
