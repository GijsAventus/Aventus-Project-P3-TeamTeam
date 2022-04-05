<?php
    // DB-credentials.
    $host = 'localhost';
    $db   = 'aventus-176632_wp_mlv2j';
    $user = 'aventus-176632';
    $pass = '&78TYt0hndWhtcsd';
    $charset = 'utf8mb4';


     // Connection string en PDO settings.
     $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
     $options = [
         PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
         PDO::ATTR_EMULATE_PREPARES   => false,
         ];
 
     // Verbinding maken met database.
     try{
         $pdo = new PDO($dsn, $user, $pass, $options);
         //echo "verbinding geslaagd<br>";
     }
     catch (\PDOException $e){
         echo "verbinding niet geslaagd";
         throw new \PDOException($e->getMessage(), (int)$e->getCode());
         
     }   
  
?>