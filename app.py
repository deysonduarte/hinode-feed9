from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def feed():
    xml_url = "https://www.hinode.com.br/XMLData/consultores.xml"

    try:
        response = requests.get(xml_url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code == 200:
            xml_content = response.content.decode("utf-8")

            html_response = f"""<?xml version="1.0" encoding="UTF-8"?>
            <html>
            <head>
            <meta name="google-site-verification" content="zVD5PLGcdIn_0knHPPc-vjJxvPktFIWCH3k3fbiDqKs" />
            </head>
            <body>
            {xml_content}
            </body>
            </html>
            """

            return Response(html_response, mimetype='application/xml')
        else:
            return f"Erro ao buscar XML: {response.status_code}", 500
    except Exception as e:
        return f"Erro inesperado: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
