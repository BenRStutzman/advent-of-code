using System;
using System.Collections.Generic;
using System.Linq;

namespace _23B
{
    class Program
    {
        private static readonly int NumCups = 1000000;
        
        static void Main(string[] args)
        {
            var cups = new List<int> { 2, 7, 8, 0, 1, 4, 3, 5, 6 };
            for (var i = 9; i < NumCups; i++)
            {
                cups.Add(i);
            }

            for (var i = 0; i < 10000000; i++)
            {
                cups = Shuffle(cups);
            }

            var indexOfOne = cups.IndexOf(0);
            var answer = (cups[indexOfOne + 1] + 1) * (cups[indexOfOne + 2] + 1);
            Console.WriteLine(answer);
        }

        private static List<int> Shuffle(List<int> cups)
        {
            var newCups = new List<int>();
            var currentCup = cups.First();
            var shuffledCups = cups.Skip(1).Take(3);
            var destinationCup = currentCup - 1;
            if (destinationCup < 0)
            {
                destinationCup += NumCups;
            }
            while (shuffledCups.Contains(destinationCup))
            {
                destinationCup--;
                if (destinationCup < 0)
                {
                    destinationCup += NumCups;
                }
            }
            var insertionIndex = cups.IndexOf(destinationCup);
            newCups.AddRange(cups.Skip(4).Take(insertionIndex - 3));
            newCups.AddRange(shuffledCups);
            newCups.AddRange(cups.Skip(insertionIndex + 1));
            newCups.Add(currentCup);
            return newCups;
        }
    }
}
