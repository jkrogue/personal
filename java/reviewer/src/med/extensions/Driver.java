package med.extensions;

public class Driver{

    public static void main(String[] args) throws Exception{
        System.out.print("Please enter the directory to be changed: ");
        java.util.Scanner scan = new java.util.Scanner(System.in);
        String directory = scan.next();
        System.out.print("Please enter the original extension (e.g., \"html\"): ");
        String oldExt = scan.next();
        System.out.print("Please enter the extension to change to (e.g., \"htm\"): ");
        String newExt = scan.next();
        
        java.io.File fileDir = new java.io.File(directory);
        if (!fileDir.exists() || !fileDir.isDirectory()){
            System.out.println("Directory: \"" + directory + "\" doesn't exist.");
            System.exit(0);
        }
        
        java.io.File[] files = fileDir.listFiles(new med.utils.ExtensionFilter(oldExt));
        for (int i = 0; i < files.length; i++){
            if (!files[i].exists() || files[i].isDirectory()){
                System.out.println("File: \"" + files[i].getName() + "\" doesn't exist");
            }
            else{
                try{
                    //System.out.println("File: \"" + files[i].getName() + "\" exists");
                    String oldFilepath = files[i].getCanonicalPath();
                    String newFilepath = oldFilepath.substring(0, oldFilepath.indexOf(oldExt)) + newExt;
                    System.out.println("Changing \"" + oldFilepath + "\" to \"" + newFilepath + "\"");
                    files[i].renameTo(new java.io.File(newFilepath));
                }
                catch(Exception e){
                    System.out.println("Error changing \"" + files[i].getName() + "\"");
                }
            }
        }
    }

    
}