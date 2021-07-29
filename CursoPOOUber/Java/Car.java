package CursoPOOUber.Java;

public class Car {
    private int id;
    private String license;
    private Account driver;
    private int passenger;

    public Car(String license, Account driver) {
        // this.id = id;
        this.license = license;
        this.driver = driver;
        // this. passenger = passenger;
    }

    public int getId() {
        return id;
    }
    public String getLicense() {
        return license;
    }
    public Account getDriver() {
        return driver;
    }
    public int getPassenger() {
        return passenger;
    }

    public void setId(int id) {
        this.id = id;
    }
    public void setLicense(String license) {
        this.license = license;
    }
    public void setDriver(Account driver) {
        this.driver = driver;
    }
    public void setPassenger(int passenger) {
        this.passenger = passenger;
    }

    @Override
    public String toString() {
        return "Car licensed: "+this.license+", Driver: "+this.driver.getName() +", Passenger: "+this.passenger;
    }
}
