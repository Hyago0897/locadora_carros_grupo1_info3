CREATE TABLE IF NOT EXISTS clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	cpf TEXT(11) NOT NULL,
	endereco TEXT NOT NULL,
	fone TEXT NOT NULL,
	email TEXT,
	login TEXT NOT NULL UNIQUE,
	senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS manutencao (
	modelo TEXT NOT NULL PRIMARY KEY,
	custo REAL NOT NULL,
	descricao TEXT
);

CREATE TABLE IF NOT EXISTS veiculo (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	placa TEXT(7) NOT NULL,
	marca TEXT NOT NULL,
	modelo TEXT NOT NULL,
	cor TEXT,
	descricao TEXT,
	ano TEXT,
	status TEXT NOT NULL,
	FOREIGN key (modelo) REFERENCES manutencao(modelo)
);

CREATE TABLE IF NOT EXISTS contrato (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_veiculo INTEGER NOT NULL,
	id_cliente INTEGER NOT NULL,
	inicio TEXT NOT NULL,
	termino TEXT NOT NULL,
	diaria REAL NOT NULL,
	n_diarias INTEGER NOT NULL,
	status TEXT NOT NULL,
	FOREIGN key (id_veiculo) REFERENCES veiculo(id_veiculo),
	FOREIGN key (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS admin (
	login TEXT PRIMARY KEY,
	senha TEXT NOT NULL,
	nome TEXT NOT NULL
);
