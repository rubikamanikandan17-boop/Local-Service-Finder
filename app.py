from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Local Service Finder</title>

        <style>
            body{
                font-family:Arial;
                text-align:center;
                background:#f4f4f4;
            }

            .box{
                width:500px;
                margin:auto;
                margin-top:40px;
                padding:20px;
                background:white;
                border-radius:10px;
                box-shadow:0 0 10px lightgray;
            }

            button{
                background:#2563eb;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:5px;
                cursor:pointer;
            }

            input{
                width:80%;
                padding:10px;
            }

            ul{
                list-style:none;
                padding:0;
            }

            li{
                padding:8px;
            }

        </style>

    </head>

    <body>

        <h1>Local Service Finder</h1>

        <a href="/login">
            <button>Login</button>
        </a>

        <div class="box">

            <h3>Find Services Near You</h3>

            <input type="text"
            placeholder="Search service">

            <br><br>

            <button onclick="alert('Searching...')">
            Search
            </button>

            <ul>

                <li>⚡ Electrician ⭐4.8</li>

                <li>🚰 Plumber ⭐4.7</li>

                <li>🚗 Mechanic ⭐4.9</li>

                <li>🧹 Cleaner ⭐4.6</li>

                <li>🎨 Painter ⭐4.5</li>

                <li>🔨 Carpenter ⭐4.7</li>

            </ul>

        </div>

    </body>

    </html>
    '''


@app.route('/login')
def login():
    return '''
    <!DOCTYPE html>

    <html>

    <head>

        <title>Login</title>

        <style>

            body{
                font-family:Arial;
                text-align:center;
                background:#f4f4f4;
            }

            .box{
                width:350px;
                margin:auto;
                margin-top:100px;
                padding:20px;
                background:white;
                border-radius:10px;
                box-shadow:0 0 10px lightgray;
            }

            input{
                width:90%;
                padding:10px;
                margin:10px;
            }

            button{
                background:#2563eb;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:5px;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <h2>Login</h2>

            <input type="text"
            placeholder="Username">

            <input type="password"
            placeholder="Password">

            <br>

            <button onclick="alert('Login Successful')">
            Login
            </button>

            <br><br>

            <a href="/">Back to Home</a>

        </div>

    </body>

    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)