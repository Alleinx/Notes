import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ViewGetMoney extends View {
    private ControllerGetMoney c;
    private JTextField t;

    public ViewGetMoney(Bank m, ControllerGetMoney c) {
        super(m);

        this.c = c;

        this.setSize(400, 300);
        this.setTitle("ViewGetMoney");
        this.setLayout(new GridLayout());

        JButton b = new JButton("Query");
        t = new JTextField();

        this.add(b);
        this.add(t);

        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = t.getText();
                String amount_message = c.getMoney(name);
                JOptionPane.showMessageDialog(null, amount_message);
            }
        });
        this.setVisible(true);
    }

    @Override
    public void update() {

    }
}
