using System;
using System.Net.Http;
using Newtonsoft.Json;

namespace Ex001
{
    class Program
    {
        static void Main(string[] args)
        {

            var client = new HttpClient();
            client.BaseAddress = new Uri("http://127.0.0.1:5000/users/1");
            // Async libera as treds do processador para que outros processos poder rodar
            var httpResponse = client.GetAsync(client.BaseAddress).GetAwaiter().GetResult();
                    
            Console.WriteLine("Resultado da consulta na API\n");
            var resultado = LerRetorno(httpResponse.Content);

            var cabecalho = new Cabecalho();
            cabecalho.Colunas = new Coluna[3];

            cabecalho.Colunas[0] = new Coluna("ID");
            cabecalho.Colunas[1] = new Coluna("Name");
            cabecalho.Colunas[2] = new Coluna("Email \n");

            cabecalho.ImprimirLinha(cabecalho.Colunas);
            System.Console.WriteLine();

            for(int i = 0; i < resultado.Length; i++){
                
                var linha = new Linha();
                linha.Colunas = new Coluna[3];
                linha.Colunas[0] = new Coluna(resultado[i].Id.ToString(), cabecalho.Colunas[0].QteLetras);
                linha.Colunas[1] = new Coluna(resultado[i].Name.ToString(), cabecalho.Colunas[1].QteLetras);
                linha.Colunas[2] = new Coluna(resultado[i].Email.ToString(), cabecalho.Colunas[2].QteLetras);

                linha.ImprimirLinha(linha.Colunas);
                System.Console.WriteLine();
            }
        }

        public static Aluno[] LerRetorno(HttpContent content)
        {
            var minhalista =  content.ReadAsStringAsync().GetAwaiter().GetResult();

            var arrayAlunos = JsonConvert.DeserializeObject<Aluno[]>(minhalista);

            return arrayAlunos;   
        }
    }
}
