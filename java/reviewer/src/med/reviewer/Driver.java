//
//  Driver.java
//  
//
//  Created by Justin Krogue on 9/27/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//


package med.reviewer;

import java.util.Calendar;
import med.utils.JTextFieldLimit;
import med.utils.DateUtils;

public class Driver {

	private static final String DIRECTORY_LOCATION_FILENAME = "dir_location.txt";
	private static String reviewDirectory = "";
	private static final String EXTENSION = ".html";
	private static final String EXTENSION_SHORT = ".htm";
	private static final String EXTENSION_PDF = ".pdf";
	private static java.util.Date date;
	private static Calendar cal;
	
	public static void main(String[] args) throws Exception{
		
		//Runtime.getRuntime().exec("open -a \"/Applications/Google Chrome.app\" \"/Users/jkrogue/Documents/medical school/reviewer/files/html/09262011.html\"");
		date = new java.util.Date();
		cal = Calendar.getInstance();
		
		getReviewDirectory();
		loadStartGUI();

	}

	private static void getReviewDirectory(){
		try{
			java.util.Scanner scan = new java.util.Scanner(new java.io.File(DIRECTORY_LOCATION_FILENAME));
			reviewDirectory = scan.nextLine();
			System.out.println(reviewDirectory);
		}
		catch (Exception e){
			javax.swing.JOptionPane.showMessageDialog(null, "Can't find/read the file that contains the location of the review files: \"" + DIRECTORY_LOCATION_FILENAME + "\"",
					"Error", javax.swing.JOptionPane.ERROR_MESSAGE);

		}
	}
	
	private static void loadStartGUI(){
		final javax.swing.JPanel panel = new javax.swing.JPanel();
		panel.add(new javax.swing.JLabel("Enter today's date:\t"));
		
		cal.setTime(date);
		
		final javax.swing.JTextField monthF = new javax.swing.JTextField(2);
		monthF.setDocument(new JTextFieldLimit(2));
		int month = cal.get(Calendar.MONTH) + 1;
		monthF.setText("" + month);
		
		final javax.swing.JTextField dayF = new javax.swing.JTextField(2);
		dayF.setDocument(new JTextFieldLimit(2));
		dayF.setText("" + cal.get(Calendar.DAY_OF_MONTH));
		
		final javax.swing.JTextField yearF = new javax.swing.JTextField(4);
		yearF.setDocument(new JTextFieldLimit(4));
		yearF.setText("" + cal.get(Calendar.YEAR));

		panel.add(monthF);
		panel.add(dayF);
		panel.add(yearF);
		
		javax.swing.JButton button = new javax.swing.JButton("Submit");
		panel.add(button);
		
		final javax.swing.JFrame frame = new javax.swing.JFrame("Enter date");
        frame.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().add(panel);
		frame.pack();
		frame.setVisible(true);
		
		button.addActionListener(new java.awt.event.ActionListener(){
			public void actionPerformed(java.awt.event.ActionEvent e){
								 int year = Integer.parseInt(yearF.getText());
								 int month = Integer.parseInt(monthF.getText());
								 int day = Integer.parseInt(dayF.getText());
				cal.set(year, month - 1, day);
				if(DateUtils.isValidDate(month, day, year)){
					date = cal.getTime();
					frame.setVisible(false);
					loadMainGUI();			 
				}
				else{
					cal.setTime(date);
					javax.swing.JOptionPane.showMessageDialog(panel, "Please enter a valid date in the format MM/DD/YYYY", 
						"Invalid Date", javax.swing.JOptionPane.INFORMATION_MESSAGE);
				}
			}
		});
		button.getRootPane().setDefaultButton(button);
	}
	
	private static void loadMainGUI(){
		final javax.swing.JFrame frame = new javax.swing.JFrame("Files to review");
        frame.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);

		java.util.ArrayList<String> filesToSearchFor = getFiles();
		java.util.ArrayList<java.io.File> filesFound = new java.util.ArrayList<java.io.File>();
		
		//System.out.println("Size: " + filesToSearchFor.size());
		for(int i = 0; i < filesToSearchFor.size(); i++){
			java.io.File file = new java.io.File(reviewDirectory + filesToSearchFor.get(i) + EXTENSION);
			if (file.exists())
				filesFound.add(file);
			else{
				file = new java.io.File(reviewDirectory + filesToSearchFor.get(i) + EXTENSION_SHORT);
				if (file.exists())
					filesFound.add(file);
				else{
					file = new java.io.File(reviewDirectory + filesToSearchFor.get(i) + EXTENSION_PDF);
					if (file.exists())
						filesFound.add(file);
				}
			}
			//System.out.println(filesToSearchFor.get(i));
		}
		
		
		final javax.swing.JPanel panel = new javax.swing.JPanel();
		panel.setLayout(new javax.swing.BoxLayout(panel, javax.swing.BoxLayout.Y_AXIS));
		for (int i = 0; i < filesFound.size(); i++){
			final java.io.File file = filesFound.get(i);

			javax.swing.JPanel row = new javax.swing.JPanel();
			final javax.swing.JLabel label = new javax.swing.JLabel(convertFilenameToString(file.getName()));
			label.setForeground(java.awt.Color.RED);
			javax.swing.JButton button = new javax.swing.JButton("View");
			button.addActionListener(new java.awt.event.ActionListener(){
				public void actionPerformed(java.awt.event.ActionEvent e){
					try{
						String[] toRun = {"open", file.getCanonicalPath()};
						for(String string: toRun){
							System.out.print(string + " ");
						}
						Runtime.getRuntime().exec(toRun);
						label.setForeground(java.awt.Color.GREEN);
					}catch(java.io.IOException ex){
						javax.swing.JOptionPane.showMessageDialog(panel, "Error encountered while trying to open \""
									+ file.getName() + "\"", "Unable to open file", 
									javax.swing.JOptionPane.ERROR_MESSAGE);
					}
				}
			});
			row.add(label);
			row.add(button);
			
			panel.add(row);
		}
		
