<?php

// Test1.1
echo "Test1.1<br>";
$row = 5;
$loop = 1;

for($loop;$loop<=5;$loop++)
{
	$check = 1;
	for ($check;$check<=5;$check++)
		{
		if ($check >= $row) {echo "o";}
		else {echo "&nbsp&nbsp";}
		}
	$row--;
	echo "<br>";
}

//Test1.2
echo "Test1.2<br>";
$min = 5;
$max = 5;
$loop = 1;

for($loop;$loop<=5;$loop++)
{
	$check = 1;
	for ($check;$check<=9;$check++)
		{
		if ($min <= $check && $check <= $max) {echo "o";}
		else {echo "&nbsp&nbsp";}
		}
	$min--;
	$max++;
	echo "<br>";
}
 ?>
