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

// Handle order placement
if (isset($_POST['place_order'])) {
    $shipping_address = mysqli_real_escape_string($conn, $_POST['shipping_address']);
    
    // Create a new order
    $order_query = "INSERT INTO Orders (o_date, shipping_address, c_id) VALUES (NOW(), '$shipping_address', $cart_id)";
    $conn->query($order_query);

    // Get the order ID
    $order_id = $conn->insert_id;

    // Move cart items to order details
    foreach ($cart_items as $cart_item) {
        $item_id = $cart_item['i_id'];
        $quantity = 1; // For simplicity, assuming each item is quantity 1 in this example

        // Create order details
        $order_details_query = "INSERT INTO OrderDetails (i_id, o_id, qty) VALUES ($item_id, $order_id, $quantity)";
        $conn->query($order_details_query);
    }

    // Clear the user's cart after placing the order
    $clear_cart_query = "DELETE FROM Cart WHERE c_id = $cart_id";
    $conn->query($clear_cart_query);

    // Redirect to a thank you page or display a success message
    header("Location: thank_you.php");
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout</title>
    <style>
        /* Styles remain unchanged */

        .checkout-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .checkout-item {
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 20px;
            padding: 10px;
        }

        .checkout-item img {
            max-width: 100%;
            height: auto;
        }

        .place-order {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            margin-top: 5px;
        }
    </style>
</head>
<body>

<div class="checkout-container">
    <h2>Checkout</h2>

    <?php
    if (empty($cart_items)) {
        echo '<p>Your cart is empty. <a href="index.php">Continue shopping</a></p>';
    } else {
        foreach ($cart_items as $cart_item) {
            echo '<div class="checkout-item">';
            echo '<h3>' . $cart_item['title'] . '</h3>';
            echo '<p>Author: ' . $cart_item['author'] . '</p>';
            echo '<p>Genre: ' . $cart_item['genre'] . '</p>';
            echo '<p>Price: $' . $cart_item['price'] . '</p>';
            echo '<img src="path/to/your/images/' . $cart_item['i_id'] . '.jpg" alt="' . $cart_item['title'] . '">';
            echo '</div>';
        }

        // Display a summary of the total cost
        $total_cost_query = "SELECT SUM(price) AS total_cost FROM Items WHERE i_id IN (SELECT item_id FROM Cart WHERE c_id = $cart_id)";
        $total_cost_result = $conn->query($total_cost_query);
        $total_cost = $total_cost_result->fetch_assoc()['total_cost'];

        echo '<p>Total Cost: $' . number_format($total_cost, 2) . '</p>';

        // Shipping address form
        echo '<form method="post" action="">';
        echo '<label for="shipping_address">Shipping Address:</label>';
        echo '<input type="text" name="shipping_address" required>';
        echo '<button class="place-order" type="submit" name="place_order">Place Order</button>';
        echo '</form>';
    }
    ?>

    <p><a href="index.php">Back to Home</a></p>
</div>

</body>
</html>
