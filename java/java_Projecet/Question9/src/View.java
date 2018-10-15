import javax.swing.*;

public abstract class View extends JFrame implements ModelListener{
    protected Bank m;

    public View(Bank m) {
        this.m = m;
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public abstract void update();
}
