<?php
//include connection file 
include_once("connection.php");
include_once('fpdf/fpdf.php');

class PDF extends FPDF
{
// Page header
function Header()
{
    // Logo
    
    $this->SetFont('Arial','B',13);
    // Move to the right
    $this->Cell(80);
    // Title
    //$this->Cell(80,10,'Students List',1,0,'C');
    // Line break
    $this->Ln(20);
	$this->Cell(65);
	$this->Cell(00,00,'Attendance List');
	$this->Ln(10);
}

// Page footer
function Footer()
{
    // Position at 1.5 cm from bottom
   
    // Arial italic 8
    $this->SetFont('Arial','I',8);
    // Page number
    $this->Cell(0,10,'Page '.$this->PageNo().'/{nb}',0,0,'C');
	
	// Position at 2.0 cm from bottom
    $this->SetY(-20);
    // Arial italic 8
    $this->SetFont('Arial','B','I',8);
    // Page number
    $this->Cell(0,10,'',0,0,'C');
}
}

$db = new dbObj();
$connString =  $db->getConnstring();
$display_heading = array('id'=>'ID', 'first_name'=> 'FirstName', 'last_name'=> 'LastName','is_attendant'=> 'is_attendant','date'=> 'Attendant','major'=>'Date','timestamp'=> 'timestamp','action'=> 'action');

$result = mysqli_query($connString, "SELECT id,first_name,last_name,date,is_attendant FROM attendance ORDER BY date ASC,first_name,id") or die("database error:". mysqli_error($connString));
$header = mysqli_query($connString, "SHOW columns FROM attendance");

$pdf = new PDF();
//header
$pdf->AddPage();
//foter page
$pdf->AliasNbPages();
$pdf->SetFont('Arial','B',12);
foreach($header as $heading) {
$pdf->Cell(40,12,$display_heading[$heading['Field']],1);
}
foreach($result as $row) {
$pdf->Ln();
foreach($row as $column)
$pdf->Cell(40,12,$column,1);
}
$pdf->Output();
?>