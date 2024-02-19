<?php

$secret = 'REDACTED';
$flag = 'blahaj{REDACTED}';

$inputsecret = $_POST['secret'];
$meaningoflife = $_POST['meaningoflife'];

# Check if the secret is correct
if (strcmp($inputsecret, $secret) != 0) {
    echo 'come back with correct secret';
}
else{
    # Check if the meaning of life is correct
    if (hash('sha1',$meaningoflife) != 42) {
        echo 'come back with correct meaning of life';
    }
    else{
        echo 'flag: ' . $flag;
    }
}

?>