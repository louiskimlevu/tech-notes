from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def print_request():
    print("Received request:")
    print(request.method, request.url, request.headers, request.get_data())

    method = request.method
    url = request.url
    headers = str(request.headers)
    data = request.get_data().decode('utf-8')

    return render_template('index.html', method=method, url=url, headers=headers, data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

