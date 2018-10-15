import java.awt.*;

public class ViewHistory extends View {
    private ControllerHistory c;

    public ViewHistory(Bank m, ControllerHistory c) {
        super(m);
        this.c = c;
        this.add(new HistoryPanel(m));
        this.setSize(400, 300);
        this.setTitle("History");
        this.setLayout(new GridLayout());

        this.setVisible(true);
    }

    @Override
    public void update() {
        repaint();
    }
}
