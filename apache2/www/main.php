<?php
//include auth_session.php file on all user panel pages
require("auth_session.php");
?>
<!DOCTYPE html>
<!-- doctype is required -->
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>webpts</title>
    <meta name="description" content="web based production tracking system">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/main.css" type="text/css" charset="utf-8" />
    <script src="/scripts/jquery.js"></script>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="/scripts/bootstrap.min.js"></script>
    <script src="/scripts/jquery.mask.js"></script>
    <link rel="stylesheet" href="css/main.css" type="text/css" charset="utf-8" />
</head>

<body>
    
    <?php include("menu.php");?> 

    <div class="container">
        <div class="row">
            <div class="col-sm-6">
            <!-- start of block1 div-->
            <div name=block1 class="rounded-block"
                style="width:450px; flex-grow:1; font-size:10px; text-align:left; ">
                <h1
                    style="margin-top:0px; padding:5px 15px; font-size:25px; color:rgba(0,0,0,.75); background-color:#ccc">
                    Prodcution Actual Record</h1>
                <br></br>
                <h2 style="display:inline-block; color:rgba(0,0,0,.75); background-color:#ccc">user:
                    <?php echo $_SESSION['username']; ?>
                </h2>
                <br></br>
                <!--make hr go up table go down?-->
                <table style="letter-spacing:2px; display:block; padding:10px; font-size:15px; width:100%; border-top: 2px solid #09c;">
                    <tr>
                        <td width="150px">Line#</td>
                        <td>
                            <?php echo $_SESSION['line']; ?>
                        </td>
                    </tr>
                    <tr>
                        <td>Date:</td>
                        <td>
                            <?php echo $_SESSION['date']; ?>
                        </td>
                    </tr>
                    <tr>
                        <td>Han-Cho:</td>
                        <td>
                            <?php echo $_SESSION['name']; ?>
                        </td>
                    </tr>
                    <tr>
                        <td>Shift:</td>
                        <td>
                            <?php echo $_SESSION['shift']; ?>
                        </td>
                    </tr>
                </table>
            </div>
            </div>
            <div class="col-sm-6">
                <!-- include block 2 datatable -->
                <?php include("block2.php");?>
            </div>
            
        </div>
        <div class="row">
            <div class="col-sm-12">   
                <!-- include block 3 datatable -->
                <?php include("block3.php");?>
            </div>
        </div>
    </div>

    

    

    <div class="save-message">
        <span>All data was saved</span>
    </div>
    



</body>
    <script src="/scripts/main.js"></script>
</html>