import java.util.Scanner;
class GreatThree
{
public static void main(String[] args)
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter  first number: ");
int n1=sc.nextInt();
System.out.println("Enter  second number: ");
int n2=sc.nextInt();
System.out.println("Enter  third number: ");
int n3=sc.nextInt();
int res=(n1>n2)? (n1>n3? n1:n3): (n2>n3? n2:n3);
System.out.println("Greatest of Three numbers is "+res);
 res=(n1>n2)? n1:n2;
n3=(res>n3)? res:n3;
System.out.println("Greatest of Three numbers is "+n3);


}
}

 