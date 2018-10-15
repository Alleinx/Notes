import javax.swing.*;
import java.awt.*;

public class ViewSimple extends JFrame implements ModelListener {
     private Bank m;
     private ControllerSimple c;
     private JLabel label;

     public ViewSimple(Bank m, ControllerSimple c) {
         this.setSize(400, 300);
         this.setTitle("ViewSimple");
         this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         this.setLayout(new FlowLayout());
         this.m = m;
         this.c = c;

         label = new JLabel();
         label.setText("Total money: " + this.m.totalMoney());

         this.add(label);
         this.setVisible(true);
     }

    @Override
    public void update() {
        this.label.setText("Total money: " + this.m.totalMoney());
    }
}
