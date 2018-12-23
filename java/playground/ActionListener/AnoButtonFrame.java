/* Anomous inner class demonstration */

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import java.awt.*;

class AnoButtonFrame extends JFrame{
    private JPanel buttonPanel;
    private final int DEFAULT_WIDTH = 300;
    private final int DEFAULT_HEIGHT = 200;

    public AnoButtonFrame() {
        setTitle("Button test");
        setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);

        buttonPanel = new JPanel();
        makeButton("Yello", Color.YELLOW);
        makeButton("Blue", Color.BLUE);
        makeButton("Red", Color.RED);
        this.add(buttonPanel);

    }

    private void makeButton(final String name, final Color backgroundColor) {
        /* Need final for local variables */

        JButton button = new JButton(name);
        buttonPanel.add(button);

        button.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                buttonPanel.setBackground(backgroundColor);
            }
        });
    }
}