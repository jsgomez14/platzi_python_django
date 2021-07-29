<?php
require_once('car.php')
class UberVan extends Car {
    public $typeCarAccepted;
    public $seatsMaterial;

    public function __construct($license, $driver,$typeCarAccepted,$seatsMaterial){
        parent::__construct($license, $driver)
        $this->brand = $typeCarAccepted;
        $this->model = $seatsMaterial;
    }
}
?>