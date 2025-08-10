from flask import Flask, render_template
import connexion

app = connexion.App(__name__, specification_dir='./config')
app.add_api('swagger.yml')


@app.route('/', methods=['GET'])
def index():
    """ just a index page """
    return render_template('hello.html')


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5001
    print(f'Server is running at {host}:{port}')
    app.run(host=host, port=port)
