import requests

def test_this():
    url = "http://webservices.daehosting.com/services/isbnservice.wso"
    # url = "http://www.dneonline.com/calculator.asmx"
    #
    payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n  <soap:Body>\n    <IsValidISBN13 xmlns=\"http://webservices.daehosting.com/ISBN\">\n      <sISBN>978-1-4612-9090-2</sISBN>\n    </IsValidISBN13>\n  </soap:Body>\n</soap:Envelope>"
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    a = 1
    b = 2

    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    print(response.content)
    print(response.text)
