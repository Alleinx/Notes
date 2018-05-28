import java.util.InputMismatchException;
import java.util.Scanner;

public class TUI {
    public static void main(String[] args) {
        Bank t = new Bank("UIC BANK");
        String user_name_msg = "Enter the name of the customer: ";
        String user_init_amount = "Enter the initial amount of money: ";
        String amount_withdraw = "Enter the amount of money to withdraw: ";
        String amount_deposit = "Enter the amount of money to deposit: ";
        String msg = "Type an action (" +
                     "total:1 "         +
                     "add:2 "           +
                     "list:3 "          +
                     "withdraw:4 "      +
                     "deposit:5 "       +
                     "quit:6) :";
        
        int menu; /* choice for menu */
        String user_name; /* store user name */
        int amount; /* store user initial amount */

        while (true) {
            menu = readPosInt(msg);

            switch (menu) {
                /*  printing the total amount of money stored in the bank */
                case 1:
                    System.out.println("Total amount of money in the bank:  " + t.totalMoney());
                    break;

                /* adding a new customer account to the bank */
                case 2:
                    String user_msg = "Type the account type (credit:1 student:2):";

                    int user_type = readPosInt(user_msg);
                    switch (user_type) {
                        case 1:
                            /* get user input */
                            user_name = readLine(user_name_msg);
                            amount = readPosInt(user_init_amount);

                            CreditAccount a = new CreditAccount(user_name, amount);
                            t.addAccount(a);
                            System.out.println("Credit account for " +
                                                user_name            +
                                                " with "             +
                                                amount               +
                                                " yuan has been added");
                            break;

                        case 2:
                            /* get user input */
                            user_name = readLine(user_name_msg);
                            amount = readPosInt(user_init_amount);

                            try {
                                StudentAccount b = new StudentAccount(user_name, amount);
                                t.addAccount(b);
                                System.out.println("Student account for " +
                                        user_name +
                                        " with " +
                                        amount +
                                        " yuan has been added");
                            } catch (NotEnoughMoneyException e) {
                                System.out.println("BUG! This must never happen!");
                                System.exit(1);
                            }
                            break;

                        default:
                            System.out.println("Unknown type of account!");
                    }
                    break;

                /* listing the amount of money in the account of a given customer. */
                case 3:
                    user_name = readLine(user_name_msg);

                    try {
                        System.out.println(user_name             +
                                           " has "               +
                                           t.getMoney(user_name) +
                                           " yuan in the bank.");
                    } catch (UnknownCustomerException e) {
                        System.out.println(e.getMessage());
                    }
                    break;

                /* withdrawing money from the account of a given customer. */
                case 4:
                    user_name = readLine(user_name_msg);
                    amount = readPosInt(amount_withdraw);

                    try {
                        t.withdraw(user_name, amount);
                    } catch (UnknownCustomerException e) {
                        System.out.println(e.getMessage());
                    } catch (NotEnoughMoneyException e) {
                        System.out.println(e.getMessage());
                    }
                    break;

                /* depositing money into the account of a given customer. */
                case 5:
                    user_name = readLine(user_name_msg);
                    amount = readPosInt(amount_deposit);

                    try {
                        t.withdraw(user_name, -amount);
                    } catch (UnknownCustomerException e) {
                        System.out.println(e.getMessage());
                    } catch (NotEnoughMoneyException e) {
                        System.out.println("BUG! This must never happen!");
                        System.exit(1);
                    }
                    break;

                /*  quitting the program. */
                case 6:
                    System.out.println("Goodbye!");
                    System.exit(0);
                    break;

                default:
                    System.out.println("Unknown action!");
            }
        }

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
