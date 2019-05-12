package GUI;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class IngredientDelete extends Controller{
    private JButton confirmButton;
    private JButton cancelButton;
    private JPanel secondPanel;
    private JPanel mainPanel;
    private JFrame frame;

    public IngredientDelete(JFrame lastWindow) {
        frame = new JFrame("Delete Ingredient");


        initTable();

        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        setWindowPosition(frame, lastWindow);

        cancelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });

        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                delete();
            }
        });
    }

    private void initTable() {
        Object[] columnNames = {"Type", "Company", "Shares", "Price", "Boolean"};
        Object[][] data = {
                {"Buy", "IBM", 1000, 80.5, false},
                {"Sell", "MicroSoft", 2000, 6.25, true},
                {"Sell", "Apple", 3000, 7.35, true},
                {"Buy", "Nortel", 4000, 20.0, false},
                {"Buy", "IBM", 1000, 80.5, false},
                {"Sell", "MicroSoft", 2000, 6.25, true},
                {"Sell", "Apple", 3000, 7.35, true},
                {"Buy", "Nortel", 4000, 20.0, false},
                {"Buy", "IBM", 1000, 80.5, false},
                {"Sell", "MicroSoft", 2000, 6.25, true},
                {"Sell", "Apple", 3000, 7.35, true},
                {"Buy", "Nortel", 4000, 20.0, false}
        };

        DefaultTableModel model = new DefaultTableModel(data, columnNames);

        JTable table = new JTable(model) {

            private static final long serialVersionUID = 1L;

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

        secondPanel.add(table.getTableHeader(), BorderLayout.NORTH);
        secondPanel.add(table, BorderLayout.CENTER);
    }

    //TODO: implement delete();

    private void delete() {
        System.out.println("DELETE");
    }

}
