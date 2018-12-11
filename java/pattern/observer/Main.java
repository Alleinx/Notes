public class Main {

    public static void main(String[] args) {
	    WeatherData weatherdata = new WeatherData();

	    CurrentConditionDisplay currentdisplay = new CurrentConditionDisplay();
		HeatIndex heat = new HeatIndex();

		weatherdata.registerObserver(currentdisplay);
		weatherdata.registerObserver(heat);
	    weatherdata.setMeasurements(12, 3, 50);
    }
}
