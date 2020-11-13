import pyodbc
import requests
import json

from flask import Flask, render_template, request, make_response, escape, session, url_for, redirect, flash


app = Flask(__name__)
app.secret_key = "flash message"
app.config['SECRET_KEY'] = "1234"


@app.route('/loginUsuario')
def loginUsuario():
    return render_template('login.html')

#--------------------------------------------------------------------------------------#
@app.route('/')
def index():
    return render_template('index.html')

#--------------------------------------------------------------------------------------#


def conexao():

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          "DESKTOP-CKIJDQ3\SQLEXPRESS"+';DATABASE='+"Danilo"+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    return cursor

#--------------------------------------------------------------------------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        emailForm = request.form['email']
        passwordForm = request.form['password']

        global email_global    

        email_global = emailForm       
      
        emailAdmim = request.form['email']
        passwordAdmim = request.form['password']
        cursor = conexao()
        sql = "select email from formulario where email = '{}' and senha = '{}'".format(
            emailForm, passwordForm)
        cursor.execute(sql)
        result_set = cursor.fetchall()

        aut = False
        for row in result_set:
            if(row.email != ''):
                aut = True

        if(aut == True and emailAdmim == 'Ahrkan@gmail.com' and passwordAdmim == '1234' or emailAdmim == '2@2' and passwordAdmim == '2'):
            session['autenticacao'] = True
            return redirect(url_for('lista'))

        if(aut == True and emailAdmim == '1@1' and passwordAdmim == '1'):
            session['autenticacao'] = True
            return redirect(url_for('index'))

        if(aut == True):
            session['autenticacao'] = True 
            return redirect(url_for('meuPerfil'))
        else:
            return redirect(url_for('loginUsuario'))
       

#--------------------------------------------------------------------------------------#
@app.route('/logout')
def logout():
    session.pop('autenticacao', None)  # Apaga os dados de login lá da session
    return redirect(url_for('index'))

#--------------------------------------------------------------------------------------#
@app.route('/cadastro', methods=['POST'])
def resultado():

        name = request.form['Name']
        email = request.form['Email']

        resultJson = requests.post('http://127.0.0.1:5000/users', json={'name': name, 'email': email})

        return redirect("http://127.0.0.1:8000")

#--------------------------------------------------------------------------------------#
@app.route('/list/')
def lista():
    cursor = conexao()

    cursor.execute("SELECT * FROM formulario")

    result_set = cursor.fetchall()

    resultJson = requests.get('http://127.0.0.1:5000/users')

    resultJson.json()
    print(resultJson.json())

    #return render_template('tabela.html', listando=result_set)
    return render_template('tabela.html', listando=resultJson.json())

#--------------------------------------------------------------------------------------#
@app.route('/editar/<email>', methods=['PUT'])
def editar(email):
    if request.method == 'POST':

        name = request.form['NameU']

        password = request.form['SenhaU']

        cursor = conexao()

        cursor.execute("Update formulario set nome_completo = '" + name + "', data_de_nascimento = '" + nascimento + "', idade = '" + idade + "', inserir_genero = '" +
                       genero + "', senha = '" + password + "', objetivo_da_graduacao = '" + objetivo + "' where email ='" + email_global + "'")

        cursor.commit()
        cursor.close()

        return redirect("http://127.0.0.1:8000/meuPerfil")

#--------------------------------------------------------------------------------------#
@app.route('/excluir/<emailUsr>')
def excluir(emailUsr):

    cursor = conexao()

    cursor.execute("DELETE from formulario where email ='" + emailUsr + "'")

    flash("Usuário Excluido com sucesso!")
    cursor.commit()
    cursor.close()

    return redirect("http://127.0.0.1:8000/")
    return emailUsr

#--------------------------------------------------------------------------------------#
@app.route('/editarAdmim/', methods=['PUT'])
def editarAdmim():

    id_pessoas = request.form['id']
    name = request.form['Name']
    email = request.form['Email']

    cursor.execute("Update formulario set nome_completo = '" + name + "', data_de_nascimento = '" + nascimento + "', idade = '" + idade + "', inserir_genero = '" +
                    genero + "', email = '" + email + "', senha = '" + password + "', objetivo_da_graduacao = '" + objetivo + "' where id_pessoas ='" + id_pessoas + "'")
    cursor.commit()
    cursor.close()

    return redirect("http://127.0.0.1:8000/list/")

#--------------------------------------------------------------------------------------#
@app.route('/excluirAdmim/<idUsr>')
def excluirAdmim(idUsr):

    cursor = conexao()

    cursor.execute("DELETE from formulario where id_pessoas ='" + idUsr + "'")

    flash("Usuário Excluido com sucesso!")
    cursor.commit()
    cursor.close()

    return redirect("http://127.0.0.1:8000/list/")
    return idUsr


if __name__ == '__main__':
    app.run(port=8000)
