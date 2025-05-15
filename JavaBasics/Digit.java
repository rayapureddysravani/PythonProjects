import java.util.Scanner;
class Digit{
public static void main(String[] args)
{
System.out.println("Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();

if(n>=0 && n<=9)
System.out.println("Single Digit");
else if(n>9 && n<99)
System.out.println("Double Digit");
else
System.out.println("Triple Digit");
}
}