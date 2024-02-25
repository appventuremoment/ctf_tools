<?php
$titles = array("lovestory.txt", "hackerstory.txt", "eggstory.txt", "castlestory.txt", "flag.txt");
//bro thought he was cool by using classes for everything...

class Book {
	public $option;
    public $name;
    public $content;

    function __construct($option) {
        $this->option = intval($option);
        $this->name = $GLOBALS['titles'][$this->option - 1];
        //if option was the flag, don't allow the user to read it
        if ($this->option == 5){
            $this->name = "fakeflag.txt";
        }
    }

    function __tostring(){
        //final defence
        if ($this->name != "fakeflag.txt") $this->name = str_ireplace("flag", "", $this->name);
        //read the file
        $this->content = file_get_contents("books/" . $this->name);
        //make it look nicer
        $this->content = str_replace("\r", "", $this->content);
        $this->content = str_replace("\n", "<br>", $this->content);

        return $this->content;
    }
}

class User {
    public $name;
    function __construct($name) {
        $this->name = $name;
    }
    function __tostring() {
        return $this->name;
    }
}
?>
