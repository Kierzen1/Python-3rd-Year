<?php
include 'db.php';
session_start();

// Check if the user is logged in
if (!isset($_SESSION['c_id'])) {
    // Redirect to login page if not logged in
    header("Location: login.php");
    exit();
}

// Fetch items from the user's cart
$cart_id = $_SESSION['c_id'];
$cart_query = "SELECT Items.*, Cart.cart_id FROM Items JOIN Cart ON Items.i_id = Cart.item_id WHERE Cart.c_id = $cart_id";
$cart_result = $conn->query($cart_query);
$cart_items = $cart_result->fetch_all(MYSQLI_ASSOC);

// Handle removing items from the cart
if (isset($_POST['remove_from_cart'])) {
    $cart_id_to_remove = mysqli_real_escape_string($conn, $_POST['cart_id']);
    $remove_query = "DELETE FROM Cart WHERE cart_id = $cart_id_to_remove AND c_id = $cart_id";
    $conn->query($remove_query);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Cart</title>
    <style>
        /* Styles remain unchanged */

        .cart-container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .cart-item {
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 20px;
            padding: 10px;
        }

        .cart-item img {
            max-width: 100%;
            height: auto;
        }

        .remove-from-cart {
            background-color: #e53935;
            color: #fff;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        h2 {
            color: #333;
            text-align: center;
        }

        p {
            text-align: center;
            color: #555;
        }
    </style>
</head>
<body>

<div class="cart-container">
    <h2>Shopping Cart</h2>

    <?php
    if (empty($cart_items)) {
        echo '<p>Your cart is empty. <a href="index.php">Continue shopping</a></p>';
    } else {
        foreach ($cart_items as $cart_item) {
            echo '<div class="cart-item">';
            echo '<h3>' . $cart_item['title'] . '</h3>';
            echo '<p>Author: ' . $cart_item['author'] . '</p>';
            echo '<p>Genre: ' . $cart_item['genre'] . '</p>';
            echo '<p>Price: $' . $cart_item['price'] . '</p>';
            echo '<img src="path/to/your/images/' . $cart_item['i_id'] . '.jpg" alt="' . $cart_item['title'] . '">';

            // Remove from Cart button
            echo '<form method="post" action=""><input type="hidden" name="cart_id" value="' . $cart_item['cart_id'] . '"><button class="remove-from-cart" type="submit" name="remove_from_cart">Remove from Cart</button></form>';

            echo '</div>';
        }

        // Proceed to Checkout button
        echo '<button onclick="location.href=\'checkout.php\'">Proceed to Checkout</button>';
    }
    ?>

    <p><a href="index.php">Back to Home</a></p>
</div>

</body>
</html>
