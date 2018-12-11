public class Whip extends CondimentDecorator {
    Beverage beverage;

    public Whip(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public String getDesc() {
        return beverage.getDesc() + ",whip";
    }

    @Override
    public double cost() {
        return .15 + beverage.cost();
    }
}
