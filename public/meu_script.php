<?php
// Conteúdo do script PHP que você deseja executar continuamente.
// Por exemplo, imprime a data e hora atual no arquivo de log.

$logFile = '/var/www/html/meu_log.txt';
    $message = 'Executado em ' . date('Y-m-d H:i:s') . PHP_EOL;
    file_put_contents($logFile, $message, FILE_APPEND);
?>
