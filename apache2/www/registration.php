<!DOCTYPE html>
<!-- doctype is required -->
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>Registration</title>
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
<?php
    require('db.php');
    // When form submitted, insert values into the database.
    if (isset($_REQUEST['username'])) {
        // removes backslashes
        $username = stripslashes($_REQUEST['username']);
        //escapes special characters in a string
        $username = mysqli_real_escape_string($con, $username);
        $email    = stripslashes($_REQUEST['email']);
        $email    = mysqli_real_escape_string($con, $email);

        $name    = stripslashes($_REQUEST['name']);
        $name    = mysqli_real_escape_string($con, $name);

        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con, $password);
        $create_datetime = date("Y-m-d H:i:s");
        $query    = "INSERT into `users` (username, password, email, create_datetime, name)
                     VALUES ('$username', '" . md5($password) . "', '$email', '$create_datetime', '$name')";
        $result   = mysqli_query($con, $query);
         if ($result) {
            echo "<div class='reg-form'>
                  <h3 class='login-title'>You are registered successfully.</h1><br/>
                  <p class='link'>Click here to <a href='login.php'>Login</a></p>
                  </div>";
        } else {
            echo "<div class='reg-form'>
                  <h3 class='login-title'>Required fields are missing.</h1><br/>
                  <p class='link'>Click here to <a href='registration.php'>registration</a> again.</p>
                  </div>";
        }
    } else {

    }   
?>
    <form class="reg-form" action="" method="post">
        <h1 class="login-title">Registration</h1>
        <input type="text" class="login-input" name="username" placeholder="AEILXXXX" required />
        <input type="text" class="login-input" name="name" placeholder="Name" required />
	<input type="text" class="login-input" name="email" placeholder="Email Adress">
        <input type="password" class="login-input" name="password" placeholder="Password">
        <input type="submit" name="submit" value="Register" class="login-button">
        <p class="link">Already have an account? <br><a href="login.php">Login here</a></p>
    </form>
    
</body>
</html>