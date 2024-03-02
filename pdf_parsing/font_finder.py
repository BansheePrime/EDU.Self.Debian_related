#!/usr/bin/env python3
import PyPDF2

# Open the PDF file in read-binary mode
with open('tests_exam.pdf', 'rb') as pdf_file:
    # Create a PdfFileReader object to read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate over each page of the PDF file
    for page_num in range(len(pdf_reader.pages)):
        # Get the PageObject for the current page
        page = pdf_reader.pages[0]

        # Get the fonts used in the current page
        #font_dict = page_obj['/Resources']['/Font']
        fonts = set()

        # Print the font names and their corresponding object numbers
        #for font_name in font_dict.keys():
        #    font_obj = font_dict[font_name]
        #    print(f"Page {page_num+1}: {font_name} )")
        for obj in page['/Resources'].get_object():
            if obj == '/Font':
                for font_obj in page['/Resources'].get_object()[obj]:
                    fonts.add(page['/Resources'].get_object()[obj][font_obj]['/BaseFont'])
        print("Fonts used on page #", page_num + 1, ":", fonts)

        for i in fonts:
            print(i)

        
# print(type(fonts))
#import re
#
#regex = r"^/[A-Z]*."
#
#test_str = ("/UWURPK+UniversLTStd-Bold\n"
#	"/UXICPK+UniversLTStd\n"
#	"/EYSZZQ+SabonLTStd-Roman\n"
#	"/DDEOII+ZapfDingbatsStd\n"
#	"/EWMPZQ+SourceCodePro-Regular\n"
#	"/ZYEAHA+UniversLTStd-BoldCn")
#
#subst = "Font name: "
#
## You can manually specify the number of replacements by changing the 4th argument
#result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
#
#if result:
#    print (result)
#

pdf_file.close()

