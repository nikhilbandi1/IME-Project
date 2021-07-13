<html>
<body>

<?php
// echo $_POST["name"];
// echo $_POST['name'];
$name = $_POST['name'];
// echo $name;
$dd = $_POST['description'];
// echo $dd;
$email = $_POST['email'];
// echo $email;

// echo exec("python ni.py $name $dd $email 2>&1");
$command_exec = escapeshellcmd("python3 ni.py $name $dd $email 2>&1");
$str_output = shell_exec($command_exec);
echo $str_output;

?><br>
You Will Get Well Soon
</body>
</html>
