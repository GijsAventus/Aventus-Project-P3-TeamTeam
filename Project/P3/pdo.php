<!doctype html>
<html lang="en">
  <head>    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PHP Script</title>
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
  <p>Tekst.</p>
  <?php
   
  function preprint_r( $arr ) {
    echo '<pre>'; 
    print_r( $arr );
    echo '</pre>'; 
  }  

  
  //verdindingsvariabelen database 
  $host = 'localhost';
  $db   = 'projectp3';
  $user = 'db_user';
  $pass = 'BTFe/@mze_K@JNGb';
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
    echo('Connectie succesvol.');
  } catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
  }   
    
  ?>
  
  </body>
</html>





