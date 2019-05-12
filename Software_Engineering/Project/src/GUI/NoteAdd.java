package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NoteAdd extends Controller {
    private JTextArea textArea1;
    private JPanel mainPanel;
    private JButton saveButton;
    private JButton closeButton;
    private JPanel secondPanel;
    private JFrame frame;

    public NoteAdd(JFrame lastWindow) {

        frame = new JFrame("Add Note");
        frame.setContentPane(this.mainPanel);
        textArea1 = new JTextArea();
        JScrollPane sp = new JScrollPane(textArea1);
        secondPanel.add(sp);

        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(400, 250);
        frame.setVisible(true);

        setWindowPosition(frame, lastWindow);
        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                save();
            }
        });

        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });
    }

    //TODO: implement save();
    private void save() {
        System.out.println(textArea1.getText());
    }

}
