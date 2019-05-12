public class Ingredient {
	private String name;
	private double amount;
	private String unit;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getAmount() {
		return amount;
	}

	public void setAmount(double amount) {
		if (amount >= 0) {
			this.amount = amount;
		} else {
			System.out.println("Error : Negative amount value");
		}
	}

	public String getUnit() {
		return unit;
	}

	public void setUnit(String unit) {
		this.unit = unit;
	}
}
