<?php
include 'db.php';

// Define an empty array to store login errors
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle login form submission
    $c_email = mysqli_real_escape_string($conn, $_POST['c_email']);
    $c_password = $_POST['c_password'];

    // Check if the email exists in the Customer table
    $check_email_query = "SELECT * FROM Customers WHERE c_email = '$c_email'";
    $result = $conn->query($check_email_query);

    if ($result->num_rows == 1) {
        // Email exists, verify password
        $row = $result->fetch_assoc();
        if (password_verify($c_password, $row['c_password'])) {
            // Password is correct, set session variables and redirect to index or another page
            session_start();
            $_SESSION['c_id'] = $row['c_id'];
            $_SESSION['c_name'] = $row['c_name'];
            header("Location: index.php");
            exit();
        } else {
            $errors[] = "Incorrect password. Please try again.";
        }
    } else {
        $errors[] = "Email not found. Please register or try a different email.";
    }
}

// HTML form for login
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }

        .container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
        }

        button {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Customer Login</h2>

    <?php
    // Display login errors
    if (!empty($errors)) {
        echo '<div style="color: red; margin-bottom: 10px;">';
        foreach ($errors as $error) {
            echo $error . '<br>';
        }
        echo '</div>';
    }
    ?>

    <form method="post" action="">
        <label for="c_email">Email:</label>
        <input type="email" name="c_email" required>

        <label for="c_password">Password:</label>
        <input type="password" name="c_password" required>

        <button type="submit">Login</button>
    </form>
	<p>Don't have an account? <a href="register.php">Sign Up</a></p>

</div>

</body>
</html>
