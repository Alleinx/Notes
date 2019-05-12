package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RecommendMain extends Controller {
    private JPanel mainPanel;
    private JComboBox comboBox1;
    private JTextArea textArea1;
    private JButton confirmButton;
    private JButton backButton;
    private JFrame frame;

    public RecommendMain(JFrame lastWindow) {
        frame = new JFrame("Recommend Recipe");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(400, 200);


        setUnitLabels(comboBox1);
        setWindowPosition(frame, lastWindow);
        frame.setVisible(true);

        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                recommend();
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }

    //#TODO : implement Recommend().
    private void recommend() {
        System.out.println(comboBox1.getSelectedItem());
        System.out.println(textArea1.getText());
        new RecommendDisplay(frame);
    }

}
