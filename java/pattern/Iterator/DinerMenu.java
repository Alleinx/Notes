public class DinerMenu implements Menu{
    static final int MAX_ITEMS = 6;
    int numOfItems = 0;
    MenuItem[] menuItems;

    public DinerMenu() {
        menuItems = new MenuItem[MAX_ITEMS];
        addItem("BL", "BB", true, 2.99);
        addItem("BL", "BBT", true, 3.22);
    }

    public void addItem(String name, String desc, boolean vegetarian, double price) {
        MenuItem menuItem = new MenuItem(name, desc, vegetarian, price);
        if (numOfItems >= MAX_ITEMS) {
            System.err.println("Menu is full!");
        } else {
            this.menuItems[numOfItems] = menuItem;
            numOfItems++;
        }
    }

    @Override
    public Iterator createIterator() {
        return new DinerMenuIterator(menuItems);
    }
}
