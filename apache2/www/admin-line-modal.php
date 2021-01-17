

<div id="admin-lines-modal" class="modal">
    <div  class="modal-content">
        <div>
        <h1 class="modal-title">Add a line</h1>
        <form class='addline-form' method='post'>
    
    
        <?php
    require("db.php");   
      
            //list department and did from database table 
        $query = "SELECT * FROM `departments`";
        
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