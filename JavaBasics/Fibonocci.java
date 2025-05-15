import java.util.Scanner;
class Fibonocci{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int a=0;
int b=1;
int c;
for(int i=1;i<=n;i++)
{
System.out.println(a);
c=a+b;
a=b;
b=c;
}
}
}