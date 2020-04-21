<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" href="../css/bootstrap.min.css">
	<script src="../js/bootstrap.min.js"></script>
	<title>Rastreador</title>
</head>
<body>
	<nav class="navbar navbar-dark bg-primary">
		<a class="navbar-brand" href="/">Rastreador</a>
	</nav>
	<div class="container mt-4 mb-4">
		<h3 class="text-center">{{codigo}}</h3>
		<div class="row d-flex justify-content-center my-4">
			%if len(resultado) != 0:
				<ul class="list-group">
				%for evento in resultado:
					<li class="list-group-item">{{evento.get('data')}} - {{evento.get('hora')}} - {{evento.get('local')}}: {{evento.get('evento')}}
					%if evento.get('destino'):
						para {{evento.get('destino')}}
					%end
					</li>
				%end
				</ul>
			%else:
				<div>
					<div class="alert alert-warning" role="alert">
						<p>O código que você inseriu está incorreto ou a encomenda ainda não foi postada. Tente novamente mais tarde.</p>
					</div>
				</div>
			%end
		</div>
	</div>
	<div class="container">
		<div class="row d-flex justify-content-center mb-4">
			<a href="/"><button class="btn btn-primary">Rastrear outro objeto</button></a>
		</div>
	</div>
</body>
</html>