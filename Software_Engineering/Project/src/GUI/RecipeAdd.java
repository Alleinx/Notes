package GUI;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RecipeAdd extends Controller{
    private JPanel mainPanel;
    private JButton saveButton;
    private JButton backButton;
    private JTextField recipeNameTextField;
    private JPanel thirdPanel;
    private JButton addButton;
    private JButton deleteButton;
    private JFrame frame;
    private JTable table;
    private DefaultTableModel model;


    public RecipeAdd(JFrame lastWindow) {

        frame = new JFrame("Recipe");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        initTable();

        frame.setSize(400, 400);
        frame.setVisible(true);
        setWindowPosition(frame, lastWindow);

        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addIngredient();
                System.out.println(model.getDataVector());
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                model.addRow(new Object[]{"Buy", "IBM", 1000, 80.5});
            }
        });

        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                removeSelectedRows();
            }
        });
    }

    //TODO: implement initTable();

    private void initTable() {
        Object[] columnNames = {"Type", "Company", "Shares", "Price"};
        Object[][] data = {
                {"Buy", "IBM", 1000, 80.5},
                {"Sell", "MicroSoft", 2000, 6.25},
                {"Sell", "Apple", 3000, 7.35}
        };

        model = new DefaultTableModel(data, columnNames);

        table = new JTable(model) {

            @Override
            public Class getColumnClass(int column) {
                switch (column) {
                    case 0:
                        return String.class;
                    case 1:
                        return String.class;
                    case 2:
                        return Integer.class;
                    case 3:
                        return Double.class;
                    default:
                        return Boolean.class;
                }
            }
        };

        table.setPreferredScrollableViewportSize(table.getPreferredSize());

        thirdPanel.add(table.getTableHeader(), BorderLayout.NORTH);
        thirdPanel.add(table, BorderLayout.CENTER);
    }

    //TODO: save data into DB.
    private void removeSelectedRows(){
        DefaultTableModel model = (DefaultTableModel) this.table.getModel();
        int[] rows = table.getSelectedRows();

        for (int i = 0; i < rows.length; i++) {
            model.removeRow(rows[i] - i);
        }
    }

    //#TODO: implement addIngredient(): If duplicate, display warning message, else add to DB and display message.
    private void addIngredient() {
        //If not duplicate: Print succeed message.
        JOptionPane.showMessageDialog(null,
                recipeNameTextField.getText());
    }

}
