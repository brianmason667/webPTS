<div id="defect-modal" class="modal">
    <div class="modal-content">
        <div>
            <span></span>
            <h1 class="modal-title">Defects</h1>


            <form id="defects-form" action="main.php" method="post">
                <table style="border:1px;">
                    <tr>
                        <th>Run</th>
                        <th>4M</th>
                        <th>Trash</th>
                        <th>Repair</th>
                        <th>Analysis</th>
                        <th>Quarantine</th>
                        <th>Cabbage Patch</th>
                        <th>Machine</th>
                        <th>Production Number</th>
                        <th>Code</th>
                        <th>Defect Details</th>
                        <th>New Code UID</th>
              </tr>
                    <tr>
                        <td><input style="width:45px;" name="run" value="" size="" type="number" placeholder="0"></td>
                        </td>
                        <td><input style="width:45px;" name="4M" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="t" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="machine" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="pnumber" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="dcode" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="code-details" value="" size="" type="number" placeholder="0"></td>
                        <td><input style="width:45px;" name="uid" value="" size="" type="number" placeholder="0"></td>
        
                    </tr>
                
                <!-- temporary-php-to-see-what-look-lik -->
                <?php
                        for ($i = 0; $i <= 20; $i++) {
                                echo '  <tr>
                                <td><input style="width:45px;" name="run" value="" size="" type="number" placeholder="0"></td>
                                </td>
                                <td><input style="width:45px;" name="4M" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="t" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="machine" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="pnumber" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="dcode" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="code-details" value="" size="" type="number" placeholder="0"></td>
                                <td><input style="width:45px;" name="uid" value="" size="" type="number" placeholder="0"></td>
                
                            </tr>   ';
                        }
                    ?>
                
                
                
                </table>

                <input type="submit" name="defectokbutton" value="OK" id="defectokbutton">
                <input type="button" class="close-modal" name="defectbackbutton" value="Close" id="defectclosebutton">
                
                            </form>
        </div>
    </div>
</div>
