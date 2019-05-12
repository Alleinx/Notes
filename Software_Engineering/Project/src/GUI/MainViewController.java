package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;

public class MainViewController {
    private JPanel mainPanel;
    private JButton recommendButton;
    private JButton recipeButton;
    private JButton equipmentButton;
    private JButton historyButton;
    private JButton ingredientButton;
    private JSplitPane splitPane;
    private JFrame frame;

    private final int positionX = 50;
    private final int positionY = 50;


    public MainViewController() {

        frame = new JFrame("Brew Day");
        frame.setContentPane(this.mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 250);
        frame.setVisible(true);

        frame.setLocation(positionX, positionY);
        splitPane.setEnabled(false);
        splitPane.setDividerSize(0);

        recommendButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new RecommendMain(frame);
            }
        });

        recipeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new RecipeMain(frame);
            }
        });

        equipmentButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new EquipmentMain(frame);
            }
        });

        historyButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new Log(frame);
            }
        });

        ingredientButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new IngredientMain(frame);
            }
        });
    }

    public static void main(String[] args) {
        new MainViewController();
    }
}
