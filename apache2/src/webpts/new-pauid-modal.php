<!-- brain pronounce this like "powi'd" -->
<div id="new-pauid-modal" class="modal">
    <div class="modal-content">
        <div>
            <span></span>
            <h1 class="modal-title">New Production Actual</h1>
            <form action="newpauid.php" method="post">
                <!-- <p>YYYY-MM-DD</p> -->
                <input id="new-pauid-date" class="new-pauid-modal-content-input" name="date" required></input>
                <br>
                
                <?php
                 require('db.php');
                $query    = "SELECT * FROM `assemblylines`";
                $result = mysqli_query($con, $query) or die(mysql_error());
                $rowCount = mysqli_num_rows($result);
                
                if($rowCount > 0){
                    echo "<select name='line'>";
                    while( $row = $result->fetch_assoc()) {
                        echo "<option>".htmlspecialchars($row['line-id'])."</option>";
                    }
                    echo "</select>";
                }
            ?>
                    <!-- <select name="line"> -->
                    <!-- need to get the options from db -->
                    <!-- <option value="AS0001">AS0001</option> -->
                    <!-- <option value="AS2006">AS2006</option> -->
                    <!-- <option value="AS2007">AS2007</option> -->
                <!-- </select> -->
                <br>
                <select name="shift">
                    <option value="1">First Shift</option>
                    <option value="2">Second Shift</option>
                </select>
                <br>
                <input type="submit" name="newpauidokbutton" value="OK" id="newpauidokbutton">
                <input type="button" class="close-modal" name="newpauidbackbutton" value="Close" id="newpauidclosebutton">
            </form>
        </div>
    </div>
</div>

<script>

    //set the date to be dafault today.

    //document.getElementById('new-pauid-date').valueAsDate = new Date();
    $('#new-pauid-date').val(getTodaysDate());

    function getTodaysDate() {
    var d = new Date(),
    month = '' + (d.getMonth() + 1),
    day = '' + d.getDate(),
    year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [month, day, year].join('/');
}
    
</script>