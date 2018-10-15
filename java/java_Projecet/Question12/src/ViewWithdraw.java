import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ViewWithdraw extends View{
    private ControllerWithdraw c;
    private JTextField t1;
    private JTextField t2;

    public ViewWithdraw(Bank m, ControllerWithdraw c) {
        super(m);
        this.c = c;

        this.setSize(400, 300);
        this.setTitle("Withdraw");
        this.setLayout(new GridLayout());

        JButton b = new JButton("Withdraw");
        t1 = new JTextField("name of customer");
        t2 = new JTextField("amount of money");

        this.add(b);
        this.add(t1);
        this.add(t2);

        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = t1.getText();
                String amount = t2.getText();
                JOptionPane.showMessageDialog(null, c.withdraw(name, amount));
            }
        });
        this.setVisible(true);

    }

    @Override
    public void update() {

    }
}
