

<div id="admin-lines-modal" class="modal">
    <div  class="modal-content">
        <div>
        <h1 class="modal-title">Add a line</h1>
        <form class='addline-form' method='post'>
    
    
        <?php
                require('db.php');   
                // When form submitted, insert values into the database.
               
                $sql = "INSERT INTO `assemblylines` (`did`, `line-id`) 
                VALUES ($did, $linenumber) 
                if ($con->query($sql) === TRUE) {
                echo "New record created successfully";
                } else {
                        echo "Error: " . $sql . "<br>" . $con->error;
                }
                //$con->close();
                echo "This is a test";
                }
               

        //close the sql connection
        $con->close();
}

function checkInput($input){
	return isset($_POST[$input]);
}
function getValue($input){
    if($_POST[$input] !=NULL){
        return $_POST[$input];
    }else{
        return 0;
    }
}
?>
               
<?php

            //list department and did from database table 
        $query    = "SELECT * FROM `departments`";
        
        $result = mysqli_query($con, $query) or die(mysql_error());
        
        $rowCount = mysqli_num_rows($result);
        
        if($rowCount > 0){
            echo "<select>";
            while( $row = $result->fetch_assoc()) {
              echo "<option name='did' value='".htmlspecialchars($row['did'])."'>".htmlspecialchars($row['dname'])."</option>";
            }            
        }  
?>
        </select>
        <br>
        <input style='width: 80px;' name='linenumber' value='' type='text' placeholder='AS0000'>
        <br>
        <input type="submit" name="submit" value="Add Line" class="login-button">
        </form>
  
        </div>
        </div>
        </div>



            
