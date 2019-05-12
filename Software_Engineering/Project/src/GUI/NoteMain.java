package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NoteMain extends Controller {
    private JTextArea textArea1;
    private JButton updateButton;
    private JButton closeButton;
    private JPanel mainPanel;
    private JPanel secondPanel;
    private JFrame frame;
    private final int SAVE_STATE = 1;
    private final int UPDATE_STATE = 0;
    private int currentState;

    public NoteMain(JFrame lastWindow, String inputStr) {

        frame = new JFrame("Edit Note");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(400, 250);

        textArea1 = new JTextArea();
        JScrollPane sp = new JScrollPane(textArea1);
        secondPanel.add(sp);

        frame.setVisible(true);

        currentState = UPDATE_STATE;

        display(inputStr);
        setWindowPosition(frame, lastWindow);


        updateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (currentState == UPDATE_STATE) {
                    updateButton.setText("Save");
                    currentState = SAVE_STATE;
                    textArea1.setEnabled(true);
                } else {
                    updateButton.setText("Update");
                    currentState = UPDATE_STATE;
                    textArea1.setEnabled(false);
                    save();
                }
            }
        });

        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        });

    }

    //TODO: implement save() and display();

    private void save() {
        System.out.println(textArea1.getText());
    }

    private void display(String inputStr) {
        textArea1.setEnabled(false);
        textArea1.setText(inputStr);
    }

}
