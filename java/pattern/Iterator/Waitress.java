public class Waitress {
    private Menu diner;

    public Waitress(Menu diner) {
        this.diner = diner;
    }

    public void printMenu() {
        Iterator dinerIterator = diner.createIterator();
        printMenu(dinerIterator);
    }

    private void printMenu(Iterator iterator) {
        MenuItem menuItem;
        while(iterator.hasNext()) {
            menuItem = (MenuItem)iterator.next();
            System.out.println(menuItem.getName() +
                               menuItem.getDesc() +
                               menuItem.isVegetarian() +
                               menuItem.getPrice());
        }
    }
}