		javax.swing.JLabel label = new javax.swing.JLabel("Do more?");
		panel.add(label);
		
		javax.swing.JPanel buttonPanel = new javax.swing.JPanel();
		javax.swing.JButton button = new javax.swing.JButton("Yes");
		button.addActionListener(new java.awt.event.ActionListener(){
								 public void actionPerformed(java.awt.event.ActionEvent e){
								 loadStartGUI();
								 frame.setVisible(false);
								 }
								 });
		buttonPanel.add(button);
		
		button = new javax.swing.JButton("No");
		button.addActionListener(new java.awt.event.ActionListener(){
								 public void actionPerformed(java.awt.event.ActionEvent e){
								 System.exit(0);
								 }
								 });
		buttonPanel.add(button);
		
		panel.add(buttonPanel);
		
		javax.swing.JScrollPane pane = new javax.swing.JScrollPane(panel);
		frame.getContentPane().add(pane);
		frame.pack();
		frame.setVisible(true);
	}
	
	private static java.util.ArrayList<String> getFiles(){
		java.util.ArrayList<String> files = new java.util.ArrayList<String>();
		
		//start yesterday
		cal.add(Calendar.DATE, -1);
		
		//Every other day for a week
		for (int i = 0; i < 3; i++){
			files.add(dateToString(cal.getTime()));
			cal.add(Calendar.DATE, -2);
		}
		
		files.add(dateToString(cal.getTime()));
				
		//Every week for one week
		for (int i = 0; i < 1; i++){
			cal.add(Calendar.DATE, -7);
			files.add(dateToString(cal.getTime()));
		}
		
		//Once in the next two weeks
		cal.add(Calendar.DATE, -14);
		files.add(dateToString(cal.getTime()));
				
		//Once a month for 2 months
		for (int i = 0; i < 2; i++){
			cal.add(Calendar.DATE, -28);
			files.add(dateToString(cal.getTime()));
		}
		
		//Once every 2 months for 10 months
		for (int i = 0; i < 5; i++){
			cal.add(Calendar.DATE, -56);
			files.add(dateToString(cal.getTime()));
		}
					  
		/*Uncomment if you want to print out the names of the files that should be reviewed*/
		 for (String file: files){
			System.out.println(file);
		}
		
		/*Uncomment if you want to do the review "scripture style"
			 for (int i = 0; i < 7; i++){
			 cal.add(Calendar.DATE, -1);
			 files.add(dateToString(cal.getTime()));
			 }
			 
			 for (int i = 0; i < 4; i++){
			 cal.add(Calendar.DATE, -7);
			 files.add(dateToString(cal.getTime()));
			 }
			 
			 for (int i = 0; i < 12; i++){
			 cal.add(Calendar.DATE, -28);
			 files.add(dateToString(cal.getTime()));
			 }
		*/
			 
		return files;
	}
	
	private static String dateToString(java.util.Date dateToConvert){
		cal.setTime(dateToConvert);
		String toReturn = "";
		int month = cal.get(Calendar.MONTH) + 1;
		if (month < 10)
			toReturn += "0";
		toReturn += month;
		int day = cal.get(Calendar.DAY_OF_MONTH);
		if (day < 10)
			toReturn += "0";
		toReturn += day;
		return (toReturn + cal.get(Calendar.YEAR));
	}
	
	private static String convertFilenameToString(String toConvert){
		String toReturn = "";
		
		try{
			toConvert = toConvert.substring(0, toConvert.indexOf(EXTENSION));
		}catch (StringIndexOutOfBoundsException e){
			try{
				toConvert = toConvert.substring(0, toConvert.indexOf(EXTENSION_SHORT));
			}catch (StringIndexOutOfBoundsException ex){
				toConvert = toConvert.substring(0, toConvert.indexOf(EXTENSION_PDF));
			}
		}
		
		int month = Integer.parseInt(toConvert.substring(0,2)) - 1;
		toReturn += DateUtils.getAbbrMonthName(month) + " ";
		toReturn += Integer.parseInt(toConvert.substring(2,4)) + ", ";
		return toReturn + Integer.parseInt(toConvert.substring(4));
	}
}