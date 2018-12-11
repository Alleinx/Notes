public class HeatIndex implements Observer, DisplayElement {
    private double heatindex;
    // private WeatherData weatherData;

    // public HeatIndex(WeatherData e) {
        // weatherData = e;
        // e.registerObserver(this);
    // }

    @Override
    public void update(float temp, float humidity, float pressure) {
        changeHeatIndex(temp, humidity);
        display();
    }

    @Override
    public void display() {
        System.out.println("Heat index is " + heatindex);
    }

    private void changeHeatIndex(float T, float RH) {
        heatindex = (T * 10) + (RH * 2);
    }
}
