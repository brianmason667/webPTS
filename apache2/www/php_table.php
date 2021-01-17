
<?php

        function makeDataGrid($sql){
            include('db.php');
                // Check conection
            if ($con->conect_error) {
                die("conection failed: " . $con->conect_error);
            }

            # Set Your Table class id to fetch records
            # You can set it from $_GET OR $_POST value
            $class = 5;
            //$class = mysqli_real_escape_string($con, $_POST['Class']);


            $result = $con->query($sql);
            $columns = array();
            $resultset = array();

            # Set columns and results array
            while ($row = mysqli_fetch_assoc($result)) {
                if (empty($columns)) {
                    $columns = array_keys($row);
                }
                $resultset[] = $row;
            }

            # If records found
        if( count($resultset > 0 )) {
            echo '<table class="sep-rows" >
                <thead>
                    <tr>';
                    
                    foreach ($columns as $k => $column_name ){
                            echo '<th>'.$column_name.'</th>';
                }

            echo '</tr>
                </thead>
                <tbody>';

                foreach($resultset as $index => $row) {
                    $column_counter =0;
                    echo "<tr>";
                    for ($i=0; $i < count($columns); $i++){
                        echo '<td>'.$row[$columns[$column_counter++]].'</td>';
                    }
                    echo "</tr>";

                }

                echo '</tbody>
            </table>';

        }else{
            echo "<h4> Information Not Available </h4>";
        }

    }

            
?>