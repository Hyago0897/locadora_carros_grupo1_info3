CREATE TABLE IF NOT EXISTS cliente (
	id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	cpf TEXT(11) NOT NULL,
	endereco TEXT NOT NULL,
	fone TEXT NOT NULL,
	`e-mail` TEXT,
	login TEXT NOT NULL,
	senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS manutencao (
	modelo TEXT NOT NULL PRIMARY KEY,
	custo_mm REAL NOT NULL,
	descricao TEXT
);

CREATE TABLE IF NOT EXISTS veiculo (
	id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
	placa TEXT(7) NOT NULL,
	marca TEXT NOT NULL,
	modelo TEXT NOT NULL,
	cor TEXT,
	descricao TEXT,
	ano TEXT,
	status_veiculo TEXT NOT NULL,,
	FOREIGN key (modelo) REFERENCES manutencao(modelo)
);

CREATE TABLE IF NOT EXISTS contrato (
	id_contrato INTEGER PRIMARY KEY AUTOINCREMENT,
	id_veiculo INTEGER NOT NULL,
	id_cliente INTEGER NOT NULL,
	data_inicio TEXT NOT NULL,
	data_termino TEXT NOT NULL,
	preco_diaria REAL NOT NULL,
	seguro TEXT NOT NULL,
	n_diarias INTEGER NOT NULL,
	status_contrato TEXT NOT NULL,
	FOREIGN key (id_veiculo) REFERENCES veiculo(id_veiculo),
	FOREIGN key (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS admin (
	login TEXT PRIMARY KEY,
	senha TEXT NOT NULL,
	nome TEXT NOT NULL
);