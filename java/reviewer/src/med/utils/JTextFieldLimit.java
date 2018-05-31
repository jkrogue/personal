//
//  JTextFieldLimit.java
//  
//
//  Created by Marissa & Justin Krogue on 9/27/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

package med.utils;

public class JTextFieldLimit extends javax.swing.text.PlainDocument{
	private boolean toUpperCase = false;
	private int limit;
	
	public JTextFieldLimit (int limit){
		super();
		this.limit = limit;
	}
	
	public void insertString(int offset, String str, javax.swing.text.AttributeSet attr) 
			throws javax.swing.text.BadLocationException{
		if (str == null)
			return;
				
		if (getLength() + str.length() <= limit){
			if (toUpperCase)
				str = str.toUpperCase();
			for (int i = 0; i < str.length(); i++){
				if (str.charAt(i) < '0' || str.charAt(i) > '9')
					return;
			}
			super.insertString(offset, str, attr);
		}
	}
}
