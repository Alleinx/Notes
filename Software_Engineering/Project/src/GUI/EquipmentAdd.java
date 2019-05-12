package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class EquipmentAdd extends Controller {
    private JPanel mainPanel;
    private JButton addButton;
    private JButton backButton;
    private JTextField equipmentNameTextField;
    private JTextField maximumCapacityTextField;
    private JTextField unitTextField;
    private JFrame frame;

    public EquipmentAdd(JFrame lastWindow) {

        frame = new JFrame("Add Equipment");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        frame.pack();
        frame.setVisible(true);

        setWindowPosition(frame, lastWindow);

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addEquipment();
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }


    //#TODO:  add Equipment: If duplicate, display warning message, else add to DB and display message.
    private void addEquipment() {
        //If not duplicate: Print succeed message.
        JOptionPane.showMessageDialog(null,
                equipmentNameTextField.getText() +
                        "\n" +
                        maximumCapacityTextField.getText());
    }

}
