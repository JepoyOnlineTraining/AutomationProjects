import requests


def test_soap_api_data_access():
    url = "http://www.dneonline.com/calculator.asmx"
    header = {'Content-Type':'text/xml; charset=utf-8'}
    a = 1
    b = 2

    soap_body = f"""
        <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <Add xmlns="http://tempuri.org/">
              <intA>{a}</intA>
              <intB>{b}</intB>
            </Add>
          </soap:Body>
        </soap:Envelope>
    """

    soap_body = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n  <soap:Body>\n    <IsValidISBN13 xmlns=\"http://webservices.daehosting.com/ISBN\">\n      <sISBN>978-1-4612-9090-2</sISBN>\n    </IsValidISBN13>\n  </soap:Body>\n</soap:Envelope>"
    print(soap_body)
    # response = requests.post(url=url, headers=header, data=soap_body)
    response = requests.request("POST", url, data=soap_body,  headers=header,)
    response.raise_for_status()
    print(response.content)
