public class StorageIngredient extends Ingredient {
    private Brew brew;

    public void addAmount(int amount) {
        if (amount >= 0) {
			super.setAmount(super.getAmount() + amount);
		} else {
			System.out.println("Error: Negative add amount value.");
		}
    }

    public void consumeAmount(int amount) {
        if (amount >= 0) {
			if (amount <= this.getAmount()) {
				super.setAmount(super.getAmount() - amount);
			} else {
				System.out.println("Error: Don't have enough ingredient to consume, available ingredient amount:" +
									this.getAmount() +
									" , consume amount :" +
									amount);
			}
		} else {
			System.out.println("Error: Negative consume amount value.");
		}
    }

    public void setBrew(Brew newBrew) {
        if (brew != newBrew) {
            Brew oldBrew = brew;
            brew = newBrew;
            if (newBrew != null) {
                newBrew.addStorageIngredient(this);
            }
            if (oldBrew != null) {
                oldBrew.removeStorageIngredient(this);
            }
        }
    }
}
