

<div id="admin-products-modal" class="modal">
    <div  class="modal-content">
<div>
<h1 class="modal-title">add/edit Products</h1>

            <!-- INSERT INTO `lines` (`departmentid`, `line-number`) VALUES ('$selecteddepartment', '$newlinename');    -->
            <form>
            <p>1) select your department</p>
            <!-- 0=mounting 1=assembly 2=sensor 3=ewp -->
            <p>
                <select name="department">
                    <!-- get department from table -->
                    <option value="use php to get deparmentid from department table">department</option>
                    <option value="use php to get deparmentid from department table">department</option>
                    <option value="use php to get deparmentid from department table">department</option>
                    <option value="use php to get deparmentid from department table">department</option>
                    <option value="use php to get deparmentid from department table">department</option>
                </select>

            <p>2) select line</p>

                    <select name="department">
                    <!-- get department from table -->
                    <option value="use php to get avalable lines from line table">line</option>
                    <option value="use php to get avalable lines from line table">line</option>
                    <option value="use php to get avalable lines from line table">line</option>
                    <option value="use php to get avalable lines from line table">line</option>
                </select>
<br>
                <input style="width: 120px;" name="new product" type="text" class="input"><br>
            <input style="" type="submit" name="addproductbutton" value="Add product" id="addproductbutton">
            <input type="button" class="close-modal" name="" value="Close" id="close-products"></form>
            <!-- something like this to add line                                   department , line
           
            INSERT INTO `lines` (`id`, `department`, `line-number`) VALUES (NULL, '2', 'AS2001'), (NULL, '2', 'AS2002');
           
        -->
            <p>
            <!-- get lines for department from table -->
                   </p>
              <p><a href="admin-display.php">Display Products</a></p>
              </div></div></div>



         