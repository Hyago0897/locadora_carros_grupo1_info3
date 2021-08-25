CREATE TABLE cliente (
	id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	cpf TEXT(11) NOT NULL,
	endereco TEXT NOT NULL,
	fone TEXT NOT NULL,
	`e-mail` TEXT,
	login TEXT NOT NULL,
	senha TEXT NOT NULL,
	data_nasci TEXT NOT NULL,
	`n_CNH` TEXT NOT NULL
);

CREATE TABLE veiculo (
	id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
	placa TEXT(7) NOT NULL,
	marca TEXT NOT NULL,
	modelo TEXT NOT NULL,
	cor TEXT,
	descrisao TEXT,
	ano TEXT,
	status_veiculo TEXT NOT NULL
);