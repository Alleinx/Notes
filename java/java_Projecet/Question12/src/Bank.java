import java.util.ArrayList;

public class Bank {
    private String name;
    private ArrayList<IAccount> accounts;
    private ArrayList<ModelListener> model_listener;
    private ArrayList<Integer> history;


    public Bank(String name) {
        this.name = name;
        accounts = new ArrayList<IAccount>();
        model_listener = new ArrayList<ModelListener>();
        history = new ArrayList<Integer>();
        history.add(0);
    }

    private void notifyListeners() {
        for (ModelListener t : model_listener) {
            t.update();
        }
    }

    public void addListener(ModelListener t) {
        this.model_listener.add(t);
    }

    public void addAccount(IAccount account) {
        this.accounts.add(account);
        this.history.add(this.totalMoney());
        this.notifyListeners();
    }

    public int totalMoney() {
        int sum = 0;
        for(IAccount e : this.accounts) {
            sum += e.getMoney();
        }
        return sum;
    }

    public int getMoney(String name) throws UnknownCustomerException{
        boolean check = true; /* check if there exists a IAccount with name name */

        for(IAccount e : this.accounts) {
            if (e.getName().equals(name)) {
                return e.getMoney();
            }
        }

        if (check == true) {
            throw new UnknownCustomerException("Customer " + name + " unknown");
        }
        return 0;
    }

    public ArrayList<Integer> getHistory() {
        return history;
    }

    public void withdraw(String name, int amount) throws UnknownCustomerException, NotEnoughMoneyException {
        boolean check = true; /* check if there exists a IAccount with name name */
        IAccount temp = null; /* store IAccount with name name */

        for(IAccount e : this.accounts) {
            if (e.getName().equals(name)) {
                check = false;
                temp = e;
                break;
            }
        }
        
        if (check == true) {
            throw new UnknownCustomerException("Customer " + name + " unknown");
        } else {
            temp.withdraw(amount);
            this.history.add(this.totalMoney());
            this.notifyListeners();
        }
    }


    public static void testBank() {
        Bank a = new Bank("Center");
        System.out.println("Center bank now has 0 dollar " + (a.totalMoney() == 0));

        try {
            a.addAccount(new StudentAccount("Jerry", 1000));
            a.addAccount(new StudentAccount("Tom", 1000));
        } catch (NotEnoughMoneyException e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Center bank now has 2000 dollars " + (a.totalMoney() == 2000));

        /* test UnknownCustomerException */
        try {
            a.getMoney("Charlotte");
        } catch (UnknownCustomerException e) {
            System.out.println(e.getMessage());
        }

        try {
            System.out.println(a.getMoney("Jerry") == 1000);
        } catch (UnknownCustomerException e) {
            System.out.println(e.getMessage());
        }

        /* test withdraw with UnknownCustomer */
        try {
            a.withdraw("Charlotte",500);
        } catch (UnknownCustomerException e) {
            System.out.println(e.getMessage());
        } catch (NotEnoughMoneyException e) {
            System.out.println(e.getMessage());
        }
        /* test withdraw with NotEnoughMoney */
        try {
            a.withdraw("Jerry", 800);
            System.out.println("Jerry now has 200 dollars " + (a.getMoney("Jerry") == 200));
            a.withdraw("Jerry",2000);
        } catch (UnknownCustomerException e) {
            System.out.println(e.getMessage());
        } catch (NotEnoughMoneyException e) {
            System.out.println(e.getMessage());
        }
    }


}
