<?php
$conn = new mysqli("localhost", "root", "", "semisproject");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["action"])) {
    if ($_POST["action"] == "insert") {
        $c_name = $_POST["name"];
        $c_email = $_POST["email"];
        $c_address = $_POST["address"];

        $stmt = $conn->prepare(
            "INSERT INTO customers  (c_name, c_email, c_address, c_status) VALUES (?, ?, ?, 'active')"
        );
        $stmt->bind_param("sss", $c_name, $c_email, $c_address);

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
    }

    if ($_POST["action"] == "delete") {
        $c_id = $_POST["id"];

        $stmt = $conn->prepare("DELETE FROM customers WHERE c_id = ?");
        $stmt->bind_param("i", $c_id);

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
    }

    if (
        $_POST["action"] == "edit" &&
        isset($_POST["id"]) &&
        isset($_POST["name"]) &&
        isset($_POST["email"]) &&
        isset($_POST["address"])
    ) {
        $c_id = $_POST["id"];
        $c_name = $_POST["name"];
        $c_email = $_POST["email"];
        $c_address = $_POST["address"];
        $c_status = $_POST["status"];

        $stmt = $conn->prepare(
            "UPDATE customers SET c_name = ?, c_email = ?, c_address = ?, c_status = ? WHERE c_id = ?"
        );
        $stmt->bind_param(
            "ssssi",
            $c_name,
            $c_email,
            $c_address,
            $c_status,
            $c_id
        );

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
        $search = "";
        if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["search"])) {
            $search = $_GET["search"];
            $sql = "SELECT * FROM customers WHERE c_name LIKE '%$search%'";
        } else {
            $sql = "SELECT * FROM customers";
        }

        $result = $conn->query($sql);
    }
}

