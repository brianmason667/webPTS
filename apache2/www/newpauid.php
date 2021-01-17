<!-- this file was pulled directly from newpauid.php  -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/main.css" type="text/css" charset="utf-8" />
    <link rel="stylesheet" href="css/id.css" type="text/css" charset="utf-8" />
    <link rel="stylesheet" href="css/class.css" type="text/css" charset="utf-8" />

</head>
<body>
<?php require("auth_session.php")?>    
<?php require("db.php");

if(isset($_POST["date"]) && isset($_POST["line"]) && isset($_POST["shift"])){
  $date = strtotime($_POST["date"]);
  $date = date('Y-m-d',$date);
	$line= $_POST["line"];
	$shift= $_POST["shift"];
	$userid= $_SESSION['userid'];
$sql = "INSERT INTO `PAUID` (`date`, `line`, `shift`, `userid`) VALUES ('$date', '$line', '$shift', $userid)";

if ($con->query($sql) === TRUE) {
//  echo "New record created successfully";

$_SESSION["pauid"]=$con -> insert_id;  
$_SESSION["line"]=$line;

$showDate = strtotime($_POST["date"]);
$showDate = date('m/d/Y',$showDate);

$_SESSION["date"]=$showDate;
$_SESSION["shift"]=$shift;

echo "<script>window.location.href='main.php'; </script>";
} else {
  echo "Error: " . $sql . "<br>" . $con->error;
}
$con->close();
}
?>

</body>
</html>




