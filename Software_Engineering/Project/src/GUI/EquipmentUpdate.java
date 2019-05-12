package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class EquipmentUpdate extends Controller{
    private JButton backButton;
    private JButton confirmButton;
    private JTextField equipmentNameTextField;
    private JTextField maximumCapacityTextField;
    private JPanel mainPanel;
    private JFrame frame;

    private final int YES = 0;


    public EquipmentUpdate(JFrame lastWindow) {
        frame = new JFrame("Update Equipment");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        setWindowPosition(frame, lastWindow);

        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                update();
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }

    //TODO: implement update().
    private void update() {
        int userChoice = JOptionPane.showConfirmDialog(null,
                "Do you want to save the changes?",
                "Confirm",
                JOptionPane.YES_NO_OPTION);
        if (userChoice == YES) {
            //update here
        }
        //else: Do nothing.
    }

}
