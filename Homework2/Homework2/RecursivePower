public class RecursivePower {
	
	public static int recPow(int n) { 
	    if(n >= 0 && n < 31){
	        if(n == 0)
	            return 1;
	        else{
	            return (2 * recPow(n-1));
	        }
	    }else{
	        throw new ArithmeticException("Input must be between 0 and 30");
	    }
	}

	  public static void main(String [] args){
	    System.out.println(recPow(0));
	    System.out.println(recPow(1));
	    System.out.println(recPow(2));
	    System.out.println(recPow(3));
	    System.out.println(recPow(10));
	    System.out.println(recPow(30));
	    System.out.println(recPow(31));
	  }
}