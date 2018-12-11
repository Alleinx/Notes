import java.util.*;

public class LoadBalancer {
    private static LoadBalancer instance = null;
    private ArrayList<String> serverList = null;

    private LoadBalancer() {
        serverList = new ArrayList<String>();
    };

    public static LoadBalancer getLoadBalancer() {
        if (instance == null) {
            instance = new LoadBalancer();
        }

        return instance;
    }

    public void addServer(String server) {
        serverList.add(server);
    }

    public void removeServer(String server) {
        serverList.remove(server);
        /* check if 'server' exists in the server? */
    }

    public String getServer() {
        Random random = new Random();
        int i = random.nextInt(serverList.size());
        return (String)serverList.get(i);
    }
}