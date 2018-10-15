import java.util.InputMismatchException;
import java.util.Scanner;

public class TUI {
    public static void main(String[] args) {
        String str1 = readLine("Type some text: ");
        System.out.println("Text read is: " + str1);
        int i = readPosInt("Type an integer: ");
        System.out.println("Integer read is: " + i);
        String str2 = readLine("Type some text again: ");
        System.out.println("Text read is: " + str2);
        
    }

    private static String readLine(String str) {
        System.out.print(str);
        Scanner input = new Scanner(System.in);

        return input.nextLine();
    }

    private static int readPosInt(String str) {
        int hold = -1;
        Scanner input = new Scanner(System.in);

        do {
            System.out.print(str);
            try {
                hold = input.nextInt();
                if (hold < 0) {
                    System.out.println("Positive integers only!");
                }
            } catch (InputMismatchException e) {
                System.out.println("You must type an integer!");
            }
            input.nextLine();


        } while (hold < 0);

        return hold;
    }
}
