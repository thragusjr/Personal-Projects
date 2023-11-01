package Java.Consultant;

/**
 * Consultant - a class with built in tools used for list modification
 * 
 * 
 * @author Ethan Page
 * @version 30 November 2022
 *
 * isPrime function provided by: https://www.educative.io/answers/how-to-check-if-a-number-is-prime-in-java
 */

 import java.awt.List;
 import java.util.ArrayList;
 
 public class Consultant {
 
     public static void main(String[] args) {

         //Demo some functionality

         System.out.println("Make lot$ of dollar$");
         
         ArrayList<Integer> D = new ArrayList<>();
         ArrayList<Integer> E = new ArrayList<>();
         
         
         //add all numbers from 62000 to 68000 to list D
         for (int i = 62000; i <= 68000; i++) {
             D.add(i);
         }
         
         //use keepPrime to add all prime numbers from list D to list E
         E.addAll(keepPrime(D));
 
         //display list E containing all Primes included
         System.out.println(E);
         System.out.println();
         
         //use sumList to display checksum
         System.out.println("The sum of all prime numbers between 62000 and 68000 is:");
         System.out.println(sumList(E));
         
     }
 
     /**
      * method named count that takes an integer N and returns a list of the first N whole numbers
      * @param listI
      * @param N
      * @return
      */
     public static ArrayList<Integer> count(ArrayList<Integer> listI, int N) {
         ArrayList<Integer> countList = new ArrayList<Integer>();
         for (int i = 0; i < N; i++) {
             int temp = listI.get(i);
             countList.add(temp);
         }
         return countList;
     }
     
     /**
      * method named odds that takes an integer N and returns a list of all 
      * positive, odd numbers less than N
      * @param listII
      * @param N
      * @return
      */
     public static ArrayList<Integer> odds(ArrayList<Integer> listII, int N) {
         ArrayList<Integer> oddsList = new ArrayList<Integer>();
         for (int i = 0; i < N; i++) {
             if (listII.get(i) % 2 > 0) {
                 int temp = listII.get(i);
                 oddsList.add(temp);
             }
         }
         return oddsList;
     }
     
     /**
      * method named addTo that takes a List of integers, an integer N, and 
      * adds N to each element of the list.
      * @param listA
      * @param N
      * @return
      */
     public static ArrayList<Integer> addTo(ArrayList<Integer> listA, int N) {
         ArrayList<Integer> sumList = new ArrayList<Integer>();
         for (int i = 0; i < listA.size(); i++) {
             int sumA = listA.get(i) + N;
             sumList.add(sumA);
         }
         return sumList;
     }
 
     /**
      * method named square that takes a List of integers and returns a list of their squares
      * @param listB
      * @return
      */
     public static ArrayList<Integer> square(ArrayList<Integer> listB) {
         ArrayList<Integer> squareList = new ArrayList<Integer>();
         for (int i = 0; i < listB.size(); i++) {
             int sqr = listB.get(i) * listB.get(i);
             squareList.add(sqr);
         }
         return squareList;
     }
 
     /**
      * method named keepEvens that takes a list of numbers then returns a list of
      * numbers only from the original list that are even
      * @param allNums
      * @return
      */
     public static ArrayList<Integer> keepEvens(ArrayList<Integer> allNums) {
         ArrayList<Integer> evenList = new ArrayList<Integer>();
         for (int i = 0; i < allNums.size(); i++) {
             int counter = allNums.get(i);
             if (counter % 2 == 0) {
                 evenList.add(counter);
             }
         }
         return evenList;
     }
 
     /**
      * isPrime method to determine if a number is Prime
      * provided by: https://www.educative.io/answers/how-to-check-if-a-number-is-prime-in-java
      * @param n
      * @return
      */
     public static boolean isPrime(int n) {
         if (n <= 1) {
             return false;
         }
         for (int i = 2; i <= n / 2; i++) {
             if ((n % i) == 0)
                 return false;
         }
         return true;
     }
 
     /**
      * method named that takes in a list and produces a new list
      * that keeps only prime numbers
      * @param listC
      * @return
      */
     public static ArrayList<Integer> keepPrime(ArrayList<Integer> listC) {
         ArrayList<Integer> primeList = new ArrayList<Integer>();
         for (int i = 0; i < listC.size(); i++) {
             int temp = listC.get(i);
             if (isPrime(temp) == true) {
                 primeList.add(temp);
             }
         }
         return primeList;
     }
 
     /**
      * method named sumList sumList which takes a list of numbers and 
      * returns the sum of all of its elements
      * @param listD
      * @return
      */
     public static ArrayList<Integer> sumList(ArrayList<Integer> listD) {
         ArrayList<Integer> listE = new ArrayList<Integer>();
         int temp = 0;
         for (int i = 0; i < listD.size(); i++) {
             temp += listD.get(i);
         }
         listE.add(temp);
         return listE;
     }
     
     /**
      * method named sevensCounter that sums numbers that are multiples of seven
      * @param listF
      * @return
      */
     public static ArrayList<Integer> sevensCounter(ArrayList<Integer> listF) {
         ArrayList<Integer> listG = new ArrayList<Integer>();
         int temp = 0;
         for (int i = 0; i < listF.size(); i++) {
             if (listF.get(i) % 7 == 0) {
                 temp += listF.get(i);
             }
         }
         listG.add(temp);
         return listG;
     }
 }
 
