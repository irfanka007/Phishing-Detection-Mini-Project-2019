<!DOCTYPE html>
<html lang="en">
<head>
  <title>PhiDet-PY</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
#mySidenav a {
  position: absolute;
  left: -90px;
  transition: 0.5s;
  padding: 15px;
  width: 300px;
  text-decoration: none;
  font-size: 20px;
  color: white;
  border-radius: 0 5px 5px 0;
  margin-top: 50px
}
.sidenav{
  left: 90px;
  position: fixed;
}


#mySidenav a:hover {
  left: 0;
}


#checkurl {
  top: -40px;
  background-color: #f44336;
}
#web {
  top: 20px;
  background-color: #4CAF50;
}

#bagging {
  top: 80px;
  background-color: #3555a1;
}
#boosting {
  top: 140px;
  background-color: #a8a80f;
}
#staking {
  top: 200px;
  background-color: #801467;
}

#about {
  top: 260px;
  background-color: #555;
}

#col4{
  
  align-self: center;
  text-align: center;
}

</style>
</head>
<body>

<div class="jumbotron text-center">
  <h1 style="text-align: center;">PHIDET-PY</h1>
  <p style="text-align: center;">Get a free, automated website analysis</p> 
</div>
  
<div class="container">
  
  <div class="row">

  <div id="mySidenav" class="sidenav">
  <a href="index.php" id="checkurl">Home</a>  
  <a href="check.php" id="checkurl">Check URL</a>
  <a href="details.php" id="web">Web Details</a>
  <a href="bagging.php" id="bagging">Bagging</a>
  <a href="boosting.php" id="boosting">Boosting</a>
  <a href="staking.php" id="staking">Staking</a>
  <a href="about.php" id="about">About System</a>





  </div>

    <div style="align-self: center;text-align: center;margin-top: 100px" >

      <h3>URL ANALYSER</h3>

      <input type="text" name="url" placeholder="enter URL Here" style="border:2px solid #456879;border-radius:20px;height: 50px;width: 600px; text-align: center; margin-top: 30px; font-size: 20px"/>
      
      
    </div>
    
  </div>
</div>

</body>
</html>
