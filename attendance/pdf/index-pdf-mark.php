<?Php
require "config.php"; // connection to database 

require('fpdf.php');
$pdf = new FPDF(); 
$pdf->AddPage();
$id=$_GET['id'];  // collect student id from URL 
if(!is_numeric($id)){
exit;
}
$count=$count=$dbo->prepare("select id,name,class,social,science,math, ( social + science + math) AS total from student3 where id=:id"); // 
$count->bindParam(":id",$id,PDO::PARAM_INT,1);

if($count->execute()){
$row = $count->fetch(PDO::FETCH_OBJ);

//$pdf->Image('../images/top2.jpg',10,10);
$pdf->SetFont('Arial','BU',20);
$pdf->SetXY(80,50);
$pdf->Cell(30,10,'MARK SHEET',0,0,L,false); // First header column 
$pdf->SetY(80);
$pdf->SetFont('Arial','B',16);
$pdf->Cell(30,10,'ID:',0,0,L,false); 
$pdf->SetFont('Arial','',14);
$pdf->Cell(40,10,$row->id,0,1,L,false); 

$pdf->SetFont('Arial','B',16);
$pdf->Cell(30,10,'NAME:',0,0,L,false);  
$pdf->SetFont('Arial','',14);
$pdf->Cell(40,10,$row->name,0,0,L,false); 

$pdf->SetFont('Arial','B',16);
$pdf->Cell(30,10,'CLASS:',0,0,L,false); 
$pdf->SetFont('Arial','',14);
$pdf->Cell(40,10,$row->class,0,0,L,false); 

$pdf->SetY(110);
$pdf->Line(10,100,190,100);
$pdf->SetXY(30,130);
$pdf->SetFont('Arial','UB',16);
$pdf->Cell(100,10,'SUBJECT:',0,0,L,false);  
$pdf->Cell(50,10,'MARK',0,1,L,false);  
$pdf->SetFont('Arial','',14);
$pdf->SetX(30);
$pdf->Cell(100,10,'SOCIAL',0,0,L,false);  
$pdf->Cell(50,10,$row->social,0,1,L,false); 

$pdf->SetX(30);
$pdf->Cell(100,10,'SCIENCE',0,0,L,false);  
$pdf->Cell(50,10,$row->science,0,1,L,false); 

$pdf->SetX(30);
$pdf->Cell(100,10,'MATH',0,0,L,false); 
$pdf->Cell(50,10,$row->math,0,1,L,false); 

$pdf->Line(30,170,150,170);

$pdf->SetX(30);
$pdf->Cell(98,10,'TOTAL',0,0,L,false); 
$pdf->Cell(50,10,$row->total,0,1,L,false);

$pdf->SetXY(160,220);
$pdf->Cell(50,10,'Signature',0,1,L,false);
$pdf->Output();
}else{
print_r($dbo->errorInfo()); 	
}	
?>