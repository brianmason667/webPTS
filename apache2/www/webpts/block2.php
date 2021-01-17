        <?php 
//inlcude the db connection
require("db.php");
$pauid = $_SESSION["pauid"];
if($pauid != null){
        if(checkInput("hour1input")){
                $hour1input = getValue("hour1input");
                $hour2input = getValue("hour2input");
                $hour3input = getValue("hour3input");
                $hour4input = getValue("hour4input");
                $hour5input = getValue("hour5input");
                $hour6input = getValue("hour6input");
                $hour7input = getValue("hour7input");
                $hour8input = getValue("hour8input");
                $hour9input = getValue("hour9input");
                $hour10input = getValue("hour10input");
                $hour11input = getValue("hour11input");
                $hour12input = getValue("hour12input");
                $sql = "INSERT INTO `HOURLY` (`pauid`, `Hour1`, `Hour2`, `Hour3`, `Hour4`, `Hour5`, `Hour6`, `Hour7`, `Hour8`, `Hour9`, `Hour10`, `Hour11`, `Hour12`) 
                VALUES ($pauid, $hour1input, $hour2input, $hour3input, $hour4input, $hour5input, $hour6input, $hour7input, $hour8input, $hour9input, $hour10input, $hour11input, $hour12input) 
                ON DUPLICATE KEY UPDATE Hour1=$hour1input, Hour2=$hour2input, Hour3=$hour3input, Hour4=$hour4input, 
                Hour5=$hour5input, Hour6=$hour6input, Hour7=$hour7input, Hour8=$hour8input, Hour9=$hour9input, Hour10=$hour10input,Hour11=$hour11input, Hour12=$hour12input";
                if ($con->query($sql) === TRUE) {
                echo "New record created successfully";
                } else {
                        echo "Error: " . $sql . "<br>" . $con->error;
                }
                //$con->close();
                echo "This is a test";
                }
                //get the current
                $query = "SELECT * FROM `HOURLY` WHERE pauid='$pauid'";
                $result = mysqli_query($con, $query) or die(mysql_error());
                $rows = mysqli_num_rows($result);
                if ($rows > 0) {
                        while($row = $result->fetch_assoc()) {
                                $hour1 = $row["Hour1"];
                                $hour2 = $row["Hour2"];
                                $hour3 = $row["Hour3"];
                                $hour4 = $row["Hour4"];
                                $hour5 = $row["Hour5"];
                                $hour6 = $row["Hour6"];
                                $hour7 = $row["Hour7"];
                                $hour8 = $row["Hour8"];
                                $hour9 = $row["Hour9"];
                                $hour10 = $row["Hour10"];
                                $hour11 = $row["Hour11"];
                                $hour12 = $row["Hour12"];
                        }
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

<?php if($pauid != null):?>
        
        <div name="block2" id="block2" class="block2 rounded-block center-text" style="padding:10px;">


<form id="hourly" action="main.php" method="post">
        <table style="boarder:1px;">
        <tr>
                <td>
                <!--required td for blankspace -->
                </td>
                <td>Hour 1</td>
                <td>Hour 2</td>
                <td>Hour 3</td>
                <td>Hour 4</td>
                <td>Hour 5</td>
                <td>Hour 6</td>
                <td>Hour 7</td>
                <td>Hour 8</td>
                <td>Hour 9</td>
                <td>Hour 10</td>
                <td>Hour 11</td>
                <td>Hour 12</td>
        </tr>
        <tr>
                <td>Pcs/Per/Hour</td>
                <td><input style="" name="hour1input" value="<?php echo $hour1;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour2input" value="<?php echo $hour2;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour3input" value="<?php echo $hour3;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour4input" value="<?php echo $hour4;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour5input" value="<?php echo $hour5;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour6input" value="<?php echo $hour6;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour7input" value="<?php echo $hour7;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour8input" value="<?php echo $hour8;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour9input" value="<?php echo $hour9;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour10input" value="<?php echo $hour10;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour11input" value="<?php echo $hour11;?>" type="number" placeholder="0"></td>
                <td><input style="" name="hour12input" value="<?php echo $hour12;?>" type="number" placeholder="0"></td>
        </tr>
        <tr>
                <td>Cumulative Pcs.</td>
                <td><input id="calchour1" style=""  type="number" placeholder="0" disabled></td>
                <td><input id="calchour2" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour3" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour4" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour5" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour6" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour7" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour8" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour9" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour10" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour11" style="" type="number" placeholder="0" disabled></td>
                <td><input id="calchour12" style="" type="number" placeholder="0" disabled></td>
        </tr>
        </table>
        <!-- <input type="submit" name="hourlyokbutton" value="OK" id="hourlyokbutton"> -->
</form>


<!-- form end tag required -->
</div>
<!-- end block2 div -->

<?php endif; ?>