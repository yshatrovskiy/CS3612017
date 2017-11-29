public class ParserDemo {
	
	private static String file1 = "prog2.jay";
	private static String file3 = "boolean.jay";
	public static void main(String[] args) {
		TokenStream tStream = new TokenStream(file1);
		System.out.println("test1");
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		System.out.println("test2");
		Program p = cSyntax.program();
		System.out.println(p.display());
		System.out.println("test3");
	}

}
