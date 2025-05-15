import java.util.Scanner;
class Vowel{
public static void main(String[] args){
Scanner sc=new Scanner(System.in);
char ch=sc.next().charAt(0);
if((ch=='A') || (ch=='E')|| (ch=='I') || (ch=='O')| (ch=='U'))
{
System.out.println("Vowels");
}
else{
System.out.println("Consonants");
}
}
}
