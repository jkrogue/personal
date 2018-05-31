import java.util.Scanner;
import java.nio.file.*;
import java.io.File;

public class SeparateFirstLast {
	public static void main (String[] args) throws Exception{
		Scanner fileScanner = new Scanner (new File(args[0]));
		fileScanner.useDelimiter("(,|\\n)");
		String outputString = "";
		while (fileScanner.hasNext()){
			String next = fileScanner.next();
			if (next.contains("@")){ //email address, add to string and move on
				outputString += "," + next + "\n";

			}else{ //separate first and last names
				try{
					//System.out.println("trying with " + next);
					Scanner nameScanner = new Scanner(next);
					String firstName = nameScanner.next();
					String lastName = nameScanner.next();
					System.out.println(firstName + "," + lastName);
					outputString += firstName + "," + lastName;
				}catch(Exception e){}
			}
		}
		Files.write(Paths.get(args[1]), outputString.getBytes());

		System.out.println(outputString);
	}
}