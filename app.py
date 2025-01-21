import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import threading  # For running the server in a separate thread

# Path to the History folder
HISTORY_FOLDER = "./History"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress logging to the console

    def do_GET(self):
        if self.path == "/":  # Serve the main page
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            # Dynamically generate the HTML for the file list
            file_list = os.listdir(HISTORY_FOLDER)
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>History Files</title>
                <style>
                    body {{
                        background-color: black;
                        color: white;
                        font-family: Arial, sans-serif;
                    }}
                    h1 {{
                        text-align: center;
                    }}
                    #file-list {{
                        width: 80%;
                        margin: 20px auto;
                        padding: 10px;
                        background-color: #333;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                    }}
                    #file-list ul {{
                        list-style: none;
                        padding: 0;
                    }}
                    #file-list li {{
                        padding: 8px;
                        border: 1px solid #555;
                        margin-bottom: 5px;
                        cursor: pointer;
                        border-radius: 4px;
                    }}
                    #file-list li:hover {{
                        background-color: #555;
                    }}
                </style>
            </head>
            <body>
                <h1>War History</h1>
                <div id="file-list">
                    <h2>View Past Battles</h2>
                    <ul>
                        {''.join(f'<li><a href="/file/{file}" style="color: white; text-decoration: none;">{file}</a></li>' for file in file_list)}
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))

        elif self.path.startswith("/file/"):  # Serve the content of a specific file
            file_name = self.path.split("/file/")[1]
            file_path = os.path.join(HISTORY_FOLDER, file_name)

            if os.path.exists(file_path) and os.path.isfile(file_path):
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().replace("✔", "&check;").replace("✘", "&cross;")
                    self.wfile.write(f"<pre>{content}</pre>".encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found.")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found.")

def run(port=8000):
    def start_server():
        server_address = ("", port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        httpd.serve_forever()

    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True  # This ensures the thread will exit when the main program exits
    server_thread.start()

    # Automatically open the browser
    webbrowser.open(f"http://localhost:{port}/")

# Main script
if __name__ == "__main__":
    run_server(port=8000)
    print("Web server started and browser opened. Exiting main script...")

