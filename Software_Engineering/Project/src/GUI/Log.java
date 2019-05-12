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

public class Log extends Controller{
    private JPanel secondPanel;
    private JPanel mainPanel;
    private JButton backButton;
    private JFrame frame;

    public Log(JFrame lastWindow) {
        frame = new JFrame("Brew History");

        initTable();

        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        setWindowPosition(frame, lastWindow);

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });

    }

    private void initTable() {
        Object[] columnNames = {"Type", "Company", "Shares", "Price", "Note"};

        Object[][] data = {
                {"Buy", "IBM", 1000, 80.5, ""},
                {"Sell", "MicroSoft", 2000, 6.25, ""}
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
                        return String.class;
                }
            }
        };

        //implement button in table cell, don't modify.
        table.getColumn("Note").setCellRenderer(new TableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
                return new JButton("View Note");
            }
        });

        table.getColumn("Note").setCellEditor(new TableCellEditor() {
            @Override
            public Component getTableCellEditorComponent(JTable table, Object value, boolean isSelected, int row, int column) {
                new NoteMain(frame, "Some Note");
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

        table.setPreferredScrollableViewportSize(table.getPreferredSize());

        secondPanel.add(table.getTableHeader(), BorderLayout.NORTH);
        secondPanel.add(table, BorderLayout.CENTER);
    }

    private void delete() {
        System.out.println("DELETE");
    }

}
