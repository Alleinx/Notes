public class StudentAccount extends Account{

    public StudentAccount(String name, int amount) throws NotEnoughMoneyException {
        super(name, amount);
        if (amount < 0) {
            throw new NotEnoughMoneyException("Cannot create student account with negative amount of money.");
        }
    }

    @Override
    public void withdraw(int amount) throws NotEnoughMoneyException{
        if (this.getMoney() - amount < 0) {
            throw new NotEnoughMoneyException("Cannot withdraw "              + 
            									 amount                          +
                                              " Yuan from the account, only " +
                                              this.getMoney()                 + 
                                              " is available.");
        } else {
            this.setMoney(this.getMoney() - amount);
        }
    }

    public static void testStudentAccount() {
        //valid StudentAccount
        try {
            StudentAccount a = new StudentAccount("Jerry", 1000);
            System.out.println(a.getMoney() == 1000);
            System.out.println("Jerry".equals(a.getName()));

            // valid amount for withdraw
            try {
                a.withdraw(500);
                System.out.println(a.getMoney() == 500);
            } catch (NotEnoughMoneyException e) {
                System.out.println(e.getMessage());
            }

            //invalid amount for withdraw
            try {
                a.withdraw(600);
            } catch (NotEnoughMoneyException e) {
                System.out.println(e.getMessage());
            }

        } catch (NotEnoughMoneyException e) {
            System.out.println(e.getMessage());
        }
        
        // invalid StudentAccount
        try {
            StudentAccount b = new StudentAccount("Tom",-10);
        } catch (NotEnoughMoneyException e) {
            System.out.println(e.getMessage());
        }
    }
}
