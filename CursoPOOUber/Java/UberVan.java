package CursoPOOUber.Java;

import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car {
    private Map<String, Map<String,Integer>> typeCarAccepted;
    private ArrayList<String> seatsMaterial;

    public UberVan( String license, Account driver,
    Map<String, Map<String,Integer>> typeCarAccepted
    ,ArrayList<String> seatsMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
        //TODO Auto-generated constructor stub
    }

    @Override
    public void setPassenger(int passenger) {
        // TODO Auto-generated method stub
        super.setPassenger(6);
    }
}
