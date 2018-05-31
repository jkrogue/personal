
public class ImpressionParser{

   static String inputFn = "";
   static String outputFn = "";

   /*
    * args[0] = input filename
    * args[1] = output filename
    */
   public static void main (String[] args){
      if (args.length == 0){
         System.out.println("no input or output filename entered");
         System.exit(0);
      }
      if (args.length == 1){
         System.out.println("no output filename entered");
         System.exit(0);
      }
      inputFn = args[0];
      outputFn = args[1];
      try{
         String outputText = "";
         java.util.Scanner rowParser = new java.util.Scanner(new java.io.File(inputFn));
         rowParser.useDelimiter("\\n(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"); //Matches all new lines that are not inside of quotes (by finding only new lines followed by even numbers of quotes)
         while (rowParser.hasNext()){
            String nextLine = rowParser.next();
            java.util.Scanner columnParser = new java.util.Scanner(nextLine);
            columnParser.useDelimiter(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)"); //Matches all commas that are not inside of quotes (by finding only new lines followed by even numbers of quotes)
            while (columnParser.hasNext()){
               String next = columnParser.next();
               outputText += next;
               if (columnParser.hasNext()){
                  outputText += ",";
               }
               if (next.contains("IMPRESSION:")){   //This means we're in report text and should pull out just impression
                  String[] impressionSplit = next.split("IMPRESSION:\\s",2);
                  if (impressionSplit.length < 2){
                  }else{
                     outputText += "\"" + impressionSplit[1] + ",";
                  }
               }
            }
            outputText += "\n";
         }
         java.nio.file.Files.write(java.nio.file.Paths.get(outputFn), outputText.getBytes());


      }catch (Exception e){
         System.out.println("Error occured:\n" + e);
         System.exit(0);
      }
   }
}