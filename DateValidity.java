import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class DateValidity {
    public static boolean isLeapYear(int year) {
        if (year % 400 == 0)
            return true;
        else if (year % 100 == 0)
            return false;
        else if (year % 4 == 0)
            return true;
        else
            return false;
    }

    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String date = scan.next();
        scan.close();
        Pattern pattern = Pattern.compile("([0-9]{1,2})\\/([0-9]{1,2})\\/([0-9]{4})");
        Matcher matcher = pattern.matcher(date);
        boolean valid = false;
        if (matcher.find()) {
            if (matcher.groupCount() == 3) {
                int day = Integer.parseInt(matcher.group(1));
                int month = Integer.parseInt(matcher.group(2));
                int year = Integer.parseInt(matcher.group(3));

                if (day > 0 && day <= 31 && month >= 1 && month <= 12 && year > 1900 & year < 3000) {
                    if (month == 2) {
                        if (!isLeapYear(year)) {
                            if (day < 29)
                                valid = true;
                        } else if (day <= 29)
                            valid = true;
                    } else if ((month < 8) && ((month % 2 == 0 && day <= 30) || (month % 2 == 1))) {
                        valid = true;
                    } else if (month >= 8 && ((month % 2 == 1 && day <= 30) || (month % 2 == 0)))
                        valid = true;
                }
            }
        }
        if (valid)
            System.out.print("Valid");
        else
            System.out.print("Invalid");
    }
}
