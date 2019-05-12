package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import javax.swing.JOptionPane;
import java.awt.event.ActionListener;

public class IngredientAdd extends Controller{
    private JPanel mainPanel;
    private JButton addButton;
    private JButton backButton;
    private JTextField ingredientNameTextField;
    private JTextField amountTextField;
    private JComboBox comboBox1;
    private JFrame frame;

    public IngredientAdd(JFrame lastWindow) {

        frame = new JFrame("Add Ingredients");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        frame.pack();
        frame.setVisible(true);

        setUnitLabels(comboBox1);

        setWindowPosition(frame, lastWindow);

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addIngredient();
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }


    //#TODO: implement add Ingredient: If duplicate, display warning message, else add to DB and display message.
    private void addIngredient() {
        //If not duplicate: Print succeed message.
        JOptionPane.showMessageDialog(null,
                ingredientNameTextField.getText() +
                        "\n" +
                        comboBox1.getSelectedItem() +
                        "\n" +
                        amountTextField.getText());
    }

}
