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
background:#f2f2f2;
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
cursor:pointer;

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


<a href="/login">

<button>Login</button>

</a>



<div class="box">


<h3>Find Services Near You</h3>



<input type="text"

id="service"

placeholder="Search Service">


<br><br>


<button onclick="searchService()">

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



<script>

function searchService(){


var service=document.getElementById("service").value;



if(service=="Electrician"){

alert("Electrician Available ⭐4.8");

}


else if(service=="Plumber"){

alert("Plumber Available ⭐4.7");

}


else if(service=="Mechanic"){

alert("Mechanic Available ⭐4.9");

}


else if(service=="Cleaner"){

alert("Cleaner Available ⭐4.6");

}


else if(service=="Painter"){

alert("Painter Available ⭐4.5");

}


else if(service=="Carpenter"){

alert("Carpenter Available ⭐4.7");

}


else{

alert("Service Not Found");

}

}


</script>



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
background:#f2f2f2;
text-align:center;

}


.box{

width:350px;
margin:auto;
margin-top:100px;
background:white;
padding:20px;
border-radius:10px;
box-shadow:0 0 10px gray;

}


input{

width:90%;
padding:10px;
margin:10px;

}


button{

background:blue;
color:white;
padding:10px;
border:none;
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