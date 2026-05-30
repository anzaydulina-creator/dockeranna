from flask import Flask
app = Flask('pythonweb')
@app.route('/')
def page():
    return 'ww!'

app.run(host='0.0.0.0' , port= 8098)
