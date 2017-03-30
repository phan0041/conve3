import json
import os
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from models import Record
import general_util
from datetime import datetime

shipper_sheet = None
sheet = None
parameter = None
data = None
count = None
data_list = None
email = None

def init():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'Conve-e61ea6dbdc95.json')
    json_key = json.load(open(file_path))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)
    global sheet
    sheet = gc.open("Record.xlsx")
    global shipper_sheet
    shipper_sheet = sheet.worksheet("Shipper Information")
    global parameter
    parameter = sheet.worksheet("Parameters")
    global email
    email = sheet.worksheet("email")
    return None

def get_row(i):
    global shipper_sheet
    return shipper_sheet.row_values(i)

def get_all_data():
    data_list =[]
    for i in range(2, get_count()+2):
        data_list.append(i)
    get_data_from(data_list)
    return None

def get_count():
    init()
    global parameter
    global count
    count = int(parameter.acell("B4").value)
    return count

def get_update_info():
    global parameter
    global data_list
    temp = parameter.acell("B5").value
    if temp is not "" :
        if "," not in temp :
            data_list = [int(temp)]
        else:
            temp_list = temp.split(",")
            for i in range(0, len(temp_list)):
                temp_list[i] = int(temp_list[i])
            data_list = temp_list
        return data_list
    else:
        return []

def get_data_from(data_list):
    init()
    global shipper_sheet
    # data = shipper_sheet.get_all_records(False, 1)
    # for i in range(start, len(data)):
    #     r = data[i].items()
    #     if r[9][1] is not "":
    #         record = Record()
    #         record.shipper_name     = r[6][1]
    #         record.date             = general_util.format_string(r[3][1])
    #         record.direction        = r[9][1]
    #         record.contact          = r[5][1]
    #         record.kg_available     = r[2][1]
    #         record.note             = r[11][1]
    #         record.price            = r[7][1]
    #         record.url              = r[0][1]
    #         record.is_checked       = False
    #         record.save()
    #     else:
    #         break

    for i in data_list:
        r = get_row(i)
        if len(Record.objects.filter(code=r[12])) == 0:
            print "insert:"
            record = Record()
            record.shipper_name     = r[3]
            record.date             = general_util.format_string(r[2])
            record.direction        = r[1]
            record.code             = r[12]
            record.contact          = r[6]
            record.kg_available     = r[4]
            record.note             = r[7]
            record.price            = r[5]
            record.url              = r[8]
            record.is_checked       = False
            record.save()
            print r
        else:
            print "update :"
            record = Record.objects.get(code=r[12])
            record.shipper_name     = r[3]
            record.date             = general_util.format_string(r[2])
            record.direction        = r[1]
            record.code             = r[12]
            record.contact          = r[6]
            record.kg_available     = r[4]
            record.note             = r[7]
            record.price            = r[5]
            record.url              = r[8]
            record.is_checked       = True
            record.save()
            print r

    return None

def update_data():
    if Record.objects.count() == 0:
            get_all_data()
    else:
        if Record.objects.count() < get_count():
            print "Updating..."
            global count
            data_list = []
            for i in range(Record.objects.count()+2, count+2):
                data_list.append(i)
            get_data_from(data_list)
    if len(get_update_info()) > 0:
        global data_list
        get_data_from(data_list)
        global parameter
        parameter.update_acell('B5', '')
    return None

def add_email(s, t):
    init()
    global parameter
    global email
    count = int(parameter.acell("B6").value)
    cell = 'A'+str((count+1))
    email.update_acell(cell, s)
    cell = 'B'+str((count+1))
    email.update_acell(cell, t)
    cell = 'C'+str((count+1))
    email.update_acell(cell, datetime.now())
    return None
