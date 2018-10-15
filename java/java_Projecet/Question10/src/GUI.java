public class GUI {
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                Bank a = new Bank("UIC");

                ControllerSimple b = new ControllerSimple(a);
//                ControllerGetMoney m = new ControllerGetMoney(a);
                ControllerWithdraw w = new ControllerWithdraw(a);

                ViewSimple c = new ViewSimple(a, b);
//                ViewGetMoney d = new ViewGetMoney(a,m);
                ViewWithdraw wd = new ViewWithdraw(a, w);


                a.addListener(c);
//                a.addListener(d);
                a.addListener(wd);
                try {
                    StudentAccount s1 = new StudentAccount("Jerry", 5000);
                    a.addAccount(s1);
                } catch (NotEnoughMoneyException e) {
                    System.out.println(e.getMessage());
                }

                try {
                    StudentAccount s2 = new StudentAccount("TOM", 522000);
                    a.addAccount(s2);
                } catch (NotEnoughMoneyException e) {
                    System.out.println(e.getMessage());
                }

            }
        });
    }
}
