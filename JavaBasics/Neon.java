import java.util.Scanner;
class Neon{
public static void main(String[] args)
{
System.out.println(" Enter Number");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int sq=n*n;
int sum=0;
for(;sq>0;sq/=10)
{
sum=sum+(sq%10);
}
if(n==sum)
System.out.println("Neon");
else
System.out.println("Not Neon");

}
}



