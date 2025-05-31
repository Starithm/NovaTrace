def parse_astronomy_report(text):
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')

    numeric_values = {}
    tables = []

    # Extract numeric values into a dictionary
    for row in soup.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 8:  # Check if the row has enough columns
            wavelengths = re.sub('[^0-9]', '', cells[1].text)  # Extract only numeric characters from the second column
            fluxes = cells[7].text  # Extract flux values from the eighth column
            filter_values = cells[5].text  # Extract filter values from the sixth column

            coordinates = cells[3].text.split('|')  # Split the fourth column using ',' as a delimiter to get x and y coordinates
            numeric_values['coordinates'] = []
            for coord in coordinates:
                numeric_values['coordinates'].append(tuple(map(float, coord.strip().split('|'))))

            numeric_values['wavelengths'] = [float(wavelength) for wavelength in wavelengths]
            numeric_values['fluxes'] = [float(flux) for flux in re.sub('[^0-9.]', '', fluxes).split()]
            numeric_values['filter_values'] = filter_values.split()  # Split the filter values using space as a delimiter

    # Extract tables into a list of dictionaries
    table_rows = soup.find_all('tr')
    if len(table_rows) > 0:
        for row in table_rows[1:]:  # Skip the header row
            columns = [cell.text for cell in row.find_all('td')]
            tables.append({'wavelength': columns[0], 'flux': columns[1], 'filter': columns[2], 'coordinates': columns[3]})

    return {"numeric_values": numeric_values, "tables": tables}