public class Espresso extends Beverage {

    public Espresso() {
        desc = "Espresso";
    }

    @Override
    public double cost() {
        return getSize_money() + 1.99;
    }
}
