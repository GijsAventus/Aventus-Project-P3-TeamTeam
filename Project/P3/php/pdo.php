<?php
     
  //verdindingsvariabelen database 
  $host = 'localhost';
  $db   = 'projectp3';
  $user = 'db_user';
  $pass = ']I(5tpwlmf4qyHnV';
  $charset = 'utf8mb4';
  
  
  //connection string en PDO settings
  $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
  $options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
  ];
  
  
  //verbinding maken met database
  try {
    $pdo = new PDO($dsn, $user, $pass, $options);
  } catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
  }   
    
  ?>
  
  </body>
