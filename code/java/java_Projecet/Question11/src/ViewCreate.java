import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ViewCreate extends View {
    private ControllerCreate c;
    private JTextField t1;
    private JTextField t2;
    private JComboBox<String> cb;

    public ViewCreate(Bank m, ControllerCreate c) {
        super(m);
        this.c = c;

        t1 = new JTextField("name");
        t2 = new JTextField("amount");
        cb = new JComboBox<String>();
        JButton b = new JButton("Create");

        this.setLayout(new GridLayout(2, 2, 20, 20));
        this.setSize(400, 300);
        this.setTitle("Create");
        this.add(t1);
        this.add(t2);
        this.add(cb);
        this.add(b);
        cb.addItem("credit account");
        cb.addItem("student account");
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = t1.getText();
                String amount = t2.getText();
                int choice = cb.getSelectedIndex();
                JOptionPane.showMessageDialog(null, c.create(name, amount, choice ));
            }
        });

        this.setVisible(true);

    }

    @Override
    public void update() {

    }
}
