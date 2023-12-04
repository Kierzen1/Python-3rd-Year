<?php
session_start();
$conn = new mysqli("localhost", "root", "", "dbmsproject");
if (isset($_SESSION['user_id'])) {
    header("Location: home.php"); 
    exit();
}
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    
    $sql = "SELECT id, username, password FROM users WHERE username = ?";

  
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 1) {
        $row = $result->fetch_assoc();
        if (password_verify($password, $row['password'])) {
            $_SESSION['user_id'] = $row['id'];
            $_SESSION['username'] = $row['username'];
			
            header("Location: home.php");
            exit();
			
        } else {
            echo "Invalid username or password";
        }
    } else {
        echo "Invalid username or password";
    }

}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Online Book Store</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #FFF2D8;
        }
        h1 {
            text-align: center;
            margin-top: 50px;
        }
        .container {
            width: 20%;
            margin: 0 auto;
            padding: 20px;
            background-color: #EAD7BB;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        form, a {
            margin-top: 20px;
			
        }
        form label {
            display: block;
            margin-bottom: 5px;
			background-color: #EAD7BB;
        }
        form input[type="username"],
        form input[type="password"],
        form input[type="submit"],
        button {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
			
        }
        form input[type="submit"],
        button {
            background-color: #BCA37F;
            color: white;
            cursor: pointer;
        }
        form input[type="submit"]:hover,
        button:hover {
            background-color: #45a049;
        }
		img.logo {
            display: block;
            margin: 0 auto; /* Center the image */
            width: 300px; /* Set the width of the image */
            
        }
    </style>
</head>
<body>
    <h1>Online Book Store</h1>

    <div class="container">
        <h2>Login</h2>
        <form method="post" action ="">
            <label for="username">Username:</label>

            
				<input type="username" name="username" placeholder="Username" required><br>
			 <label for="password">Password:</label>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">

        </form>
		<a href="registration.php"><button>Register</button></a>
    </div>
<img class="logo" src="book-shop.png" alt="Bookstore Logo">
</body>
</html>