from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# filename = "individual-medicine-details.csv"
# f = open(filename, 'w')

# column_title = 'Medicine Name, Quantity, Chemical Name, Compnay Name, Unit Price\n'

# f.write(column_title)

for page_number in range(8, 9):
    medex_url = 'https://medex.com.bd/brands?page=' + str(page_number)

    uClient = uReq(medex_url)
    html_page = uClient.read()
    uClient.close()

    page_soup = soup(html_page, 'html.parser')

    containers = page_soup.findAll(
        'a', {'class': 'hoverable-block'})

    details_containers = []

    # Getting individual url
    for container in containers:
        details_url = container['href']

        uClient = uReq(details_url)
        details_page = uClient.read()
        uClient.close()

        details_page_soup = soup(details_page, 'html.parser')

        details_containers.append(details_page_soup.find(
            'div', {'class': 'row'}))

    medicine_name = ''
    generic_name = ''
    strength = ''
    manufacturer = ''
    unit_price = ''

    dosage_informations = []

    for details_container in details_containers:
        brand_header = details_container.div.div.div

        medicine_name = brand_header.h1.text.strip()

        medicine_name.replace(' ', '')
        # ' '.join(medicine_name.split())

        generic_name = brand_header.findAll('div')[0].text.strip()
        strength = brand_header.findAll('div')[1].text.strip()
        manufacturer = brand_header.findAll('div')[2].text.strip()

        unit_price = details_container.findAll(
            'div', {'class': 'package-container'})[0].text.strip()

        unit_price.replace(' ', '')

        # Dosage information
        dosage_informations.append(details_container.find(
            'div', {'class': 'col-xs-12 col-sm-12 col-md-12 col-lg-12'}))

    print(medicine_name, generic_name, strength,
          manufacturer, ' '.join(unit_price.split()))

    # for dosage_information in dosage_informations:
    print(dosage_informations[0])

    page_number + 1
