<div id="downtime-modal" class="modal">
    <div  class="modal-content">
        <div>
            <h1 class="modal-title">Downtime</h1>                    
            <form id="downtime" action="main.php" method="post">
                
<table>
<thead>
        <tr>
        <th>Run</th>
        <th>Machine</th>
        <th>Product Number</th>
        <th>Stop Time</th>
        <th>Start Time</th>
        <th>Totals</th>
        <th>Fcode</th>
        <th># of TM</th>
        <th>Han-Cho</th>
        <th>Shoku-Cho</th>
        <th>Maintenace</th>
        <th>Ko-Cho</th>
        <th>Explanation of Trouble</th>
        <th>P/U</th>
        </tr>
</thead>
<tbody>
        <tr>
        <td>    <input style="width:30px;" name="run" value="" type="number" placeholder="0"></td>
        <td>    
            
<!--         
        
                <select style="width:45;" name="Machine">
                        <option value="HM1">HM1</option>
                        <option value="HM2">HM2</option>
                        <option value="AS0003">AS0003</option>
                        <option value="AS0004">AS0004</option>
                        <option value="ASA">ASA</option>
                        <option value="RA">RA</option>
                        <option value="BP">BP</option>
                        <option value="SI">SI</option>
                        <option value="FPS">FPS</option>
                        <option value="TF1">TF1</option>
                        <option value="TF2">TF2</option>
                        <option value="HT">HT</option>
                        <option value="NT">NT</option>
                        <option value="LE">LE</option>
                </select>
 -->

                    <!-- somehow this needs to refrence pauid to know what line to show machines from -->
                            <?php
                                $query    = "SELECT * FROM `machines`";
                                $result = mysqli_query($con, $query) or die(mysql_error());
                                $rowCount = mysqli_num_rows($result);
                                
                                if($rowCount > 0){
                                    echo "<label for='ddl_machine'></label>"; 
                                    echo "<select name='machine' id='ddl_machine'>";
                                    while( $row = $result->fetch_assoc()) {
                                        echo "<option>".htmlspecialchars($row['machine-name'])."</option>";
                                    }
                                    echo "</select>";
                                }
                            ?> 


        </td>
        <td>    <input style="width: 111px;" name="product number" value="" type="number" placeholder="482828-10210"></td>
        <td>    <input style="width:120px;" name="stoptime" value="" type="time" placeholder="0"></td>
        <td>    <input style="width:120px;" name="starttime" value="" type="time" placeholder="0"></td>
        <td>    <input style="width:45px;" name="totals" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="fcode" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="tm" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="hancho" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="shoko" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="maintenance" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:45px;" name="kocho" value="" type="number" placeholder="0"></td>
        <td>    <input style="width:500px;" name="trouble" value="" type="text" placeholder="Explanation of Trouble"></td>
        <td>    <input style="width:45px;" name="pu" value="" type="number" placeholder="0"></td>        
        </tr>
                   <!-- temporary-php-to-see-what-look-lik -->
                    <?php
                        for ($i = 0; $i <= 20; $i++) {
                                echo '        <tr>
                                <td>    <input style="width:30px;" name="run" value="" type="number" placeholder="0"></td>
                                <td>    <select style="width:45;" name="Machine">
                                                <option value="HM1">HM1</option>
                                                <option value="HM2">HM2</option>
                                                <option value="AS0003">AS0003</option>
                                                <option value="AS0004">AS0004</option>
                                                <option value="ASA">ASA</option>
                                                <option value="RA">RA</option>
                                                <option value="BP">BP</option>
                                                <option value="SI">SI</option>
                                                <option value="FPS">FPS</option>
                                                <option value="TF1">TF1</option>
                                                <option value="TF2">TF2</option>
                                                <option value="HT">HT</option>
                                                <option value="NT">NT</option>
                                                <option value="LE">LE</option>
                                        </select>
                                </td>
                                <td>    <input style="width: 111px;" name="product number" value="" type="number" placeholder="482828-10210"></td>
                                <td>    <input style="width:120px;" name="stoptime" value="" type="time" placeholder="0"></td>
                                <td>    <input style="width:120px;" name="starttime" value="" type="time" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="totals" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="fcode" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="tm" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="hancho" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="shoko" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="maintenance" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:45px;" name="kocho" value="" type="number" placeholder="0"></td>
                                <td>    <input style="width:500px;" name="trouble" value="" type="text" placeholder="Explanation of Trouble"></td>
                                <td>    <input style="width:45px;" name="pu" value="" type="number" placeholder="0"></td>        
                                </tr>';
                        }
                    ?>
</tbody>
                    

                    

                </table>
                <input type="button" name="downtimeokbutton" value="OK" id="downtimeokbutton">
                <input type="button" class="close-modal" name="downtimebackbutton" value="Close" id="downtimeclosebutton">                
            
            </form>
        </div>
    </div>
</div>
