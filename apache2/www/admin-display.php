<?php
//include auth_session.php file on all user panel pages
require("auth_session.php");
include("php_table.php");
?>
<!DOCTYPE html>
<!-- doctype is require -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Put this page description here">
    <script src="/scripts/jquery.js"></script>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="/scripts/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/main.css" type="text/css" charset="utf-8" />
    <script src="/scripts/jquery.mask.js"></script>
    <title>Display</title>
</head>
<body>
 
<?php include("menu.php");?>


    <div class="jumbotron text-center">
        <h1>Display </h1>
        <p>Select Department, line, Machine to display the Downtime/Defect codes</p>
        
        
        <div class="row small-form">
                <div class="col-sm-4">
                        <?php
                        include('db.php');
                        $query    = "SELECT * FROM `departments`";
                        $result = mysqli_query($con, $query) or die(mysql_error());
                        $rowCount = mysqli_num_rows($result);
                        
                        if($rowCount > 0){
                            echo "<label for='ddl_department'>Select Department</label>"; 
                            echo "<select name='department' id='ddl_department'>";
                            while( $row = $result->fetch_assoc()) {
                                echo "<option>".htmlspecialchars($row['dname'])."</option>";
                            }
                            echo "</select>";
                        }
                    ?>
                </div>

                <div class="col-sm-4">
                            <?php
                                $query    = "SELECT * FROM `assemblylines`";
                                $result = mysqli_query($con, $query) or die(mysql_error());
                                $rowCount = mysqli_num_rows($result);
                                
                                if($rowCount > 0){
                                    echo "<label for='ddl_line'>Select Line</label>"; 
                                    echo "<select name='line' id='ddl_line'>";
                                    while( $row = $result->fetch_assoc()) {
                                        echo "<option>".htmlspecialchars($row['line-id'])."</option>";
                                    }
                                    echo "</select>";
                                }
                            ?>   
                </div> 

                <div class="col-sm-4">
                            <?php
                                $query    = "SELECT * FROM `machines`";
                                $result = mysqli_query($con, $query) or die(mysql_error());
                                $rowCount = mysqli_num_rows($result);
                                
                                if($rowCount > 0){
                                    echo "<label for='ddl_machine'>Select Machine</label>"; 
                                    echo "<select name='machine' id='ddl_machine'>";
                                    while( $row = $result->fetch_assoc()) {
                                        echo "<option>".htmlspecialchars($row['machine-name'])."</option>";
                                    }
                                    echo "</select>";
                                }
                            ?>   
                </div> 
         </div>               
         
    </div>  
    
                <div class="container">

                    <div class="row">
                        <div class="col-sm-12">
                              <div class="">
                                <?php makeDataGrid("SELECT `line-id`, `did` FROM assemblylines");?>
                                <?php makeDataGrid("SELECT `line-id`, `machine`, `4M`, `downtime-code`, `PU`,`downtime-description`, `standard-time` FROM downtimecodes");?>
                                <?php makeDataGrid("SELECT `line-id`, `machine`, `4M`, `defect-code`, `defect-description` FROM defectcodes");?>
                                <?php makeDataGrid("SELECT `line-id`, `part-number`, `num-of-tm`, `ct` FROM products");?>
                                
                              </div>

                         

                        </div>
                    </div>

          
                    <!-- <div class="row">   
                            <div class="col-sm-3">
                            <h3>lines</h3>        
                            <ul>
                                <li>line1</li>
                                <li>line2</li>
                                <li>line3</li>
                            </ul>
                            </div>
                            
                      
                            <div class="col-sm-3">
                            <h3>machines </h3>
                            <ul>
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                            </ul>
                            </div>
                        
                   
                            <div class="col-sm-3">
                            <h3>Defect Codes </h3>
                            <ul>
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                            </ul>
                            </div>
                          
                            
                            <div class="col-sm-3">
                            <h3>Fault Codes </h3>
                            <ul>
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                                <li>machine 1</li>
                                <li>machine 2</li>
                                <li>...</li>
                                
                            </ul>
                            </div>
                    </div>
                </div>       -->
    
</body>

 <script src="/scripts/main.js"></script>
</html>
