# Used with views.py
# debug towards end of:
# https://www.youtube.com/watch?v=0LK-CBehUNA&list=PLqvh7Qfqxgg5IjBDfhVBAZMkHQHiQf8wP&index=27&ab_channel=SugarloafAndaCupofJoe
# PYXL Doc: https://openpyxl.readthedocs.io/en/stable/

# Storing unique values for the different headers within the 2014 and 2015 spreadsheets
# Class helps keep tracvks of the names used below.
# Each value is a string that will be looked for to determine which header is which
class XLHEADERS():
    COUNTRY = 'country'
    CITY = 'city'
    STATION_EOI_CODE = 'stationeoicode'
    STATION_NAME = 'stationname'
    AIR_POLLUTANT = 'airpollutant'
    AIR_POLLUTION_LEVEL = 'airpollutionlevel'
    TYPE = 'type'
    AREA = 'area'
    LONGITUDE = 'longitude'
    LATITUDE = 'latitude'
    ALTITUDE = 'altitude'

# choices taking values from above and stored in an array/dictionary
    # Able to reuse in different sections
    choices = [COUNTRY, CITY, STATION_EOI_CODE, STATION_NAME, AIR_POLLUTANT, AIR_POLLUTION_LEVEL, TYPE, AREA,
               LONGITUDE, LATITUDE, ALTITUDE]

def get_headers_and_units(ws):
    # Initialize variables
    headers_row = None
    headers = {}
    units = ''
    
    # Get headers row
    # +1 to make sure it gets all rows
    for row in range(ws.max_row + 1):
        cell = ws['A'][row].value
        if isinstance(cell, str) and 'country' in cell.lower():
            headers_row = row
            break
    if headers_row is None:
        # from views.py, if headers_row is None, then header = None and units = None
        return None, None, None

        # Remember headers positions
        # go row by row which are lists of all the elements

    for i in range(ws.max_column):
        # a = 0
        # column = char(a +65)
        # column = 65
        # 65 in ASCI is 65
        column = chr(i + 65)
        header = ws[column][headers_row].value
        #if the cell (header) is none type then we are ready to break
        if header is None:
            break
        # When looking for a phrase, make sure the headers are unique across the different worksheets
        #remove spaces then remove any '_' and lower
        header = header.strip().replace('_', '').lower()

        # Get units stored in header from the 1 spreadsheet
        if 'm3' in header:
            # get information between() of header - can use regex
            units_index = header.find('(') + 1
            # for loop breaks once we find ')'
            for index in range(units_index, units_index + 20):
                if header[index] == ')':
                    break
                # iterate
                units += header[index]
        elif 'unit' in header:
            #we want information from below the header. Not the header as in the if loop above.
            units = ws[column][headers_row + 1].value
            continue

        # Map headers with their indices
        for choice in XLHEADERS.choices:
            # Check if choice is in headers dictionary
            if choice in header:
                # 1: worksheet and extract column A, B, C, D and row 0,1,2,3,4 and get value or 2: Iterate worksheet using rows and each row is a list of values
                # Using 2
                # We want to but the index of a column and not the letter
                headers[choice] = i
                break

    return headers_row, headers, units

