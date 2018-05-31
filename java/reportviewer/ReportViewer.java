public class ReportViewer{

	public static void main (String[] args){
		if (args.length != 0){
			ReportViewerFrame frame = new ReportViewerFrame(args[0]);
		}
		else System.out.println("Enter a filename to use");
	}
}