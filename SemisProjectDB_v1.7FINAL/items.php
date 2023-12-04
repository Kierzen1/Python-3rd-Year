<?php
session_start(); 
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
} 
$conn = new mysqli("localhost", "root", "", "dbmsproject");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["action"])) {
    if ($_POST["action"] == "insert") {
        $isbn = $_POST["isbn"];
        $title = $_POST["title"];
        $author = $_POST["author"];
        $genre = $_POST["genre"];
        $booktype = $_POST["booktype"];
        $price = $_POST["price"];

        $stmt = $conn->prepare("INSERT INTO items  (isbn, title, author, genre, booktype, price) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssss", $isbn, $title, $author, $genre, $booktype, $price);

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
    }

    if ($_POST["action"] == "delete") {
        $i_id = $_POST["id"];

        $stmt = $conn->prepare("DELETE FROM items WHERE i_id = ?");
        $stmt->bind_param("i", $i_id);

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
    }

    if (
        $_POST["action"] == "edit" &&
        isset($_POST["id"]) &&
        isset($_POST["isbn"]) &&
        isset($_POST["title"]) &&
        isset($_POST["author"]) &&
        isset($_POST["genre"]) &&
        isset($_POST["booktype"]) &&
        isset($_POST["price"])
    ) {
        $i_id = $_POST["id"];
        $isbn = $_POST["isbn"];
        $title = $_POST["title"];
        $author = $_POST["author"];
        $genre = $_POST["genre"];
        $booktype  = $_POST["booktype"];
        $price = $_POST["price"];
        
        $stmt = $conn->prepare(
            "UPDATE items SET isbn = ?, title = ?, author = ?, genre = ?, booktype =?, price = ? WHERE i_id = ?"
        );
        $stmt->bind_param(
            "sssssii",
            $isbn,
            $title,
            $author,
            $genre,
            $booktype,
            $price,
            $i_id
        );

        if ($stmt->execute()) {
            echo "";
        } else {
            echo "Error: " . $conn->error;
        }
        $search = "";
        if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["search"])) {
            $search = $_GET["search"];
            $sql = "SELECT * FROM items WHERE isbn LIKE '%$search%'";
        } else {
            $sql = "SELECT * FROM items";
        }

        $result = $conn->query($sql);
    }
}

// Retrieve customer data
$sql = "SELECT * FROM items";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <link href='https://fonts.googleapis.com/css?family=Kanit' rel='stylesheet'>

    <title>Items Management</title>
