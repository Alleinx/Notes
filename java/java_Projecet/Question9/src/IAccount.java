public interface IAccount {
    String getName();
    int getMoney();
    void withdraw(int amount) throws NotEnoughMoneyException;
}
