/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "prog2.jay";
	private static String file2 = "separator.jay";
	private static String file3 = "boolean.jay";
	private static String file4 = "identifier.jay";
	private static String file5 = "integer.jay";
	private static String file6 = "keyword.jay";
	private static String file7 = "literal.jay";
	private static String file8 = "operator.jay";
	private static String file9 = "separator.jay";
	private static int counter = 1;

	public static void main(String args[]) {


		TokenStream ts = new TokenStream(file3);


		
		Token tok;

		while (!ts.isEndofFile()) {
			tok = ts.nextToken();
			System.out.println(tok.toString());
		}
	}
}
