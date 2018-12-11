public class MallardDuck extends Duck{

    public MallardDuck() {
        setFlyBehavior(new FlyWithWings());
        setQuackBehavior(new Quack());
    }
    public void display() {
        System.out.println("This is a mallard Duck.");
    }
}
