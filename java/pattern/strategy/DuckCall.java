public class DuckCall {

    public DuckCall() {
        quackBehavior = new Quack();
    }

    public void perform() {
        this.quackBehavior.quack();
    }

    private QuackBehavior quackBehavior;
}
