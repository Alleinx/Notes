public class RecipeIngredient extends Ingredient {
	private Recipe recipe;

	public void updateUnit(String unit) {
		super.setUnit(unit);
	}

	public void setRecipe(Recipe newRecipe) {
		if(recipe != newRecipe) {
			Recipe oldRecipe = recipe;
			recipe = newRecipe;
			if(newRecipe != null) {
				newRecipe.addRecipeIngredient(this);
			}
			if(oldRecipe != null) {
				oldRecipe.removeRecipeIngredient(this);
			}
		}
	}
}
