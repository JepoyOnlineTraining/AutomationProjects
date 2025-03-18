import requests
from xml.etree import ElementTree as ET



def test_soap_api():

    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'Content-Type': 'text/xml; charset=utf-8'}

    soap_body = """
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Add xmlns="http://tempuri.org/">
          <intA>5</intA>
          <intB>10</intB>
        </Add>
      </soap:Body>
    </soap:Envelope>
    """

    try:
        response = requests.post(url=url, headers=headers, data=soap_body)
        response.raise_for_status()

        tree = ET.fromstring(response.content)

        result_element = tree.find(".//{http://tempuri.org/}AddResult")

        if result_element is not None:
            result = int(result_element.text)
            assert result == 15, f"Expected 15, but got {result}"
            print(f"SOAP request successful. Result: {result}")
        else:
            print("AddResult element not found in response.")
            assert False, "AddResult element not found in response."

    except requests.exceptions.RequestException as e:
        print(f"SOAP request failed: {e}")
        assert False, f"Request exception: {e}"
    except ET.ParseError as e:
        print(f"Error parsing XML response: {e}")
        assert False, f"XML Parsing error: {e}"