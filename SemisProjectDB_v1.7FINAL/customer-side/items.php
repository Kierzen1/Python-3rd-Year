<?php
include 'db.php';
session_start();

// Check if the user is logged in
if (!isset($_SESSION['c_id'])) {
    // Redirect to login page if not logged in
    header("Location: login.php");
    exit();
}

// Fetch and display details of the selected item
if (isset($_GET['item_id'])) {
    $item_id = mysqli_real_escape_string($conn, $_GET['item_id']);
    $item_query = "SELECT * FROM Items WHERE i_id = $item_id";
    $item_result = $conn->query($item_query);

    if ($item_result->num_rows == 1) {
        $item = $item_result->fetch_assoc();
    } else {
        // Redirect to the index page if the item is not found
        header("Location: index.php");
        exit();
    }
} else {
    // Redirect to the index page if item_id is not provided
    header("Location: index.php");
    exit();
}

// Handle adding the item to the cart
if (isset($_POST['add_to_cart'])) {
    $cart_id = $_SESSION['c_id'];

    // Check if the item is already in the cart
    $check_cart_query = "SELECT * FROM Cart WHERE c_id = $cart_id AND item_id = $item_id";
    $check_cart_result = $conn->query($check_cart_query);

    if ($check_cart_result->num_rows == 0) {
        // Item is not in the cart, add it
        $add_to_cart_query = "INSERT INTO Cart (c_id, item_id) VALUES ($cart_id, $item_id)";
        $conn->query($add_to_cart_query);
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $item['title']; ?> - Item Details</title>
    <style>
        /* Styles remain unchanged */

        .item-details {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .item-details img {
            max-width: 100%;
            height: auto;
        }

        .add-to-cart {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="item-details">
    <h2><?php echo $item['title']; ?></h2>
    <p>Author: <?php echo $item['author']; ?></p>
    <p>Genre: <?php echo $item['genre']; ?></p>
    <p>Price: $<?php echo $item['price']; ?></p>
    <img src="path/to/your/images/<?php echo $item['i_id']; ?>.jpg" alt="<?php echo $item['title']; ?>">

    <!-- Add to Cart button -->
    <form method="post" action="">
        <input type="hidden" name="item_id" value="<?php echo $item['i_id']; ?>">
        <button class="add-to-cart" type="submit" name="add_to_cart">Add to Cart</button>
    </form>

    <p><a href="index.php">Back to Home</a></p>
</div>

</body>
</html>
