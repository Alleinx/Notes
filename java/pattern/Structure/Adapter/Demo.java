public class Demo {

}

interface Target {
    void request();
}

interface Adaptee {
    void specificRequest();
}

class Adapter implements Target, Adaptee {
    private Adaptee adaptee;
    private Target target;

    public Adapter(Target target) {
        this.target = target;
    }

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    public Adapter(Target target, Adaptee adaptee) {
        this.adaptee = adaptee;
        this.target = target;
    }

    @Override
    public void request() {
        adaptee.specificRequest();
    }

    @Override
    public void specificRequest() {
        target.request();
    }
}