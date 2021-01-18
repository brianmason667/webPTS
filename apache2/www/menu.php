<ul id="smenu" class="smenu active">
    <li>
        <a>File</a>
        <ul>
            <li>
                <div><a id="newpauidmenuoption">New Production Actual<span></span></a></div>
            </li>
            <li><a id="loadpauidmenuoption">Open Production Actual</a></li>
            <li><a id="edit-preferences">Preferences..</a></li>
            <li><a id="Reload">Reload (With out save)</a></li>
            <li><a id="Write">Write (Save all data)</a></li>
        </ul>
    </li>
    <li>
        <a>Production</a>
        <ul>
            <li><a id="edit-run">Add/Edit Run<span></span></a></li>
            <li><a id="edit-redo"> <span></span></a></li>
            <li class="split"></li>
            <li><a class="image" id="edit-stroke">Stroke..</a></li>
            <li><a class="image" id="edit-fill">Fill..</a></li>
            <li class="split"></li>
        </ul>
    </li>
    <li>
        <a>Downtime</a>
        <ul>
            <li><a id="downtimemenuoption">Add/Edit Downtime</a></li>
            <li><a id="fcode-request">New Fcode request</a></li>
            <li class="split"></li>
            <li><a id=""></a></li>
            <li><a id=""></a></li>
        </ul>
    </li>
    <li>
        <a>Defects</a>
        <ul>
            <li><a id="defectmenuoption">Add/Edit defect</a></li>
            <li><a id="dcode-request">New Dcode request</a></li>
            <li><a id=""></a></li>
            <li><a id=""></a></li>
            <li class="split"></li>
        </ul>
    <li>
        <a>Charts</a>
        <ul>
            <li><a id="production-control">Production Control<span>PC</span></a></li>
            <li><a id="quality-control">Quality Control <span>QC</span></a></li>
            <li class="split"></li>
            <li><a id="auto-total-chart">Chart Totals, End of month<span>Ctrl + 0</span></a></li>
        </ul>
    </li>
    <li>
        <a>Help</a>
        <ul>
            <li><a id="help-shortcuts">Keyboard shortcuts..</a></li>
            <li class="split"></li>
            <li><a id="help-email">Email</a></li>
        </ul>
    </li>

    <!-- this is hidden when not administrator-->
        
    <?php
        if(isset($_SESSION['isadmin'])){
            $isAdmin = $_SESSION['isadmin'];
        }else{
            $isAdmin = false;
        }

        if($isAdmin):
    ?>

    <li class="menu-float-right">
            <a><?php echo $_SESSION['username']; ?></a>
            <ul>
            <li><a href=logout.php id="logout">logout</a></li>
        </ul>
    </li>


    <li id="admin-menu" class="menu-float-right">
        <a id="admin-menu">Administrator</a>
        <ul>
            <!-- <li><li class="menu-float-right"><a>Add</a>
                <ul>
                    <li><a id="admindcodemenuoption">Add/Remove dcode</a></li>
                    <li><a id="adminfcodemenuoptition">Add/Remove fcode</a></li>
                    <li><a id="adminlinemenuoptition">Add/Remove lines</a></li>
                    <li><a id="adminproductmenuoptition">Add/Remove products</a></li>
                </ul> -->
            </li></li>
            
            <li><a id="adminlinemenuoptition">Add/Remove lines</a></li>
            <li><a id="admindcodemenuoption">Add/Remove dcode</a></li>
            <li><a id="adminfcodemenuoptition">Add/Remove fcode</a></li>
            <li><a id="adminproductmenuoptition">Add/Remove products</a></li>
            <li><a href="admin-display.php">Display<span>Products,Codes,Cycle times</span></a></li>
            <li><a href="main.php" id="back">Main Dashboard<span>(Back)</span></a></li>
        </ul>
    </li> 

    <?php endif;?>

</ul>


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

    
    <!-- ########### start of Modals Includes ########### -->
    <?php ?>    
    <?php include("downtimes-modal.php");?>
    <?php include("defects-modal.php");?>
    <?php include("admin-dcode-modal.php");?>
    <?php include("admin-fcode-modal.php");?>
    <?php ?>
    <?php include("admin-products-modal.php");?>
    <!-- include("new-pauid-modal.php"); -->
    <!-- include("admin-line-modal.php"); -->

    <!-- ############ end of Modals ############ -->


<script>

    //Get the button that opens the modal
    var newPauidButton = document.getElementById("newpauidmenuoption");

    //When the user clicks the button, open the modal 
    newPauidButton.onclick = function () {
        openModalWithId("new-pauid-modal");
    }


    //Get the button that opens the modal
    var downtimeButton = document.getElementById("downtimemenuoption");

    //When the user clicks the button, open the modal 
    downtimeButton.onclick = function () {
        openModalWithId("downtime-modal");
    }

    //Get the button that opens the modal
    var defectButton = document.getElementById("defectmenuoption");

    //When the user clicks the button, open the modal 
    defectButton.onclick = function () {
        openModalWithId("defect-modal");
    }

    //Get the button that opens the modal
    var dcodeButton = document.getElementById("admindcodemenuoption");

    //When the user clicks the button, open the modal 
    dcodeButton.onclick = function () {
        openModalWithId("admin-dcode-modal");
    }

    //Get the button that opens the modal
    var fcodeButton = document.getElementById("adminfcodemenuoptition");

    //When the user clicks the button, open the modal 
    fcodeButton.onclick = function () {
        openModalWithId("admin-fcode-modal");
    }

    //Get the button that opens the modal
    var fcodeButton = document.getElementById("adminlinemenuoptition");

    //When the user clicks the button, open the modal 
    fcodeButton.onclick = function () {
        openModalWithId("admin-lines-modal");
    }

        //Get the button that opens the modal
        var fcodeButton = document.getElementById("adminproductmenuoptition");

//When the user clicks the button, open the modal 
fcodeButton.onclick = function () {
    openModalWithId("admin-products-modal");
}
</script>


