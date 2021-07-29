package CursoPOOUber.Java;

public class UberX extends Car {
    private String brand;

    private String model;

    public UberX( String license, Account driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
        //TODO Auto-generated constructor stub
    }

    @Override
    public void setPassenger(int passenger) {
        // TODO Auto-generated method stub
        super.setPassenger(4);
    }
    
}
