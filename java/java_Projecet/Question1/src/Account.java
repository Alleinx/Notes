public abstract class Account implements IAccount {
    private String name;
    private int money;

    public Account(String name, int money) {
        this.name = name;
        this.money = money;
    }

    public String getName() {
        return this.name;
    }

    public int getMoney() {
        return this.money;
    }

    protected void setMoney(int money) {
        this.money = money;
    }

    public abstract void withdraw(int amount) ;

    public static void testAccount() {
//        Account t = new Account("Good", 100);
//        abstract class can not be initialized
    }

}
