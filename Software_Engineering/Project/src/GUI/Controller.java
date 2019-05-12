package GUI;

import javax.swing.*;

public class Controller {
    private final int offsetX = 100;
    private final int offSetY = 100;

    private final String[] UnitLabels = {"Liter", "Milliliter", "Quart", "Kilogram", "Gram"};

    public void setWindowPosition(JFrame currentWindow, JFrame lastWindow) {
        currentWindow.setLocation(lastWindow.getX() + offsetX, lastWindow.getY() + offSetY);
    }

    public void setUnitLabels(JComboBox box) {
        for (String s : UnitLabels) {
            box.addItem(s);
        }
    }
}
