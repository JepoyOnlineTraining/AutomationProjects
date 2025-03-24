

import requests
from xml.etree import ElementTree as ET

def test_something():
    url = "http://webservices.daehosting.com/services/isbnservice.wso"
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    pay_load = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <IsValidISBN13 xmlns="http://webservices.daehosting.com/ISBN">
          <sISBN>9781461290902</sISBN>
        </IsValidISBN13>
      </soap:Body>
    </soap:Envelope>"""
    response = requests.post(url, headers=headers, data=pay_load)
    print(response.content)

    tree = ET.fromstring(response.content)

    namespace = {'m': 'http://webservices.daehosting.com/ISBN'}
    result_tree = tree.find(".//m:IsValidISBN13Result", namespaces=namespace)
    print(f" Result text: {result_tree.text}")