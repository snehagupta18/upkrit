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

if(isset($_POST['contact-save']))
{	
	 $name = $_POST['name'];
	 $message = $_POST['message'];
	 $email = $_POST['email'];
	 $phone = $_POST['phone'];

	 $sql_query = "INSERT INTO contact (name,message,email,phone)
	 VALUES ('$name','$message','$email','$phone')";

	 if (mysqli_query($conn, $sql_query)) 
	 {
		echo "Contact Details saved Successfully!!";
	 } 
	 else
     {
		echo "Error: " . $sql . "" . mysqli_error($conn);
	 }
	 mysqli_close($conn);
}
?>