// Retrieve customer data
$sql = "SELECT * FROM customers";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Customer Management</title>
    <style>
        body {
            font-family: 'Garamond', serif;
            margin: 20px;
			background-color:#E4D9FF; 
        }
		.navbar {
            background-color: #30343F;
            overflow: hidden;
			font-size: 0.8em;
        }

        .navbar a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 5px 20px;
            text-decoration: none;
        }

        .navbar a:hover {
            background-color: #FAFAFF;
            color: black;
        }
		
        h1 {
            color: #333;
            text-align: center;
        }

        h2 {
            color: #333;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
        }

        .modal-content {
            background-color: #f9f9f9;
            width: 50%;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        
		form, .form1 {
            width: 13%;
            padding: 15px;
            border: 2px solid #ccc;
            border-radius: 5px;
            background-color: #273469;
        }
		 .form2 {
			width: 50%;
			margin: 20px auto;
			padding: 25px;
			border: 2px solid #ccc;
			border-radius: 5px;
			background-color:#273469;
			animation-name: slideIn;
			animation-duration: 1s;
			text-align: center;
			}
		.form3 {
			width: 50%;
            margin: 20px auto;
            padding: 20px;
            border-radius: 5px;
            background-color: #273469;
			text-align: center;
			display: center;
		}


        table {
            width: 100%;
            margin: 20px auto;
            
        }

        table, th, td {
            border: 1px dashed black;
			
        }

        th, td {
            padding: 8px;
            text-align: left;
			
        }

        th {
            background-color: #273469;
            color: white;
			font-size: 2em;
        }
		tr{
			font-size: 1em;
		}
        .close {
            float: right;
            cursor: pointer;
        }

        input[type="text"] {
            width: 90%; 
            padding: 5px;
            margin: 5px 0;
        }
		table form.form3,
        table form.form4 {
            display: inline-block; 
            margin: 0;
			padding: 10px;
        }

        table form.form4 button {
            width: 100%; 
            padding: 8px;
			background-color: white;
        }

		
		.edit-form {
        display: none;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #f9f9f9;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        z-index: 999;
        opacity: 0; 
        transition: opacity 0.5s; 
    }
	 table button {
        width: 60px;
        padding: 6px;
		border-radius: 5px;
		background-color: white;
		color: black;
    }

    
    form input[type="text"],
    form input[type="submit"] {
        width: 100%; 
        padding: 8px;
        margin: 5px 0;
    }
		 input[type="submit"] {
            padding: 12px; 
            width: 90%; 
            margin-top: 10px;
        }
		
		
    </style>
       <script>
    function toggleEditForm(id) {
        var editForm = document.getElementById('editForm' + id);
        if (editForm.style.display === 'block') {
            editForm.style.opacity = 0; 
            setTimeout(function() {
                editForm.style.display = 'none';
            }, 500); 
        } else {
            editForm.style.display = 'block';
            setTimeout(function() {
                editForm.style.opacity = 1; 
            }, 50); 
        }
    }

    function closeEditForm(id) {
        var editForm = document.getElementById('editForm' + id);
        editForm.style.opacity = 0; 
        setTimeout(function() {
            editForm.style.display = 'none';
        }, 500);
    }
</script>

</head>
<body style="margin: 0;">
	<div class="navbar">
        <a href="home.php">Home</a>
        <a href="customer.php">Customers</a>
        <a href="items.php">Items</a>
    </div>

        <h1 style="color:black; font-size:3em;">Customer List</h1>
        
     
    </div>
	 <form method="get" action="">
            <input type="text" name="search" style="width:185px"placeholder="Search by name">
            <input type="submit" value="Search">
        </form>
		<form method="get" action="">
            <input type="submit" name="showAll" value="Show All">
        </form>
    <!-- Customer List -->
<table>
    <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Address</th>
        <th>Status</th>
        <th>Edit</th>
        <th>Delete</th>
    </tr>
	<?php
 $search = "";
 if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["search"])) {
     $search = $_GET["search"];
     $sql = "SELECT * FROM customers WHERE c_name = '$search'";
 } else {
     $sql = "SELECT * FROM customers";
 }

 $result = $conn->query($sql);
 ?>
    <?php if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["c_name"] . "</td>";
            echo "<td>" . $row["c_email"] . "</td>";
            echo "<td>" . $row["c_address"] . "</td>";
            echo "<td>" . $row["c_status"] . "</td>";
            echo "<td>";

            echo "<button onclick='toggleEditForm(" .
                $row["c_id"] .
                ")'>Edit</button>";
            echo "</td>";
            echo "<td style='padding-left: 5px;'>"; 
  
            echo "<form class='form3' method='post' action=''>
					<input type='hidden' name='action' value='delete'>
					<input type='hidden' name='id' value='" .
								$row["c_id"] .
								"'>
					<input type='submit' value='Delete'>
				</form>";
            echo "</td>";
            echo "</tr>";

            // editing form
            echo "<div id='editForm" . $row["c_id"] . "' class='edit-form'>";
            echo "<span class='close' onclick='closeEditForm(" .
                $row["c_id"] .
                ")'>&times;</span>";
            echo "<form method='post' action=''>";
            echo "<input type='hidden' name='action' value='edit'>";
            echo "<input type='hidden' name='id' value='" . $row["c_id"] . "'>";
            echo "Name: <input type='text' name='name' value='" .
                $row["c_name"] .
                "'><br>";
            echo "Email: <input type='text' name='email' value='" .
                $row["c_email"] .
                "'><br>";
            echo "Address: <input type='text' name='address' value='" .
                $row["c_address"] .
                "'><br>";
            echo "Status: <input type='text' name='status' value='" .
                $row["c_status"] .
                "'><br>";
            echo "<input type='submit' value='Save'>";
            echo "</form>";
            echo "</div>";
        }
    } else {
        echo "<tr><td colspan='5'>No customers found</td></tr>";
    } ?>
</table>

    <!-- Customer Insertion Form -->
    <form method="post" action="">
		<p style="color:white; font-size:20px; text-align:center;">Insert Customer</p>
        <input type="hidden" name="action" value="insert">
         <input type="text" name="name" placeholder="Name:"style="width: 198px; padding: 1px;">
         <input type="text" name="email" placeholder="Email:"style="width: 198px; padding: 1px;">
        <input type="text" name="address" placeholder="Address:" style="width: 198px; padding: 1px;">
        <input type="submit" value="Insert">
    </form>
</body>
</html>