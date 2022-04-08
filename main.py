import jinja2
#import pyqrcode
# from pyqrcode import QRCode
#import png
import os
import pdfkit
# from xhtml2pdf import pisa
# from PyPDF2 import PdfFileMerger
import pandas as pd
import traceback
options = {'page-size': 'Letter',
        'margin-top': '0.13in',
        'margin-right': '0.69in',
        'margin-bottom': '0.19in',
        'margin-left': '0.46in',
           }
def render_html(Sitare_Id,Firstname,Lastname,engSa2, hinSa2, matSa2, sciSa2, sstSa2, engSa2P, hinSa2P, matSa2P, sciSa2P, sstSa2P, sa2Avg, sa2AvW,
                engPt2, hinPt2, matPt2, sciPt2, sstPt2, engPt2P, hinPt2P, matPt2P, sciPt2P, sstPt2P,
                engSa1, hinSa1, matSa1, sciSa1,
                sstSa1,
                engSa1P,
                hinSa1P,
                matSa1P,
                sciSa1P,
                sstSa1P,
                sa1Avg,
                sa1AvW,
                engPt1,
                hinPt1,
                matPt1,
                sciPt1,
                sstPt1,
                engPt1P,
                hinPt1P,
                matPt1P,
                sciPt1P,
                sstPt1P,
                pt1Avg,
                pt1AvW,
                pt2Avg,
                pt2AvW,
                Note,
                ):
    """
    Render html page using jinja
    """
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "Template/Final Grade 6 Template/FinalGrade6Template.html"
    template = template_env.get_template(template_file)
    output_text = template.render(
        Sitare_Id=Sitare_Id,
        Firstname=Firstname,
        Lastname=Lastname,
        engSa2=engSa2,
        hinSa2=hinSa2,
        matSa2=matSa2,
        sciSa2=sciSa2,
        sstSa2=sstSa2,
        engSa2P=engSa2P,
        hinSa2P=hinSa2P,
        matSa2P=matSa2P,
        sciSa2P=sciSa2P,
        sstSa2P=sstSa2P,
        sa2Avg=sa2Avg,
        sa2AvW=sa2AvW,
        engPt2=engPt2,
        hinPt2=hinPt2,
        matPt2=matPt2,
        sciPt2=sciPt2,
        sstPt2=sstPt2,
        engPt2P=engPt2P,
        hinPt2P=hinPt2P,
        matPt2P=matPt2P,
        sciPt2P=sciPt2P,
        sstPt2P=sstPt2P,
        engSa1=engSa1,
        hinSa1=hinSa1,
        matSa1=matSa1,
        sciSa1=sciSa1,
        sstSa1=sstSa1,
        engSa1P=engSa1P,
        hinSa1P=hinSa1P,
        matSa1P=matSa1P,
        sciSa1P=sciSa1P,
        sstSa1P=sstSa1P,
        sa1Avg=sa1Avg,
        sa1AvW=sa1AvW,
        engPt1=engPt1,
        hinPt1=hinPt1,
        matPt1=matPt1,
        sciPt1=sciPt1,
        sstPt1=sstPt1,
        engPt1P=engPt1P,
        hinPt1P=hinPt1P,
        matPt1P=matPt1P,
        sciPt1P=sciPt1P,
        sstPt1P=sstPt1P,
        pt1Avg=pt1Avg,
        pt1AvW=pt1AvW,
        pt2Avg=pt2Avg,
        pt2AvW=pt2AvW,
        Note=Note,

    )

    html_path = f'ReportHtml/{Sitare_Id}.html'
    html_file = open(html_path, 'w')
    html_file.write(output_text)
    html_file.close()
    print(f"Report Card html of {Sitare_Id} is successfully generated at {html_file.name}")
    pdfkit.from_file(html_path, f'ReportPdf/{Sitare_Id}.pdf', options=options)
    print("PDF Saved Successful")

render_html("JAI-21102","Harshit","Gupta","1%",2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,"Continued")



