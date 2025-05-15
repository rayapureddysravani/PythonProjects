import java.util.Scanner;
class GreatTwoNum
{
public static void main(String[] args)
{
Scanner s=new Scanner(System.in);
System.out.println("Enter a number");
int n1=s.nextInt();
System.out.println("Enter a number");
int n2=s.nextInt();
int res=(n1>n2)? n1:n2;
System.out.println("The greatest number is "+ res);
}
}


