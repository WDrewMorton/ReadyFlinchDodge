using System;
using System.Random;

Random RNG = new Random();

public class ReadyDodgeYell
{

    public startGame()
    {
        String name1;
        String name2;
        int health = 100;

        String[] actions = ["Attack", "Dodge", "Yell"];

    }

    static int Main(string[] args)
    {
        Player p1 = new Player();
        Player p2 = new Player();

        startgame();

        Console.WriteLine("***** My First C# App *****");
        Console.WriteLine("Hello World!");
        Console.WriteLine();
        Console.ReadLine();

        return 0;
    }
}

public class Player
{
    public string name;
    public int health = 100;
    String[] actions = ["Attack", "Dodge", "Yell"];
    Boolean speed = false;
    Boolean confident = false;
    public Player(string name, int health, String[] actions, Boolean speed, Boolean confident)
    {
        this.name = name;
        this.health = health;
        this.actions = actions;
        this.speed = speed;
        this.confident = confident;
    }
}