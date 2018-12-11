public class Context {

    public Context() {
        stateA = new ConcreteStateA(this);
        stateB = new ConcreteStateB(this);
        state = stateB;
    }

    public void start() {
        state.change();
    }

    public void setState(State state) {
        this.state = state;
    }

    State state;
    State stateA;
    State stateB;
}