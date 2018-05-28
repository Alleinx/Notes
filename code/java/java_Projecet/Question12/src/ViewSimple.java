import javax.swing.*;
import java.awt.*;

public class ViewSimple extends View  {
     private ControllerSimple c;
     private JLabel label;

     public ViewSimple(Bank m, ControllerSimple c) {
         super(m);

         this.setSize(400, 300);
         this.setTitle("ViewSimple");
         this.setLayout(new FlowLayout());
         this.c = c;

         label = new JLabel();
         label.setText("Total money: " + this.m.totalMoney());

         this.add(label);
         this.setVisible(true);
     }

    @Override
    public void update() {
        this.label.setText("Total money:" + this.m.totalMoney());
    }
}
