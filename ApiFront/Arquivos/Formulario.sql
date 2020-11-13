-------------------------------------------------------------------------
--Cria a tabela formulario
	if not exists(select * from INFORMATION_SCHEMA.tables where table_name = 'formulario') 
	begin
	create table formulario
	(
		id_pessoas integer identity(1,1) constraint PK_id_pessoas primary key,
		nome_completo varchar(255) not null,
		data_de_nascimento date not null,
		idade int null,
		inserir_genero varchar(9),
		email varchar(40),
		senha varchar(30),
		objetivo_da_graduacao varchar(1000) null
	)
	end
	go

-- Esse if pesquisa na net ai

-- reseta o id no sql
-- DBCC CHECKIDENT('formulario', RESEED, 0)

-- select * from formulario

-- drop table formulario
-------------------------------------------------------------------------
--Cria a Tabela genero
	if not exists(select * from INFORMATION_SCHEMA.tables where table_name = 't_genero')
	begin
	create table t_genero
	(
		id_genero integer identity(1,1)constraint PK_id_genero primary key,
		inserir_genero varchar(9)
	)

	end
	go

-- select * from t_genero

-- drop table t_genero

-------------------------------------------------------------------------
--Caso o masculino e feminino não estao criados, ele cria

	if not exists(select * from t_genero where inserir_genero = 'Masculino')
	begin
		insert into t_genero(inserir_genero) values('Masculino')
	end
	go

	if not exists(select * from t_genero where inserir_genero = 'Feminino')
	begin
		insert into t_genero(inserir_genero) values('Feminino')
	end
	go

	if not exists(select * from t_genero where inserir_genero = 'Outros')
	begin
		insert into t_genero(inserir_genero) values('Outros')
	end
	go
-------------------------------------------------------------------------
--Cria Procedure para retornar genero é a dos Alunos para Aplicação
	if OBJECT_ID('sp_retorna_formulario') is not null
	begin
		drop procedure sp_retorna_formulario
	end
	go

	create procedure sp_retorna_formulario
	as
	begin 
		--Retorna os dados Localizados na t_alunos
		select * from formulario
	end
	go
	sp_retorna_formulario
	go
-------------------------------------------------------------------------
	if OBJECT_ID('sp_retorna_genero') is not null
	begin
		drop procedure sp_retorna_genero
	end
	go

	create procedure sp_retorna_genero
	as
	begin
		--Retorna os dados Localizados na t_genero
		select * from t_genero
	end
	go
	sp_retorna_genero
-------------------------------------------------------------------------

insert into formulario (nome_completo, data_de_nascimento, idade, inserir_genero, email, senha, objetivo_da_graduacao) 
values ('Danilo', '1999/04/21', 20, 'Masculino', 'Ahrkan@gmail.com', '1234', 'sla')

insert into formulario (nome_completo, data_de_nascimento, idade, inserir_genero, email, senha, objetivo_da_graduacao) 
values ('Amanda', '1999/04/21', 20, 'Feminino', '1@gmail.com', '1', 'sla')

insert into formulario (nome_completo, data_de_nascimento, idade, inserir_genero, email, senha, objetivo_da_graduacao) 
values ('Rodrigo', '2000/02/07', 19, 'Masculino', '2@gmail.com', '2', 'sla')

insert into formulario (nome_completo, data_de_nascimento, idade, inserir_genero, email, senha, objetivo_da_graduacao) 
values ('Cafe', '1999/04/21', 20, 'Masculino', '3@gmail.com', '3', 'sla')