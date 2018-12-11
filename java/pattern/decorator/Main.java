public class Main {

    public static void main(String[] args) {
        Beverage h = new HouseBlend();

        System.out.println(h.getDesc());
        System.out.println(h.cost());
        
        h = new Mocha(h);
        h = new Soy(h);

        System.out.println(h.getDesc());
        System.out.println(h.cost());

    }
}
