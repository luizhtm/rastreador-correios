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
		<h3 class="text-center">Rastreie suas encomendas do Correios</h3>
		<div class="d-flex justify-content-center mt-4">
			<form class="form-inline" action="/rastrear" method="POST">
				<div class="col-auto">
					<input class="form-control" name="codigo" type="search" placeholder="Código" aria-label="Search" required>
				</div>
				<div class="col-auto">
					<button class="btn btn-primary" type="submit">Rastrear</button>
				</div>
			</form>
		</div>
	</main>
	<footer class="footer">
      <div class="container text-center">
        <span class="text-muted">Rastreador™ - Todos os direitos reservados ©</span>
      </div>
    </footer>
</body>
</html>