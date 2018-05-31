import org.apache.commons.csv.*;

public class ReportViewerIO{
	public static java.util.ArrayList<CSVRecord> parseCSV(String filename){
		try{
			java.io.File csvData = new java.io.File(filename);
			java.util.ArrayList<CSVRecord> csvList = new java.util.ArrayList<CSVRecord>();
			CSVParser parser = CSVParser.parse(csvData, java.nio.charset.Charset.defaultCharset(),CSVFormat.EXCEL);
	 		for (CSVRecord csvRecord : parser) {
	 			csvList.add(csvRecord);
			}
			return csvList;
		}catch(Exception e){
			return null;
		}
	}
}