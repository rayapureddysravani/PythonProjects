import java.util.Scanner;
class Prime{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
boolean flag=true;
for(int i=2;i<=n/2;i++)
{
if(n%i==0)
{
flag=false;
System.out.println("Not Prime");
break;
}
}
if(flag==true)
System.out.println(" Prime");
}
}
