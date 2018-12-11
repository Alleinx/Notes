public class Soy extends CondimentDecorator {
    Beverage beverage;

    public Soy(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public String getDesc() {
        return beverage.getDesc() + ",soy";
    }

    @Override
    public double cost() {
        return .15 + beverage.cost();
    }
}
