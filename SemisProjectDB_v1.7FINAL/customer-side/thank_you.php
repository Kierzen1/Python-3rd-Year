<?php
include 'db.php';
session_start();

// Check if the user is logged in
if (!isset($_SESSION['c_id'])) {
    // Redirect to login page if not logged in
    header("Location: login.php");
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
    <style>
        /* Styles remain unchanged */

        .thank-you-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        h2 {
            color: #4caf50;
        }

        p {
            color: #555;
        }
    </style>
</head>
<body>

<div class="thank-you-container">
    <h2>Thank You for Your Order!</h2>
    <p>Your order has been successfully placed.</p>

    <!-- You may include additional details, such as order number, estimated delivery time, etc. -->
    
    <p>If you have any questions or concerns, please contact our customer support.</p>

    <p><a href="index.php">Back to Home</a></p>
</div>

</body>
</html>
