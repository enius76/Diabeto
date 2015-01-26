<?php

	/* renvoi le chemin du fichier */
	echo realpath('legumes.php');
	echo realpath('skel.min.js');

?>

<!DOCTYPE HTML>

<html>
	<head>
		<title>Diab'ON - Catalogue</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
		<script src="../../js/jquery.min.js"></script>
		<script src="../../js/jquery.poptrox.min.js"></script>
		<script src="../../js/jquery.scrolly.min.js"></script>
		<script src="../../js/jquery.scrollgress.min.js"></script>
		<script src="../../js/skel.min.js"></script>
		<script src="../../js/init.js"></script>
		<script src="../../js/change_content.js"></script>
		<noscript>
			<link rel="stylesheet" href="../../css/skel.css" />
			<link rel="stylesheet" href="../../css/style.css" />
			<link rel="stylesheet" href="../../css/style-wide.css" />
			<link rel="stylesheet" href="../../css/style-normal.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
	</head>
	<body>

		<!-- Header -->
			<header id="header">

				<!-- Logo -->
					<h1 id="logo"><a href="index.html">Diab'ON</a></h1>
				
				<!-- Nav -->
					<nav id="nav">
						<ul>
							<li><a href="carnet-de-bord.html"><span class="flaticon-small21"></span>Carnet</a></li>
							<li><a href="alimentation.html"><span class="flaticon-restaurant23"></span>Alimentation</a></li>
							<li><a href="conseils.html"><span class="flaticon-thumbs16"></span>Conseils</a></li>
							<li class="log-on"><a href="profil.html"><span class="flaticon-profile7"></span></a></li>
							<li class="search"><a href="#"><span class="flaticon-dark37"></span></a></li>
						</ul>
					</nav>

			</header>
			
		<!-- Catalogue -->
			<section id="work" class="main style3 primary">
				<div class="content container">
					<header>
						<h2>Catalogue complet des aliments</h2>
						<p> Je n'ai fait le test que pour Aperitifs, Fruits secs et Fruit</p>
					</header>

					<!-- Choix alphabetique -->
						<nav id="catalogue-alphabetique">
	                        <ul>
	                            <li><a href="sub_content/aliments/lettre-a.html">A</a></li>
	                            <li><a href="sub_content/aliments/lettre-b.html">B</a></li>
	                            <li><a href="sub_content/aliments/lettre-c.html">C</a></li>
	                            <li><a href="sub_content/aliments/lettre-d.html">D</a></li>
	                            <li><a href="sub_content/aliments/lettre-e.html">E</a></li>
	                            <li><a href="sub_content/aliments/lettre-f.html">F</a></li>
	                            <li><a href="sub_content/aliments/lettre-g.html">G</a></li>
	                            <li><a href="sub_content/aliments/lettre-h.html">H</a></li>
	                            <li><a href="sub_content/aliments/lettre-i.html">I</a></li>
	                            <li><a href="sub_content/aliments/lettre-j.html">J</a></li>
	                            <li><a href="sub_content/aliments/lettre-k.html">K</a></li>
	                            <li><a href="sub_content/aliments/lettre-l.html">L</a></li>
	                            <li><a href="sub_content/aliments/lettre-m.html">M</a></li>
	                            <li><a href="sub_content/aliments/lettre-n.html">N</a></li>
	                            <li><a href="sub_content/aliments/lettre-o.html">O</a></li>
	                            <li><a href="sub_content/aliments/lettre-p.html">P</a></li>
	                            <li><a href="sub_content/aliments/lettre-q.html">Q</a></li>
	                            <li><a href="sub_content/aliments/lettre-r.html">R</a></li>
	                            <li><a href="sub_content/aliments/lettre-s.html">S</a></li>
	                            <li><a href="sub_content/aliments/lettre-t.html">T</a></li>
	                            <li><a href="sub_content/aliments/lettre-u.html">U</a></li>
	                            <li><a href="sub_content/aliments/lettre-v.html">V</a></li>
	                            <li><a href="sub_content/aliments/lettre-w.html">W</a></li>
	                            <li><a href="sub_content/aliments/lettre-x.html">X</a></li>
	                            <li><a href="sub_content/aliments/lettre-y.html">Y</a></li>
	                            <li><a href="sub_content/aliments/lettre-z.html">Z</a></li>
	                            <div class="clear"></div>
	                        </ul>
		                </nav>
            
            		<!-- Aliments  -->
	                    <div class="container 75% tri-result">
	                    	<div class="table catalogue">
							    <table class="full">
							        <tr class="table-title">
							            <td></td>
							            <td>Nom de l'aliment</td>
							            <td>Calories</td>
							            <td>Protéines</td>
							            <td>Glucides</td>
							            <td>Lipides</td>
							            <td>Quantité</td>
							        </tr>
							        <tr>
							            <td><img src="../../images/catalogue/apericubes.png" alt="Apéricubes" /></td>
							            <td class="label">Apéricube</td>
							            <td>267</td>
							            <td>11.5</td>
							            <td>4.5</td>
							            <td>22.5</td>
							            <td>100 g</td>
							        </tr>
							        <tr>
							            <td><img src="../../images/catalogue/bretzel.png" alt="Bretzel" /></td>
							            <td class="label">Bretzel</td>
							            <td>80</td>
							            <td>2.4</td>
							            <td>10.2</td>
							            <td>3.3</td>
							            <td>1 unité</td>
							        </tr>
							    </table>
							</div>
	                    </div>
	            </div>                  
        	</section>

		<!-- Footer -->
			<footer id="footer">

				<!-- Icons -->
					<ul class="actions">
						<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
						<li><a href="#" class="icon fa-google-plus"><span class="label">Google+</span></a></li>
						<li><a href="#" class="icon fa-dribbble"><span class="label">Dribbble</span></a></li>
						<li><a href="#" class="icon fa-pinterest"><span class="label">Pinterest</span></a></li>
						<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
					</ul>

				<!-- Menu -->
					<ul class="menu">
						<li><a href="mentions-legales.html">Mentions Légales</a></li>
						<li><a href="contact.html">Contact</a></li>
						<li>&copy; Diab'On</li>
					</ul>
			
			</footer>

	</body>
</html>