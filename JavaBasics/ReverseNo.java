import java.util.Scanner;
class ReverseNo{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int rev=0;
for(;n>0;n/=10)
{
rev=(rev*10)+n%10;
}
System.out.println(rev);
}
}
