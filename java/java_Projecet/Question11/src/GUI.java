public class GUI {
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                Bank a = new Bank("UIC");

                ControllerSimple b = new ControllerSimple(a);
                ControllerGetMoney m = new ControllerGetMoney(a);
                ControllerWithdraw w = new ControllerWithdraw(a);
                ControllerCreate c = new ControllerCreate(a);

                ViewSimple cs = new ViewSimple(a, b);
                ViewGetMoney d = new ViewGetMoney(a,m);
                ViewWithdraw wd = new ViewWithdraw(a, w);
                ViewCreate cr = new ViewCreate(a, c);


                a.addListener(cs);
                a.addListener(cr);
                a.addListener(wd);
                a.addListener(cr);

            }
        });
    }
}
