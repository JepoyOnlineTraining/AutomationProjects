import pytest
import requests
from xml.etree import ElementTree as ET



def test_daehosting_01():

    try:
        base_url = "http://webservices.daehosting.com/services/isbnservice.wso"
        headers = {'Content-Type': 'text/xml; charset=utf-8'}
        soap_body = """
        <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <IsValidISBN13 xmlns="http://webservices.daehosting.com/ISBN">
              <sISBN>9781461290902</sISBN>
            </IsValidISBN13>
          </soap:Body>
        </soap:Envelope>
        """
        response = requests.get(url=base_url, headers=headers, data=soap_body)
        response.raise_for_status()
        print(response.content)

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")