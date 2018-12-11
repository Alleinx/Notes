public abstract class Beverage {
    public String getDesc() {
        return desc;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
        switch (size) {
            case "s":
                this.size_money = 0.1;
                break;
            case "m":
                this.size_money = 0.15;
                break;
            case "l":
                this.size_money = 0.20;
                break;
        }
    }

    public double getSize_money() {
        return size_money;
    }

    public abstract double cost();

    String desc = "Unknown Beverage";
    private String size = "Unknown Size";
    private double size_money = 0.0;
}
