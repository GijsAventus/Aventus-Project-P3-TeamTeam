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

     $SQL= 'INSERT INTO portfolio (naam, adres, geboortedatum, werkervaring, studieloopbaan, certificaten, vaardigheden)
            VALUES (naam:, adres:, geboortedatum:, werkervaring:, studieloopbaan:, certificaten:, vaardigheden:)';
    $stmt=  $pdo->prepare($sql);

    $values = [
            'naam'           => $_GET['naam']
            'adres'          => $_GET['adres']
            'geboortedatum'  => $_GET['geboortedatum']
            'hobbyintresse'  => $_GET['hobbyintresse']
            'werkervaring'   => $_GET['werkervaring']
            'studieloopbaan' => $_GET['studieloopbaan']
            'certificaten'   => $_GET['certificaten']
            'vaardigheden'   => $_GET['vaardigheden']

    $stmt->execute($values);    
            
?>