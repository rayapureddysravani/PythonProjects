import java.util.Scanner;
class Spy{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int sum=0;
int mul=1;
for(;n>0;n/=10)
{
sum+=n%10;
mul=mul*(n%10);
}
if(sum==mul)
{
System.out.println("Spy num");
}
else
{
System.out.println("Not Spy num");
}
}
}

