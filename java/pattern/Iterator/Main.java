public class Main {

    public static void main(String[] args) {
    DinerMenu dinerMenu = new DinerMenu();
    Waitress waitress = new Waitress(dinerMenu);
    waitress.printMenu();
	// write your code here
    }
}
