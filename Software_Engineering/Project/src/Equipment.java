public class Equipment {
    private String name;
    private int maxVolume;
    private int currentVolume;
    private String unit;
    private Brew brew;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMaxVolume() {
        return maxVolume;
    }

    public void setMaxVolume(int maxVolume) {
        if (maxVolume >= 0) {
			this.maxVolume = maxVolume;
		} else {
			System.out.println("Error: Negative max volume value.");
		}
    }

    public int getCurrentVolume() {
        return currentVolume;
    }

    public void addCurrentVolume(int volume) {
        if (volume >= 0) {
			if (volume + currentVolume > maxVolume) {
				System.out.println("Error: Can't store more volume , current volume :" +
									currentVolume +
									" Add amount : " +
									volume +
									" ,max Volume(capacity) :" +
									maxVolume);
			} else {

				currentVolume += volume;
			}
		} else {
			System.out.println("Error: Negative add volume value.");
		}
    }

    public void consumeCurrentVolume(int volume) {
        if (volume >= 0) {
			if (volume > currentVolume) {
				System.out.println("Error: Don't have enough volume to consume, available volume amount:" +
						currentVolume +
						" , consume amount :" +
						volume);
			} else {
				currentVolume -= volume;
			}

		} else {
			System.out.println("Error: Negative consume volume value.");
		}
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public void setBrew(Brew newBrew) {
        if(brew != newBrew) {
            Brew oldBrew = brew;
            brew = newBrew;
            if(newBrew != null) {
                newBrew.addEquipment(this);
            }
            if(oldBrew != null) {
                oldBrew.removeEquipment(this);
            }
        }
    }
}
