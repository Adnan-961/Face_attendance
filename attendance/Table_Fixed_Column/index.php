<!DOCTYPE html>
<?php
 $host = "127.0.0.1";
$username = "root";
$pass = "";
$con = mysqli_connect($host, $username, $pass, "student_db");
?>
<html lang="en">


<head>
	<title>Table V05</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>

<body>

	
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100 ver1">
					<div class="table100-firstcol">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Student Name
</th>
								</tr>
							</thead>
							<tbody>
								<tr class="row100 body">
									<td class="cell100 column1">Brandon Green</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Kathy Daniels</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Elizabeth Alvarado</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Michael Coleman</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Jason Cox</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Christian Perkins</td>
								</tr>

								<tr class="row100 body">
									<td class="cell100 column1">Emily Wheeler</td>
								</tr>
							</tbody>
						</table>
					</div>
					
					<div class="wrap-table100-nextcols js-pscroll">
						<div class="table100-nextcols">
							<table>
								<thead>
									<tr class="row100 head">
										<th class="cell100 column2">Major</th>
										<th class="cell100 column3">Date</th>
										<th class="cell100 column4">Attendant</th>
										
									</tr>
								</thead>
								<tbody>
									<tr class="row100 body">
										<td class="cell100 column2">CMO</td>
										<td class="cell100 column3">16 Nov 2012</td>
										<td class="cell100 column4">16 Nov 2017</td>
										
										
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">Marketing</td>
										<td class="cell100 column3">16 Nov 2015</td>
										<td class="cell100 column4">30 Nov 2017</td>
										
										
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">CFO</td>
										<td class="cell100 column3">16 Nov 2013</td>
										<td class="cell100 column4">30 Nov 2017</td>
									
										
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">Designer</td>
										<td class="cell100 column3">16 Nov 2013</td>
										<td class="cell100 column4">30 Nov 2017</td>
									
										
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">Developer</td>
										<td class="cell100 column3">16 Nov 2017</td>
										<td class="cell100 column4">30 Nov 2017</td>
									
										
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">Sale</td>
										<td class="cell100 column3">16 Nov 2016</td>
										<td class="cell100 column4">30 Nov 2017</td>
									
									
									</tr>

									<tr class="row100 body">
										<td class="cell100 column2">Support</td>
										<td class="cell100 column3">16 Nov 2013</td>
										<td class="cell100 column4">30 Nov 2017</td>
									
									
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>


<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
	<script>
		$('.js-pscroll').each(function(){
			var ps = new PerfectScrollbar(this);

			$(window).on('resize', function(){
				ps.update();
			})

			$(this).on('ps-x-reach-start', function(){
				$(this).parent().find('.table100-firstcol').removeClass('shadow-table100-firstcol');
			});

			$(this).on('ps-scroll-x', function(){
				$(this).parent().find('.table100-firstcol').addClass('shadow-table100-firstcol');
			});

		});

		
		
		
	</script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>