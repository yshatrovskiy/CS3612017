/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "keyword.jay";
	
	private static int counter = 1;

	public static void main(String args[]) {


		TokenStream ts = new TokenStream(file1);
		Token tok;
		int i = 0;
		while (!ts.isEndofFile()) {
			tok = ts.nextToken();
			i++;
//			if(tok.getType().equals("Other"))
//				System.out.println("Token " + i + " " + tok.toString());
			System.out.println("Token " + i + " " + tok.toString());
		}
	}
}
