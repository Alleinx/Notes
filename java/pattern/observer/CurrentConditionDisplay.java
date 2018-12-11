public class CurrentConditionDisplay implements Observer, DisplayElement {
    private float temperature;
    private float humidity;
    // private Subject weatherData;

    // public CurrentConditionDisplay(Subject e) {
        // this.weatherData = e;
        // weatherData.registerObserver(this);
    // }

    @Override
    public void update(float temp, float humidity, float pressure) {
        this.temperature = temp;
        this.humidity = humidity;
        display();
    }

    @Override
    public void display() {
        System.out.println("Current conditions: " +
                           temperature            +
                           "F degrees and "       +
                           humidity               +
                           "% humidity");
    }
}
