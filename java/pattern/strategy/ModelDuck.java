public class ModelDuck extends Duck {
    
    public ModelDuck() {
        setFlyBehavior(new FlyNoWay());
        setQuackBehavior(new Squack());
    }

    public void display() {
        System.out.println("I'm a Model duck!");
    }
}