</head>
<style>
    body 
        {
            font-family: 'Kanit';
            margin: 0;
            padding: 0;
            background-color: #FFF2D8;
           
        }
    .navbar 
        {
            background-color: #BCA37F;
            overflow: hidden;
        }

    .navbar a 
        {
        float: left;
        display: block;
        color: black;
        text-align: center;
        padding: 7px 20px;
        text-decoration: none;
        }
    .navbar a:hover 
        {
        background-color: #113946;
        color: white;
        }
		.burger-icon {
            display: block;
            float: right;
            padding: 7px 20px;
            cursor: pointer;
        }

        .burger-menu {
            display: none;
            position: fixed;
            background-color: #BCA37F;
            width: 200px;
            top: 60px;
            right: 0;
            z-index: 1;
        }

        .burger-menu a {
            display: block;
            color: black;
            padding: 14px 20px;
            text-decoration: none;
        }

        .burger-menu a:hover {
            background-color: #113946;
            color: white;
        }
    .forminfo{
        width: 240px;
            margin: 0px auto;
            padding: 10px;
            border-radius: 5px 5px 5px 5px; 
            background-color: #EAD7BB;
            text-align: center;
    }
    .form1 {
            width: 350px;
            margin: 8px auto;
            padding: 0%;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #EAD7BB;
            text-align: center;
        }
    .formsearch
    {
         width: 240px;
            margin: 0px auto;
            padding: 10px;
            border-radius: 5px 5px 0px 0px; 
            background-color: #EAD7BB;
    }
    .formshow
    {
        width: 250px;
            margin: 0px auto;
            padding: 5px;
            border-radius: 0px 0px 5px 5px;
            background-color: #EAD7BB;
            text-align: center;
    }
    .formdelete
     {
        width: 50%;
        margin: 10px auto;
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
        }
    .formedit
    {
        width: 80%;
        margin: 20px auto;
        text-align: center;
        padding: 2px;
        }
    .edit-form 
        {
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
        table {
            width: 90%;
            margin: 10px auto;
            border-radius: 7px;
        }
        table, th, td {
            border: 2px outset #EAD7BB;
        }
        th {
            padding: 6px;
            background-color: #EAD7BB;
            color: black;
        }
        form input[type="text"] {
        width: 220px; 
        padding: 2px;
        margin: 3px 0;
        font-family: 'Kanit';
         }
         .inpputsearch{
            font-family: 'Kanit';
         }
        
    
</style>
<body style="margin: 0;">
	<div class="navbar">
        <a href="home.php">Home</a>
        <a href="customer.php">Customers</a>
        <a href="items.php">Items</a><div class="burger-icon" onclick="toggleBurgerMenu()">☰</div>
    </div>
	<div class="burger-menu" id="burgerMenu">
        <?php
		if (isset($_SESSION['user_id'])) {
		echo "<a>Welcome, " . $_SESSION['username'] . "!<br></a>";
        echo "<a href='logout.php'>Logout</a>";
		}
        ?>
    </div>
    <div class="form1">
        <h2>Items List</h2>
        
        </form>
    </div>
	 <form class = "formsearch" method="get" action="">
            <input class = "inpputsearch"name="search" placeholder="Search by ISBN">
            <input type="submit" value="Search" style = 'font-family: Kanit;'>
        </form>
		
	<form class = "formshow"method="get" action="">
            <input type="submit" name="showAll" value="Show All" style = 'font-family: Kanit;'>
        </form>
    <!-- Customer List -->
<table>
    <tr>
        <th>ISBN</th>
        <th>Title</th>
        <th>Author</th>
        <th>Genre</th>
        <th>Booktype</th>
        <th>Price</th>
    </tr>
	<?php
 $search = "";
 if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["search"])) {
     $search = $_GET["search"];
     $sql = "SELECT * FROM items WHERE isbn = '$search'";
 } else {
     $sql = "SELECT * FROM items";
 }

 $result = $conn->query($sql);
 ?>
    <?php if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["isbn"] . "</td>";
            echo "<td>" . $row["title"] . "</td>";
            echo "<td>" . $row["author"] . "</td>";
            echo "<td>" . $row["genre"] . "</td>";
            echo "<td>" . $row["booktype"] . "</td>";
            echo "<td>" . $row["price"] . "</td>";
            echo "<td>";
            // Edit button that opens the modal
            echo "<button class = 'formedit'onclick='toggleEditForm(" .
                $row["i_id"] .
                ")' style='font-family: Kanit;'>Edit</button>";
            echo "</td>";
            echo "<td style='padding-left: 5px;'>"; // Adding a small left padding for a space
            // Delete button and form
            echo "<form class='formdelete' method='post' action='' style='display: inline;'>
					<input type='hidden' name='action' value='delete'>
					<input type='hidden' name='id' value='" . $row["i_id"] ."'>
					<input type='submit' value='Delete'  style='font-family: Kanit;'>
				</form>";
            echo "</td>";
            echo "</tr>";

            // editing form
            echo "<div id='editForm" . $row["i_id"] . "' class='edit-form'>";
            echo "<span class='close' onclick='closeEditForm(" .
                $row["i_id"] .
                ")'>&times;</span>";
            echo "<form method='post' action=''>";
            echo "<input type='hidden' name='action' value='edit'>";
            echo "<input type='hidden' name='id' value='" . $row["i_id"] . "'>";
            echo "ISBN: <input type='text' name='isbn' value='" .
                $row["isbn"] .
                "'><br>";
            echo "Title: <input type='text' name='title' value='" .
                $row["title"] .
                "'><br>";
            echo "Author: <input type='text' name='author' value='" .
                $row["author"] .
                "'><br>";
            echo "Genre: <input type='text' name='genre' value='" .
                $row["genre"] .
                "'><br>";
            echo "Booktype: <input type='text' name='booktype' value='" .
                $row["booktype"] .
                "'><br>";
            echo "Price: <input type='text' name='price' value='" .
                $row["price"] .
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
	
    <form class = "forminfo "method="post" action="" onsubmit = "return validateForm()">
    <h4>Add Items</h4>
        <input type="hidden" name="action" value="insert">
         <input type="text" name="isbn" id = "isbn"placeholder="ISBN:"><br>
         <input type="text" name="title" id = "title"placeholder="Title:"><br>
        <input type="text" name="author" id = "author"placeholder="Author:"><br>
        <input type="text" name="genre" id = "genre"placeholder="Genre:"><br>
        <input type="text" name="booktype" id = "booktype"placeholder="Booktype:"><br>
        <input type="text" name="price" id ="price"placeholder="Price:"><br>
        <input type="submit" value="Add" style = 'font-family: Kanit;'>
    </form>
    <script>
          function validateForm() {
    var isbn = document.getElementById('isbn').value;
    var title = document.getElementById('title').value;
    var author = document.getElementById('author').value;
    var genre = document.getElementById('genre').value;
    var booktype = document.getElementById('booktype').value;
    var price = document.getElementById('price').value;

    if (isbn === "" || title === "" || author === ""|| genre ===""|| booktype ===""|| price==="") {
        alert("Please input all fields");
        return false; // Prevent form submission
    }

    // If all fields are filled, allow the form to be submitted
    return true;
}
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
	function toggleBurgerMenu() {
            var menu = document.getElementById('burgerMenu');
            if (menu.style.display === 'block') {
                menu.style.display = 'none';
            } else {
                menu.style.display = 'block';
            }
        }

        // Disable cache to prevent back navigation after logout
        window.onload = function () {
            if (window.history.replaceState) {
                window.history.replaceState(null, null, window.location.href);
            }
        }
	</script>
</body>
</html>