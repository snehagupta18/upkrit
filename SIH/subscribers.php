<?php
$server_name="localhost";
$username="root";
$password="";
$database_name="upkrit";

$conn=mysqli_connect($server_name,$username,$password,$database_name);
//now check the connection
if(!$conn)
{
	die("Connection Failed:" . mysqli_connect_error());

}

if(isset($_POST['save']))
{	
	 $subscriber_email = $_POST['subscriber_email'];
	 $sql_query = "INSERT INTO subscribers (subscriber_email)
	 VALUES ('$subscriber_email')";

	 if(mysqli_query($conn, $sql_query)) 
	 {
		echo "you are subscribed !";
	 } 
	 else
     {
		echo "Error: " . $sql . "" . mysqli_error($conn);
	 }
	 mysqli_close($conn);
}
?>