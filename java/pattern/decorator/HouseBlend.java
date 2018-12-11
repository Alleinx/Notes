public class HouseBlend extends Beverage {

    public HouseBlend() {
        desc = "House Blend Coffee";
    }

    @Override
    public double cost() {
        return getSize_money() + .89;
    }
}
