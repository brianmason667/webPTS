
<?php 
$pauid = $_SESSION["pauid"];
if($pauid != null):?>
    
<div name="block3" class="rounded-block center-text">
        <form>
            <table id="block3" class="block3 sep-rows">
                <tr>
                    <th>Run#</th>
                    <th>Partal Start</th>
                    <th>Partal End</th>
                    <th>Finished Goods</th>
                    <th>Kanban Count</th>
                    <th>Product Number</th>
                    <th>Team Members</th>
                    <th>Start Time</th>
                    <th>Finish Time</th>
                    <th>Plan Down Time</th>
                    <th>Net Operation</th>
                    <th>Plan Qty</th>
                    <th>Result Qty</th>
                    <th>Scrap</th>
                    <th>Repair</th>
                    <th>Analysis</th>
                    <th>Quarantine</th>
                    <th>Cabbage Patch</th>
                    <th>Unplan Downtime</th>
                    <th>Cycle Time</th>
                    <th>Standard Time</th>
                    <th>OA</th>
                    <th>OA w/o Downtime</th>
                </tr>
                <tr>
                    <td><input style="min-width:30px;" type="number" maxlength="2" placeholder="0"></td>
                    <td><input style="min-width:40px;" type="number" maxlength="3" placeholder="0"></td>
                    <td><input style="min-width:47px" type="number" maxlength="3" placeholder="0"></td>
                    <td><input style="min-width:47px" type="number" maxlength="3" placeholder="0"></td>
                    <td><input style="min-width:47px" type="number" placeholder="0"></td>
                    <td><input style="min-width:120px;" id="pnumber" maxlength="12" placeholder="000000-00000"></td>
                    <td><input style="min-width: 35px;" type="number" maxlength="1" placeholder="0"></td>
                    <td><input type="time"></td>
                    <td><input type="time"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                    <td><input type="text" placeholder="0"></td>
                    <td><input type="number" placeholder="0"></td>
                </tr>
                
                <?php
                    for ($i = 0; $i <= 5; $i++) {
                        echo '                    <tr>
                        <td><input style="min-width:30px;" type="number" maxlength="2" placeholder="0"></td>
                        <td><input style="min-width:40px;" type="number" maxlength="3" placeholder="0"></td>
                        <td><input style="min-width:47px" type="number" maxlength="3" placeholder="0"></td>
                        <td><input style="min-width:47px" type="number" maxlength="3" placeholder="0"></td>
                        <td><input style="min-width:47px" type="number" placeholder="0"></td>
                        <td><input style="min-width:120px;" maxlength="12" placeholder="000000-00000"></td>
                        <td><input style="min-width: 35px;" type="number" maxlength="1" placeholder="0"></td>
                        <td><input type="time"></td>
                        <td><input type="time"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                        <td><input type="text" placeholder="0"></td>
                        <td><input type="number" placeholder="0"></td>
                    </tr>';
                    }

                ?>
            </table>
    </div>

<?php endif;?>