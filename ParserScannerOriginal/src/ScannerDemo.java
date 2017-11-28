/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "prog2.jay";
	
	private static int counter = 1;

	public static void main(String args[]) {


		TokenStream ts = new TokenStream(file1);
		Token tok;
		int i = 0;
		while (!ts.isEndofFile()) {
			tok = ts.nextToken();
			i++;
			System.out.println("Token " + i + " " + tok.toString());
		}
	}
}
