package GUI;

import javax.swing.*;
import javax.swing.event.CellEditorListener;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellEditor;
import javax.swing.table.TableCellRenderer;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.EventObject;

public class RecipeMain extends Controller{
    private JButton addButton;
    private JButton deleteButton;
    private JPanel mainPanel;
    private JPanel secondPanel;
    private JButton backButton;
    private JFrame frame;

    public RecipeMain(JFrame lastWindow) {
        frame = new JFrame("Recipe List");

        initTable();

        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);

        setWindowPosition(frame, lastWindow);

        //create Add ingredient window;
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new RecipeAdd(frame);
            }
        });


        //create Delete ingredient window;
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new RecipeDelete(frame);
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }

    private void initTable() {
        Object[] columnNames = {"Type", "Company", "Shares", "Update"};
        Object[][] data = {
                {"Buy", "IBM", 1000, 80.5},
                {"Sell", "MicroSoft", 2000, 6.25},
                {"Sell", "Apple", 3000, 7.35},
                {"Buy", "Nortel", 4000, 20.0},
                {"Buy", "IBM", 1000, 80.5},
                {"Sell", "MicroSoft", 2000, 6.25},
                {"Sell", "Apple", 3000, 7.35},
                {"Buy", "Nortel", 4000, 20.0},
                {"Buy", "IBM", 1000, 80.5},
                {"Sell", "MicroSoft", 2000, 6.25},
                {"Sell", "Apple", 3000, 7.35},
                {"Buy", "Nortel", 4000, 20.0}
        };

        DefaultTableModel model = new DefaultTableModel(data, columnNames);

        JTable table = new JTable(model) {
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

        table.getColumn("Update").setCellRenderer(new TableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
                return new JButton("Update");
            }
        });

        table.getColumn("Update").setCellEditor(new TableCellEditor() {
            @Override
            public Component getTableCellEditorComponent(JTable table, Object value, boolean isSelected, int row, int column) {
                new RecipeAdd(frame);
                return null;
            }

            @Override
            public Object getCellEditorValue() {
                return null;
            }

            @Override
            public boolean isCellEditable(EventObject anEvent) {
                return true;
            }

            @Override
            public boolean shouldSelectCell(EventObject anEvent) {
                return false;
            }

            @Override
            public boolean stopCellEditing() {
                return false;
            }

            @Override
            public void cancelCellEditing() {

            }

            @Override
            public void addCellEditorListener(CellEditorListener l) {

            }

            @Override
            public void removeCellEditorListener(CellEditorListener l) {

            }
        });

        secondPanel.add(table.getTableHeader(), BorderLayout.NORTH);
        secondPanel.add(table, BorderLayout.CENTER);
    }
}
