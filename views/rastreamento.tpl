<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" href="{{get_url('static', path='bootstrap.min.css')}}">
	<link rel="stylesheet" href="{{get_url('static', path='custom.css')}}">
	<script src="{{get_url('static', path='bootstrap.min.js')}}"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>Rastreador</title>
</head>
<body>
	<nav class="navbar navbar-default navbar-dark bg-primary">
		<a class="navbar-brand" href="/">Rastreador</a>
	</nav>
	<main role="main" class="container mt-4 mb-4">
		<h3 class="text-center">{{codigo}}</h3>
		<div class="row d-flex justify-content-center my-4">
			%if valido:
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
					<div class="alert alert-warning" role="alert">
						<p>Esse código não consta no sistema dos Correios. Se sua encomenda foi postada recentemente, tente novamente mais tarde.</p>
					</div>
				%end
			%else:
				<div class="alert alert-danger" role="alert">
					<p>O código que você inseriu é inválido. Lembre-se que códigos de rastreamento tem o seguinte formato: <strong>AA123456789XX</strong></p>
				</div>
			%end
		</div>
		<div class="d-flex justify-content-center mb-5">
			<a href="/"><button class="btn btn-primary">Rastrear outro objeto</button></a>
		</div>
	</main>
	<footer class="footer">
      <div class="container">
        <span class="text-muted">Rastreador™ - Todos os direitos reservados ©</span>
      </div>
    </footer>
</body>
</html>