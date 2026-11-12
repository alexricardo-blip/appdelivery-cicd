import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSAO = "2.0"

class AppDelivery(BaseHTTPRequestHandler):
    def do_GET(self):
        mensagem = f"AppDelivery CI-CD AUTOMATICO! Versao {VERSAO}"

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(mensagem.encode("utf-8"))

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8080))
    servidor = HTTPServer(("0.0.0.0", porta), AppDelivery)
    print(f"AppDelivery iniciado na porta {porta}")
    servidor.serve_forever()
