package med.utils;

public class ExtensionFilter implements java.io.FilenameFilter{
    public ExtensionFilter(String extension){
        this.extension = extension;
    }
    
    public boolean accept(java.io.File dir, String name){
        return name.toLowerCase().endsWith(extension);
    }
    private String extension;
}