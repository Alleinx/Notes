public class CreditAccount extends Account {
    public CreditAccount(String name, int money) {
        super(name,money);

    }

    @Override
    /* allowed to have a negative amount of money */
    public void withdraw(int amount) {
        setMoney(getMoney() - amount);
    }

    public static void testCreditAccount() {
        CreditAccount a = new CreditAccount("Gorge", 1000);

        System.out.println(a.getMoney() == 1000);
        System.out.println("Gorge".equals(a.getName()));
        a.setMoney(2000);
        System.out.println(a.getMoney() == 2000);
        a.withdraw(1000);
        System.out.println(a.getMoney() == 1000);
    }
}
