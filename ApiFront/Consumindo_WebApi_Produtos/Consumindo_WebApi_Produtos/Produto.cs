using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Consumindo_WebApi_Produtos
{
    public  class Produto
    {

        [JsonProperty("id")]
        public int id { get; set; }
        [JsonProperty("name")]
        public string name { get; set; }
        [JsonProperty("email")]
        public string email { get; set; }
        public List<Child> Children { get; set; } = new List<Child>();
    }

    public class Child
    {
        public string Id { get; set; }

        public string Name { get; set; }

        public string email { get; set; }
    }

}
