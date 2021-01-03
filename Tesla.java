import java.util.*;

public class Tesla {
    public static int Solution(String T[], String R[])
    {
        int letterCount = 0;
        for(int i = 0; i < T[0].length(); i++)
        {
            if(!(T[0].charAt(i) > 47 && T[0].charAt(i) < 58))
            {
                letterCount++;
            }
            else
            {
                break;
            }
        }
        for(int i = 0; i < T.length; i++)
        {
            T[i] = T[i].substring(letterCount);
        }
        boolean hasResult = true;
        int validCount = 0;
        int okCount = 0;
        int numberCount = 0;
        int group = 1;
        while(hasResult){
            for(int i = 0; i < T.length; i++)
            {
                String integer = "";
                for(int j = 0; j < T[i].length(); j++)
                {
                    if(T[i].charAt(j) > 47 && T[i].charAt(j) < 58)
                    {
                        integer += T[i].charAt(j);
                    }
                }
                int number = Integer.parseInt(integer);
                if(number == group && R[i].equals("OK"))
                {
                    System.out.println("Gets to 1");
                    okCount++;
                    numberCount++;
                }
                else if(number == group)
                {
                    numberCount++;
                }
            }
            System.out.println("Group " + group);
            System.out.println(okCount);
            System.out.println(numberCount);
            if(numberCount > 0 && numberCount == okCount)
            {
                validCount++;
                group++;
                okCount = 0;
                numberCount = 0;
            }
            else if(numberCount == 0)
            {
                hasResult = false;
            }
            else
            {
                group++;
                okCount = 0;
                numberCount = 0;
            }
        }

        return validCount * 100 / (group - 1);
    }
    public static void main(String[] args)
    {
        String T1[] = {"tesla1aaa", "tesla2", "tesla1b", "tesla1c", "tesla3"};
        String R1[] = {"Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded"};
        String T2[] = {"codility1", "codility3", "codility2", "codility4b", "codility4a"};
        String R2[] = {"Wrong answer", "OK", "OK", "Runtime error", "OK"};
        
        System.out.println(Solution(T1, R1));
        System.out.println(Solution(T2, R2));
    }
}
