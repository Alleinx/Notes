public class ConcreteStateB implements State {
    
    public ConcreteStateB(Context context) {
        this.context = context;
    }

    @Override
    public void change() {
        System.out.println("Concrete state B...");
        try {
            Thread.sleep(1000L);
        } catch (Exception e) {
            e.printStackTrace();
        }
        context.setState(context.stateA);
        context.start();
    }

    private Context context;
}