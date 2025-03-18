import requests


def test_soap_api_data_access():
    url = "http://www.dneonline.com/calculator.asmx"
    headers = {'Content-Type':'text/xml; charset=utf-8'}

    soap_body = """
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="http://tempuri.org/">
      <intA>4</intA>
      <intB>4</intB>
    </Add>
  </soap:Body>
</soap:Envelope>
    """

    response = requests.post(url=url, headers=headers, data=soap_body)
    response.raise_for_status()
    print(response.content)
