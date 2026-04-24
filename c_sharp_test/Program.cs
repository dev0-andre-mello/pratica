Console.Write("Digite seu nome: ");
string name = Console.ReadLine();
Console.WriteLine($"Seja muito bem vindo(a), {name}!");
Console.Write("Digite o ano do seu nascimento: ");
int year = int.Parse(Console.ReadLine());
int age = 2026 - year;
Console.WriteLine($"Você tem {age} anos.");

if (age >= 18)
{
    Console.WriteLine("Você é maior de idade");

}
else
{
    Console.WriteLine("Você é menor de idade");
}
