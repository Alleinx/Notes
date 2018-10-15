public class ControllerGetMoney extends Controller{

    public ControllerGetMoney(Bank m) {
        super(m);
    }

    public String getMoney(String name) {
        String result;
        try {
            result = "Money: " + m.getMoney(name);
        }catch (UnknownCustomerException e) {
            result = e.getMessage();
        }
        return result;
    }
}
