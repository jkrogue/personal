/*
 * Name = NameScanner.java
 * Designed by Justin Krogue, MD in San Francisco, CA
 */

import java.util.Scanner;

public class NameScanner{
	public static void main (String[] args){
		String firstName = "";
		String lastName = "";
		Scanner nameScanner = new Scanner(System.in);
		System.out.print("Enter your first name: ");
		firstName = nameScanner.next();
		System.out.print("Enter your last name: ");
		lastName = nameScanner.next();
		System.out.println("Your name is: " + firstName + " " + lastName);
	}
}