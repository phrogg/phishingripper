<html>
	<head>
		<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
	  <link rel="icon" href="/favicon.ico" type="image/x-icon">
	  <style>
		  body{
			  text-align:center;
			  background-color:#7f08e0;
		  }
	  </style>
    <title>PhishingRipper</title>
  </head>
  <body>
		<form action="upload.php?submit=1" method="post" enctype="multipart/form-data">
			<input type="text" name="url" hint="https://blablabtgergerg.com/post.php"/>
			<select name="typ" size="1"><option value="" selected disabled hidden>Request Type</option>
				<option>_POST</option>
				<option>_GET</option>
		</select>

		</form>
  </body>
</html>

<?php
    //exec("phishingripper.py");
?>