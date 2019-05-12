import java.util.HashSet;
import java.util.Set;

public class Recipe {
	private String name;
	private Set<Brew> brews;
	private Set<RecipeIngredient> recipeIngredients;

	public Recipe(String name) {
		this.name = name;
		brews = new HashSet<>();
		recipeIngredients = new HashSet<>();
	}

	/* Get the recipe Name */
	public String getName() {
		return name;
	}

	/* Set the recipe Name */
	public void setName(String name) {
		this.name = name;
	}

	/* Give Brew a Recipe */
	public void addBrew(Brew b) {
		brews.add(b);
		b.setRecipe(this);
	}

	/* One brew has 0...1 recipe, one recipe could be owned by many brews */
	public void removeBrews(Brew b) {
		brews.remove(b);
		b.setRecipe(null);
	}

	public void addRecipeIngredient(RecipeIngredient recipeIngredient) {
		recipeIngredients.add(recipeIngredient);
		recipeIngredient.setRecipe(this);
	}

	public void removeRecipeIngredient(RecipeIngredient recipeIngredient) {
		recipeIngredients.remove(recipeIngredient);
		recipeIngredient.setRecipe(null);
	}
}
