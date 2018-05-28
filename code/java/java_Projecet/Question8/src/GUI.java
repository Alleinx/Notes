public class GUI {
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                Bank a = new Bank("UIC");
                ControllerSimple b = new ControllerSimple(a);
                ViewSimple c = new ViewSimple(a, b);
                a.addListener(c);
                try {
                    StudentAccount s1 = new StudentAccount("jerry", 5000);
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
