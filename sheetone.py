import smartsheet
import requests
import os
from dotenv import load_dotenv

load_dotenv()

key="SMARTSHEET_ACCESS_TOKEN"
sheet_token=os.getenv(key)

smartsheet_client = smartsheet.Smartsheet(sheet_token)
sheetId = '4144824786937732'
sheet = smartsheet_client.Sheets.get_sheet(sheetId)
url = 'http://api.coinlayer.com/live?access_key=bbd1a180a4409ec39b8caaf9266ed399'

def call_api(api_url):
    r = requests.get(api_url)
    r_dict = r.json()['rates']
    for key in r_dict:
        # print('key is', key)
        # coinNamePrice(key, r_dict[key])

        ### Get the rows and check if there is already data. If there is then use the 'update_rows' for line 29.
        name = coinNameCol(key)
        price = coinPriceCol(r_dict[key])
        newRow = smartsheet_client.models.Row()
        newRow.cells.append(name)
        newRow.cells.append(price)
        smartsheet_client.Sheets.add_rows(sheetId, newRow)

#   btc_price = r.json()['rates']['BTC']
#   print(f'Bitcoin\'s price is: {btc_price}')
    return


### WORKING CODE:
def coinNameCol(coinName):
    for column in sheet.columns:
        if column.title == 'Coin name':
            nameColumn = column.id
    
    nameCell = smartsheet_client.models.Cell()

    nameCell.column_id = nameColumn
    nameCell.value = coinName
    return nameCell
    

def coinPriceCol(coinPrice):
    for column in sheet.columns:
        if column.title == 'coin value':
            priceColumn = column.id

    # newRow = smartsheet_client.models.Row()
    priceCell = smartsheet_client.models.Cell()

    priceCell.column_id = priceColumn
    priceCell.value = coinPrice
    # newRow.cells.append(priceCell)
    # smartsheet_client.Sheets.add_rows(sheetId, newRow)
    return priceCell

########## EXPERIMENTAL:
# def coinNamePrice(coinName, coinPrice):
#     for column in sheet.columns:
#         if column.title == 'Coin name':
#             nameColumn = column.id

#     for column in sheet.columns:
#         if column.title == 'coin value':
#             priceColumn = column.id

#     newRow = smartsheet_client.models.Row()
    
#     nameCell = smartsheet_client.models.Cell()
#     priceCell = smartsheet_client.models.Cell()

#     nameCell.column_id = nameColumn
#     nameCell.value = coinName

#     priceCell.column_id = priceColumn
#     priceCell.value = coinPrice
#     newCells = [nameCell, priceCell]
#     newRow.cells.append(newCells)
#     smartsheet_client.Sheets.add_rows(sheetId, newRow)

call_api(url)