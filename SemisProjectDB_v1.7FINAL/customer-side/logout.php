<?php
session_start();

// Destroy the session data
session_destroy();

// Redirect to the login page after logout
header("Location: login.php");
exit();
?>