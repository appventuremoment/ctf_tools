<?php
include("util.php");
if ($_SERVER['REQUEST_METHOD'] == "POST"){
    $option = $_POST['book'];  
}
else{
    $option = -1;
}

if (!isset($_COOKIE['PHPSESSID'])){
    $user = new User("User". substr(uniqid(),5,9));
    setcookie("PHPSESSID", base64_encode(serialize($user)));
}
else{
    $user = unserialize(base64_decode($_COOKIE['PHPSESSID']));
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Libwary</title>
</head>
<body>
    <h1> Welcome to the Libwary™,  
        <?php 
            echo $user;
        ?>
    </h1>
    <h3> Select a book to read </h3>

    <form action="index.php" method="POST">
        <select name="book">
            <option value="1">A Love Story</option>
            <option value="2">The Hackerman</option>
            <option value="3">The Egg</option>
            <option value="4">Exploring the Castle</option>
            <option value="5"> The Flag </option>
        </select>
        <input type="submit" value="Read">
    </form>

    <p> <?php 
        if ($option != -1){
            $book = new Book($option);
            echo $book;
        }
        else{
            echo "Please select a book to read";
        }
    ?>
    </p>

</body>
</html>
