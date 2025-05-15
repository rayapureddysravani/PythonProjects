import java.util.Scanner;
class Table{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
System.out.println(" Enter last Number");
int l=sc.nextInt();
for(int i=1;i<=l;i++)
{
System.out.println(n +"*"+ i+ "=" +n*i);
}
}
}

