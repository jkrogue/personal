//------------------------------------------------------------//
//  JavaGetUrl.java:                                          //
//------------------------------------------------------------//
//  A Java program that demonstrates a procedure that can be  //
//  used to download the contents of a specified URL.         //
//------------------------------------------------------------//
//  Code created by Developer's Daily                         //
//  http://www.DevDaily.com                                   //
//------------------------------------------------------------//

import java.io.*;
import java.net.*;
import java.util.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;

public class UcsfEmailParser {

   public static void main (String[] args) {

      //-----------------------------------------------------//
      //  Step 1:  Start creating a few objects we'll need.
      //-----------------------------------------------------//

      URL u;
      InputStream is = null;
      DataInputStream dis; 
      String s;
      String name = "";
      String email = ""; 
      boolean firstEntry = false;
	boolean inBody = false;
	boolean next = false;
	boolean inDiv = false;
	ArrayList<NameEmailPair> nameEmailPairs = new ArrayList<NameEmailPair>();
	
	

      try {

         //------------------------------------------------------------//
         // Step 2:  Create the URL.                                   //
         //------------------------------------------------------------//
         // Note: Put your real URL here, or better yet, read it as a  //
         // command-line arg, or read it from a file.                  //
         //------------------------------------------------------------//

         u = new URL(args[0]);

         //----------------------------------------------//
         // Step 3:  Open an input stream from the url.  //
         //----------------------------------------------//

         is = u.openStream();         // throws an IOException

         //-------------------------------------------------------------//
         // Step 4:                                                     //
         //-------------------------------------------------------------//
         // Convert the InputStream to a buffered DataInputStream.      //
         // Buffering the stream makes the reading faster; the          //
         // readLine() method of the DataInputStream makes the reading  //
         // easier.                                                     //
         //-------------------------------------------------------------//

         dis = new DataInputStream(new BufferedInputStream(is));

         //------------------------------------------------------------//
         // Step 5:                                                    //
         //------------------------------------------------------------//
         // Now just read each record of the input stream, and print   //
         // it out.  Note that it's assumed that this problem is run   //
         // from a command-line, not from an application or applet.    //
         //------------------------------------------------------------//

         while ((s = dis.readLine()) != null) {
            	if (s.contains("tbody")){
			inBody = true;
		}	
		if (inBody){
			if(s.contains("<tr>"))
				firstEntry = true;
			else if(s.contains("div"))
				inDiv = true;
			else {
				if (firstEntry && s.contains("<a")){
					next = true;
					inDiv = false;
				}
				else if(next){
					name = parseText(s);
					firstEntry = false;
					next = false;

				}
				else if (s.contains("@") && !s.contains("mailto") && !inDiv){
					email = parseText(s); 
					//NameEmailPair pair = new NameEmailPair(name, email);
					//System.out.println(pair);
					nameEmailPairs.add(new NameEmailPair(name, email));
				}
			}
		}
		//System.out.println(s);
         }

	writeToFile(nameEmailPairs, args[1]);
	//System.out.println(nameEmailPairs);

      } catch (MalformedURLException mue) {

         System.out.println("Ouch - a MalformedURLException happened.");
         mue.printStackTrace();
         System.exit(1);

      } catch (IOException ioe) {

         System.out.println("Oops- an IOException happened.");
         ioe.printStackTrace();
         System.exit(1);

      } finally {

         //---------------------------------//
         // Step 6:  Close the InputStream  //
         //---------------------------------//

         try {
            is.close();
         } catch (IOException ioe) {
            // just going to ignore this one
         }

      } // end of 'finally' clause

   }  // end of main

   private static String parseText(String text){
	String parsedText = "";
	Scanner nameScan = new Scanner(text);
	while(nameScan.hasNext()){
		String next = nameScan.next();
		if (next.contains("</a"))
			break;
		if (parsedText.length() != 0)
			parsedText += " ";
		parsedText += next;
	}
	return parsedText;

   }

   private static boolean writeToFile (ArrayList<NameEmailPair> nameEmailPairs, String fileName) throws IOException{
	String toWrite = "";
	int size = nameEmailPairs.size();
	for (int i = 0; i< size; i++){
		toWrite += nameEmailPairs.get(i).toString() + "\n";
	}	
	Files.write(Paths.get(fileName), toWrite.getBytes());
	return true;
   }


} // end of class definition

