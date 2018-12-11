public class ConcreteStateA implements State {
    
    public ConcreteStateA(Context context) {
        this.context = context;
    }

    @Override
    public void change() {
        System.out.println("Concrete state A...");
        try {
            Thread.sleep(1000L);
        } catch (Exception e) {
            e.printStackTrace();
        }
        context.setState(context.stateB);
        context.start();
    }

    private Context context;
}