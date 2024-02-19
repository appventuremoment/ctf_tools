<?php

for ($x = 0; $x <= 1000000000000; $x++) {
  if (strcmp(substr((string)hash('sha1', "$x"), 0, 2), '42') == 0){
      echo "$x <br>";
      echo (string)hash('sha1', "$x");
      break;
  }
}

?>