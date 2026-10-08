from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>PEP Cloud & DevOps</title>
        </head>
        <body>
            <h1>🚀 PEP Cloud & DevOps CI/CD Project</h1>
            <p>Docker container is running successfully!</p>
            <p>Deployed using Terraform + AWS EC2</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)