#!/usr/bin/php

<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    
    
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$plain_text = json_encode($defaultdata);
$chipertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');

#echo(xor_encrypt($plain_text, $chipertext));

$key = 'qw8J';
$our_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$our_plantext = json_encode($our_data);
$our_chiphertext = xor_encrypt($our_plantext, $key);

$cookie = base64_encode($our_chiphertext);
echo($cookie);



?>