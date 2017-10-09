
public class MergeFunctions {

	private static int[] finalArray;
	private static int[] tempArray;
	private static int length;

	public static void main(String a[]){
		
        //regular sort 
		//	        int[] inputArr = {45,23,11,89,77,98,4,28,65,43};
		//	        int[] inputArr2 = {45,23,11,89,77,98,4,28,65,43};
		//	        sort(inputArr, inputArr2);
		
        //empty sort
		//	        int[] inputArr3 = {0};
		//	        int[] inputArr4 = {};
		//	        sort(inputArr3, inputArr4);

		//negative numbers sort
		//	        int[] inputArr5 = {-1,-20,50,6,10};
		//	        int[] inputArr6 = {0,3,5};
		//	        sort(inputArr5, inputArr6);
		//	        for(int i:finalArray){
		//	            System.out.print(i);
		//	            System.out.print(" ");
		//	        }

		//max size test
		int[] inputArr7 = new int [99995];
		int[] inputArr8 = {0,3,5};

		sort(inputArr7, inputArr8);
		for(int i:finalArray){
			System.out.print(i);
			System.out.print(" ");
		}
	}

	public static void sort(int inputArr[], int inputArr2[]) {

		if(inputArr.length==0 || inputArr2.length == 0){
			throw new ArithmeticException("Cannot Have an empty Array");
		}
		else if((inputArr.length + inputArr2.length) > 99999){
			throw new ArithmeticException("Array Too Large");
		}else{


			int combinedLength  = inputArr.length + inputArr2.length;
			finalArray = new int [combinedLength];

			int j = 0;
			for(int i = 0;i <= inputArr.length-1; i++, j++){
				finalArray[j]=inputArr[i];
			}
			for(int i = 0;i <= inputArr2.length-1; i++, j++){
				finalArray[j]=inputArr2[i];
			}

			length = finalArray.length;
			tempArray = new int[length];
			split(0, length - 1);
		}
	}

	private static void split(int lowerIndex, int higherIndex) {

		if (lowerIndex < higherIndex) {
			int middle = lowerIndex + (higherIndex - lowerIndex) / 2;
			split(lowerIndex, middle);
			split(middle + 1, higherIndex);
			mergeParts(lowerIndex, middle, higherIndex);
		}
	}

	private static void mergeParts(int lowerIndex, int middle, int higherIndex) {

		for (int i = lowerIndex; i <= higherIndex; i++) {
			tempArray[i] = finalArray[i];
		}
		int i = lowerIndex;
		int j = middle + 1;
		int k = lowerIndex;
		while (i <= middle && j <= higherIndex) {
			if (tempArray[i] <= tempArray[j]) {
				finalArray[k] = tempArray[i];
				i++;
			} else {
				finalArray[k] = tempArray[j];
				j++;
			}
			k++;
		}
		while (i <= middle) {
			finalArray[k] = tempArray[i];
			k++;
			i++;
		}

	}
}
