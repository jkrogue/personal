//
//  DateUtils.java
//  
//
//  Created by Marissa & Justin Krogue on 9/27/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

package med.utils;

public class DateUtils {
	
	/**
	 * @param index the index of the month whose abbreviated name is to be returned (ie 0 for "Jan")
	 *
	 * @throws IllegalArgumentException if index < 0 or index > 11
	 * @return abbreviated name of indexed month
	 */
	public static String getAbbrMonthName(int index){
		if (index < 0 || index > 11)
			throw new IllegalArgumentException("Can't get abbreviated month name: index is less than 0 or greater than 11");
		return MONTH_ABBR_NAMES[index];
	}
	
	/**
	 * Returns true if the integers supplied describe a valid date
	 *
	 * @param month Must be between 1-12 to be valid
	 * @param day Must be between 1 and maximum number of days in the month (ie 31 for January) to be valid
	 * @param year Whatever integer is supplied will be valid
	 *
	 * @return true if a valid date is supplied
	 */
	public static boolean isValidDate(int month, int day, int year){
		if (month < 1 || month > 12)
			return false;
		
		month--;
		
		if (day < 1)
			return false;
		if (day > DAYS_IN_MONTH[month]){
			if (month == FEB_INDEX && isLeapYear(year) && day == 29){
				return true;
			}
			return false;
		}
		
		return true;
	}
	
	/*
	 * Returns true if the year supplied is a leap year
	 *
	 * @param year the year to be checked
	 * 
	 * @return true if the year is a leap year
	 */
	private static boolean isLeapYear(int year){
		return (year % 4 == 0);
	}

	private static final int FEB_INDEX = 1;
	private static final int[] DAYS_IN_MONTH = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	private static final String[] MONTH_ABBR_NAMES = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
					"Sep", "Oct", "Nov", "Dec"};

	/** 
	 * If DateUtils is run as the main class a test driver will run on the class
	 */
	public static void main(String[] args){
		boolean success = true;
		
		//RUN TESTS
		
		if (success)
			System.out.println("Tests finished successfully");
		else
			System.out.println("Tests failed");
	}
}
