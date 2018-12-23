import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import java.awt.*;

class ButtonFrame extends JFrame{
    private JPanel buttonPanel;
    private final int DEFAULT_WIDTH = 300;
    private final int DEFAULT_HEIGHT = 200;

    public ButtonFrame() {
        setTitle("Button test");
        setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);

        JButton yellowB = new JButton("Yellow");
        JButton blueB = new JButton("Blue");
        JButton redB = new JButton("Red");

        buttonPanel = new JPanel();
        buttonPanel.add(yellowB);
        buttonPanel.add(blueB);
        buttonPanel.add(redB);

        this.add(buttonPanel);
        ColorAction yellowA = new ColorAction(Color.YELLOW);
        ColorAction blueA = new ColorAction(Color.BLUE);
        ColorAction redA = new ColorAction(Color.RED);

        yellowB.addActionListener(yellowA);
        blueB.addActionListener(blueA);
        redB.addActionListener(redA);
    }

    private class ColorAction implements ActionListener {
        private Color backgroundColor;

        public ColorAction(Color c) {
            backgroundColor = c;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            buttonPanel.setBackground(backgroundColor);
        }
    }
}