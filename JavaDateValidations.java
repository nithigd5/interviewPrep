import java.time.LocalDate;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.format.ResolverStyle;
import java.util.Locale;
import java.util.Scanner;

public class JavaDateValidations {

  static DateTimeFormatter dateFormatter =
      DateTimeFormatter.ofPattern("dd/MM/yyyy")
      .withResolverStyle(ResolverStyle.LENIENT);
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String date = scan.next();
    LocalDate parsedLocalDate 
        = validateAndParse(date, dateFormatter);
    scan.close();
    if(parsedLocalDate ==null){
      System.out.println("Invalid");
    }else{
      System.out.println("Valid");
    }
  }

  public static LocalDate validateAndParse(String dateStr,
                                    DateTimeFormatter dateFormatter) {

    LocalDate date = null;
    try {
      date = LocalDate.parse(dateStr, dateFormatter);
    } catch (DateTimeParseException e) {
      // e.printStackTrace();
    }
    return date;
  }
}