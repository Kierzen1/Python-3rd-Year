<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dbms_booc";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $loginPassword = $_POST['password'];

    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        if (password_verify($loginPassword, $row['password'])) {
            // Start a session and set a session variable indicating the user is logged in
            session_start();
            $_SESSION['email'] = $email;

            // Redirect to home.php
            header("Location: home.php");
            exit; // Ensure that no other content is sent before the redirect
        } else {
            echo "Invalid password";
        }
    } else {
        echo "User not found";
    }
}

$conn->close();
?>
