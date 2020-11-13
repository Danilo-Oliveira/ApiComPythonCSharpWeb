using System;

namespace Ex001
{
    public class Aluno
    {
        public string Nome { get; set; }   
        public string Email { get; set; }
    }

    public class Coluna
    {
        //Método construtor não tem retorno e possui o mesmo nome da classe
        public Coluna(string conteudo)
        {
            Conteudo = conteudo;
        }

        public Coluna(string conteudo, int qtdeParaCompletar)
        {
            Conteudo = conteudo.PadRight(qtdeParaCompletar, ' ');          
        }

        public string Conteudo;
        public int QteLetras => Conteudo.Length;

    }

    public class Tabela
    {
        public void ImprimirLinha(Coluna[] Colunas)
        {
            for (int i = 0; i < 2; i++)
            {
                Console.Write(Colunas[i].Conteudo);

                if (i < 2)
                {
                    Console.Write("     |     ");
                }

            }
        }
    }
    public class Cabecalho : Tabela
    {
        public Coluna[] Colunas;
    }

    public class Linha : Tabela
    {
        public Coluna[] Colunas;
    }
}