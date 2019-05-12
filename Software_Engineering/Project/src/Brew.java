import java.util.Date;
import java.util.HashSet;
import java.util.Set;

public class Brew {
    private Date time;
    private int batchSize;
    private String unit;
    private Recipe recipe;
    private Note note;
    private Set<Equipment> equipments;
    private Set<StorageIngredient> storageIngredients;

    public Brew(Note note) {
        this.note = note;
        this.equipments = new HashSet<>();
        this.storageIngredients = new HashSet<>();
    }

    public Date getTime() {
        return time;
    }

    public void setTime(Date time) {
        this.time = time;
    }

    public int getBatchSize() {
        return batchSize;
    }

    public void setBatchSize(int batchSize) {
        if (batchSize >= 0) {
			this.batchSize = batchSize;
		} else {
			System.out.println("Error: Negative value for batch size.");
		}
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public Recipe getRecipe() {
        return recipe;
    }

    public Note getNote() {
        return note;
    }

    public void setRecipe(Recipe r) {
        if (this.recipe != r) {
            Recipe oldRecipe = this.recipe;
            this.recipe = r;
            if (r != null) {
                r.addBrew(this);
            }
            if (oldRecipe != null) {
                oldRecipe.removeBrews(this);
            }
        }
    }

    public void addEquipment(Equipment equipment) {
        equipments.add(equipment);
        equipment.setBrew(this);
    }

    public void removeEquipment(Equipment equipment) {
        equipments.remove(equipment);
        equipment.setBrew(null);
    }

    public void addStorageIngredient(StorageIngredient storageIngredient) {
        storageIngredients.add(storageIngredient);
        storageIngredient.setBrew(this);
    }

    public void removeStorageIngredient(StorageIngredient storageIngredient) {
        storageIngredients.remove(storageIngredient);
    }
}
