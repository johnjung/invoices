# Invoices

Generate PDF invoices, using custom fonts and a custom layout, from a Google
Sheet with time tracking information. These scripts are customized for my own
invoices, but please feel free to modify this code.

## Setup

### Getting Python modules

Set up a Python virtual environment somewhere appropriate and install 
the required Python libraries:

```console
$ python3 -m venv env
$ pip install -r requirements.txt
```

### Getting Apache Formatting Objects Processor (FOP)

1. [Download FOP](https://xmlgraphics.apache.org/fop/)
2. Add Avenir to the fonts folder. 

### Setting up API access to Google Sheets

1. Go to the Google API Console: https://console.developers.google.com/
2. Click 'create a new project'. 
3. Give the project a memorable name. 
4. Click 'enable APIs and services'.
5. G Suite, Google Drive API, Google Sheets API. 
6. Click 'create credentials'.
7. Download the JSON service account key and put it in this folder.
8. Look in the .json file for 'client_email'. Be sure to share the initial
   spreadsheet with that email address.

## Making a new invoice

```console
$ invoice <client> <yyyymm> <invoice_number>
```
