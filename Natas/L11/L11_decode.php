#!/usr/bin/php

<?php

// ? 解xor_encrypt() key 想法
// ? => cheapText ^ key = ciphertext
// ? => cheapText ^ ciphertext = key

function xor_encrypt($in, $key)
{
    $text = $in;
    $outText = '';

    // Iterate through each character
    for ($i = 0; $i < strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// TODO: Test json_encode()
$defaultdata = array("showpassword" => "no", "bgcolor" => "#ffffff");
// echo json_encode($defaultdata);

// TODO: Get key && test key
$data = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");
$defaultdata = json_encode($defaultdata);
// ? substr($str, start, length);
$key = substr(xor_encrypt($data, $defaultdata), 0, 4);
// $cheapText = xor_encrypt($data, $key);
// echo $cheapText;
// echo "\n";
// echo $key;

// TODO: Encrypt cheapText to cipherText
$cheapText = json_encode(array("showpassword" => "yes", "bgcolor" => "#ffffff"));
$cipherText = base64_encode(xor_encrypt($cheapText, $key));
echo $cipherText;