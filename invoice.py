#!python3
"""Usage:
     invoice <invoice_number> <yyyymm>
"""
import gspread
import re
import xml.etree.ElementTree as ET
from oauth2client.service_account import ServiceAccountCredentials
from docopt import docopt


GOOGLE_SHEET_URL = ''
AUTH_JSON_FILENAME = ''


if __name__ == '__main__':
    options = docopt(__doc__)

    yyyymm_re = re.compile('^' + options['<yyyymm>'] + '[0-9]{2}$')

    sheet = gspread.authorize(
        ServiceAccountCredentials.from_json_keyfile_name(
            AUTH_JSON_FILENAME,
            ['https://spreadsheets.google.com/feeds']
        )
    ).open_by_url(
        GOOGLE_SHEET_URL
    ).sheet1
    
    # collect invoice info and confirm that 8 hours were logged this month.
    total = 0.0
    invoice_lines = []

    for cell in sheet.findall(yyyymm_re):
        if cell.col == 1:
            total = total + float(sheet.cell(cell.row, 5).value)
            invoice_line = sheet.cell(cell.row, 11).value
            if invoice_line:
                invoice_lines.append(invoice_line)

    # get invoice.fo
    root = ET.parse('invoice.fo').getroot()

    print(total)
    for i in invoice_lines:
        print(i)

    # print(ET.tostring(root))
