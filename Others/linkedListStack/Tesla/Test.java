
import java.util.*;

public class Test {

	public static void main(String[] args) {
		int [] input = {-4, 8, 6, -5, 6, -2, 1, 2, 3, -11};
		int j = 0, i;
		for(i = 0; i < input.length; i++)
		{
			if(input[i] <= 0)
			{
				int temp = input[i];
				input[i] = input[j];
				input[j] = temp;
				j++;
			}
			
		}
		System.out.println(Arrays.toString(input));
		
	}
	

}
