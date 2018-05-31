
import javax.swing.JFrame;
import org.apache.commons.csv.*;

public class ReportViewerFrame extends JFrame{
	
	public ReportViewerFrame(String filename){
		super ("Report Viewer");
		this.getContentPane().add(new javax.swing.JEditorPane());	
		this.getContentPane().add(new javax.swing.JButton("Hello"));
		this.pack();
		this.setVisible(true);
		java.util.ArrayList<CSVRecord> csvList = ReportViewerIO.parseCSV(filename);
		for (int i = 0; i< csvList.size(); i++){
			CSVRecord record = csvList.get(i);
			for (int j = 0; j < record.size(); j++){
				System.out.println(record.get(j));
			}
		}

	}
}