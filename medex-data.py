from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "medicine_details.csv"
f = open(filename, 'w')

column_title = 'Medicine Name, Quantity, Chemical Name, Compnay Name, Unit Price\n'

f.write(column_title)

for page_number in range(1, 714):

    medex_url = 'https://medex.com.bd/brands?page=' + str(page_number)

    # Opening up connection grabbing the page
    uClient = uReq(medex_url)
    html_page = uClient.read()
    uClient.close()

    # HTML parsing
    page_soup = soup(html_page, 'html.parser')

    # getting every container containing medicine details
    containers = page_soup.findAll('div', {'class': 'row data-row'})

    for container in containers:
        # Getting medicine name
        medicine_name = container.div.text.strip()

        # Getting medicine quantity
        quantity = container.findAll(
            'span', {'class': 'grey-ligten'})[0].text.strip()

        # Getting chemichal name
        chemical_name = container.findAll('div')[2].text.strip()

        # Getting company name
        compnay_name = container.findAll(
            'span', {'class': 'data-row-company'})[0].text.strip()

        # Getting price
        unit_price = container.findAll(
            'div', {'class': 'package-container'})[0].text.strip()

        unit_price.replace(' ', '')

        f.write(medicine_name + ',' + quantity + ',' +
                chemical_name.replace(',', '|') + ',' + compnay_name + ',' + ' '.join(unit_price.split()) + '\n')

    page_number+1
    print('done: page' + str(page_number))

f.close()
