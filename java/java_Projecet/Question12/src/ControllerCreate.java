public class ControllerCreate extends Controller {

    public ControllerCreate(Bank m) {
        super(m);
    }

    public String create(String name, String amount, int type) {
        int input_amount;
        String result;

        try {
            input_amount = Integer.parseInt(amount);
            if (type == 0) {
                m.addAccount(new CreditAccount(name, input_amount));
                result = "";
            } else {
                try {
                    m.addAccount(new StudentAccount(name, input_amount));
                    result = "";
                } catch (NotEnoughMoneyException e) {
                    result = e.getMessage();
                }
            }

        } catch (NumberFormatException e) {
            result = "Must input an integer!";
        }

        return result;
    }
}
