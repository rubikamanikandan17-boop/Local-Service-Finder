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
                background:#f2f2f2;
                font-family:Arial;
                text-align:center;
            }

            h1{
                color:#0066cc;
            }

            .box{
                width:500px;
                margin:auto;
                background:white;
                padding:20px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }

            input{
                width:80%;
                padding:10px;
            }

            button{
                background:blue;
                color:white;
                padding:10px;
                border:none;
                border-radius:5px;
            }

            ul{
                list-style:none;
            }

            li{
                padding:10px;
            }

        </style>

    </head>


    <body>

        <h1>Local Service Finder</h1>
        
        <button>Login</button>

        <br><br>
        
        <div class="box">

        <h3>Find Services Near You</h3>

        <input type="text" placeholder="Search service">

        <br><br>

        <button>Search</button>

        <ul>

            <li>🔧 Electrician ⭐4.8</li>

            <li>🚰 Plumber ⭐4.7</li>

            <li>🚗 Mechanic ⭐4.9</li>

            <li>🧹 Cleaner ⭐4.6</li>

            <li>🎨 Painter ⭐4.5</li>

            <li>🪚 Carpenter ⭐4.7</li>

        </ul>

        </div>

    </body>

    </html>

    '''


if __name__ == '__main__':
    app.run(debug=True)