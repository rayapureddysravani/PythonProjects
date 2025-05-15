import java.util.Scanner;
class Alpha{
public static void main(String[] args)
{
System.out.println(" Enter Character");
Scanner sc=new Scanner(System.in);
char ch=sc.next().charAt(0);
if((ch>='A' && ch<='Z') || (ch>='a' && ch<='Z'))
{
System.out.println("Alphabet");
}
else
{
System.out.println("Special Character");
}
}
}

