public class Main {

    public static void main(String[] args) {
        MallardDuck a = new MallardDuck();
        a.performFly();
        a.performQuack();

        ModelDuck b = new ModelDuck();
        b.performFly();
        b.performQuack();
        b.setFlyBehavior(new FlyRocketPowered());
        b.performFly();

        DuckCall c = new DuckCall();
        c.perform();
    }
}
