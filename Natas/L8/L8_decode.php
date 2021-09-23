#!/usr/bin/php

<?php
    $cipher = '3d3d516343746d4d6d6c315669563362';
    $cheapText = base64_decode(strrev(hex2bin($cipher)));
    echo $cheapText;
?>