

<?php
    // Enter your host name, database username, password, and database name.
    // If you have not set database password on localhost then set empty.
    $con = mysqli_connect("mysql","root","example1","webpts");
    $conn = $con;
    // Check conection
    if (mysqli_connect_errno()){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
    }
    if (session_status() == PHP_SESSION_NONE) {
        session_start();
     }


            
?>

