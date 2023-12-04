<?php
include 'db.php';

// Define an empty array to store registration errors
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle registration form submission
    $c_name = mysqli_real_escape_string($conn, $_POST['c_name']);
    $c_email = mysqli_real_escape_string($conn, $_POST['c_email']);
    $c_address = mysqli_real_escape_string($conn, $_POST['c_address']);
    $c_password = password_hash($_POST['c_password'], PASSWORD_DEFAULT);

    // Check if the email is already registered
    $check_email_query = "SELECT * FROM Customers WHERE c_email = '$c_email'";
    $result = $conn->query($check_email_query);

    if ($result->num_rows > 0) {
        $errors[] = "Email already registered. Please choose a different email.";
    } else {
        // Insert the new customer data into the Customer table
        $insert_query = "INSERT INTO Customers (c_name, c_email, c_address, c_password) VALUES ('$c_name', '$c_email', '$c_address', '$c_password')";

        if ($conn->query($insert_query) === TRUE) {
            // Registration successful
            header("Location: login.php");
            exit();
        } else {
            $errors[] = "Registration failed. Please try again later.";
        }
    }
}

// HTML form for registration
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Registration</title>
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
    <h2>Customer Registration</h2>

    <?php
    // Display registration errors
    if (!empty($errors)) {
        echo '<div style="color: red; margin-bottom: 10px;">';
        foreach ($errors as $error) {
            echo $error . '<br>';
        }
        echo '</div>';
    }
    ?>

    <form method="post" action="">
        <label for="c_name">Name:</label>
        <input type="text" name="c_name" required>

        <label for="c_email">Email:</label>
        <input type="email" name="c_email" required>

        <label for="c_address">Address:</label>
        <input type="text" name="c_address" required>

        <label for="c_password">Password:</label>
        <input type="password" name="c_password" required>

        <button type="submit">Register</button>
    </form>
</div>

</body>
</html>
s