package GUI;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RecommendDisplay extends Controller{
    private JPanel mainPanel;
    private JButton backButton;
    private JPanel thirdPanel;
    private JButton brewButton;
    private JFrame frame;

    public RecommendDisplay(JFrame lastWindow) {
        frame = new JFrame("Recommended Recipes");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setVisible(true);

        setWindowPosition(frame, lastWindow);

        initTable();

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });


        brewButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                brew();
                new NoteAdd(frame);
            }
        });
    }

    //#TODO : brew() + initTable();
    private void brew() {
        //Each time could only choose one recipe to brew.
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

        thirdPanel.add(table.getTableHeader(), BorderLayout.NORTH);
        thirdPanel.add(table, BorderLayout.CENTER);
    }

}
