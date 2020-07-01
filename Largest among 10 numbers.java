import java.util.Scanner;
class Main
{
    public static void main(String arg[])
    {
        Scanner p= new Scanner(System.in);
        int a[]=new int[10];
        for(int i=0;i<a.length;i++)
        {
            a[i]=p.nextInt();
        }
        int min=a[0];
        for(int i=1;i<a.length;i++)
        {
            if(a[i]<min)
            {
                min=a[i];
            }
        }
        System.out.println(min);
    }
}
