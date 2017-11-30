public class ParserDemo {
	
	private static String file1 = "prog2.jay";
	private static String file3 = "boolean.jay";
	public static void main(String[] args) {
		TokenStream tStream = new TokenStream(file1);
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		Program p = cSyntax.program();
		System.out.println(p.display());
	}

}
