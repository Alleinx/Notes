public class ControllerWithdraw extends Controller {

    public ControllerWithdraw(Bank m) {
        super(m);
    }

    public String withdraw(String name, String amount) {
        int input_amount;
        String result;
        try {
            input_amount = Integer.parseInt(amount);
            try {
                m.withdraw(name, input_amount);
                result = "";
            } catch (UnknownCustomerException e) {
                result = e.getMessage();
            } catch (NotEnoughMoneyException e) {
                result = e.getMessage();
            }
        } catch (NumberFormatException e) {
            result = "Must input an integer!";
        }

        return result;
    }
}
