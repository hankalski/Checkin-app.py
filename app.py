from flask import Flask
app = Flask(__name__)

@app.route("/")
def function_def(x):
    y = x/math.sin(x)

    if math.sin(x) !=0:
        return 'Функция выполнима'

if __name__ == "__main__":
    app.run()
