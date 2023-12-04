<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
} 
?>
<!DOCTYPE html>
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Kanit' rel='stylesheet'>
    <title>Online Bookstore</title>
    <style>
        body {
            font-family: 'Kanit';
            margin: 0;
            padding: 0;
            background-color: #FFF2D8;
         
        }

        .navbar {
            background-color: #BCA37F;
            overflow: hidden;
        }

        .navbar a {
            float: left;
            display: block;
            color: black;
            text-align: center;
            padding: 7px 20px;
            text-decoration: none;
        }

        .navbar a:hover {
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

        h1 {
            text-align: center;
            padding-top: 50px;
            color: #333;
            font-size: 3em;
            animation: fadeIn 2s;
        }

        p {
            text-align: center;
            color: #555;
            font-size: 1.2em;
            animation: slideInFromLeft 2s;
        }

        img.logo {
            display: block;
            margin: 0 auto; /* Center the image */
            width: 300px; /* Set the width of the image */
            animation: fadeInImage 2s; /* Apply fade-in animation */
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes slideInFromLeft {
            from {
                margin-left: -100%;
                opacity: 0;
            }
            to {
                margin-left: 0;
                opacity: 1;
            }
        }

        @keyframes fadeInImage {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <div class="navbar">
        <a href="home.php">Home</a>
        <a href="customer.php">Customers</a>
        <a href="items.php">Items</a>
		<div class="burger-icon" onclick="toggleBurgerMenu()">☰</div>
    </div>
	<div class="burger-menu" id="burgerMenu">
        <?php
		if (isset($_SESSION['user_id'])) {
		echo "<a>Welcome, " . $_SESSION['username'] . "!<br></a>";
        echo "<a href='logout.php'>Logout</a>";
		}
        ?>
    </div>
    <h1>Welcome to the Online Bookstore!</h1>
    <p>Explore our collection of books and much more.</p>
    <img class="logo" src="book-shop.png" alt="Bookstore Logo">
	<script>
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
