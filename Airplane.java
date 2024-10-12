package Assigement1_Group1;

public abstract class Airplane {

    private String make;
    private String flightNumber;
    private String planeType;
    private int mileage;
    private String flightduration;
    private String departuretime;
    private String landingtime;

    public Airplane(String make, String flightNumber, int mileage, String flightDuration, String departuretime, String landingtime )
    {
        this.make=make;
        this.flightNumber=flightNumber;
        this.mileage=mileage;
        this. flightduration=flightDuration;
        this.departuretime=departuretime;
        this.landingtime=landingtime;
    }
   

    //Setters
    
    public void setMake(String make) {
        this.make = make;
    }
    
    public void setFlightNumber(String flightNumber) 
    {
        this.flightNumber = flightNumber;
    }
    public void setMileage(int mileage) 
    {
        this.mileage = mileage;
    }
    public void setPlaneType(String planeType) 
    {
        this.planeType = planeType;
    }
    public void setFlightduration(String flightduration)
     {
        this.flightduration = flightduration;
    }
    public void setDeparturetime(String departuretime) 
    {
        this.departuretime = departuretime;
    }
    public void setLandingtime(String landingtime)
    {
        this.landingtime = landingtime;
    }

    // Getters

    public String getLandingtime() {
        return landingtime;
    }
    public String getFlightduration() {
        return flightduration;
    }
    public String getMake() {
        return make;
    }
    
    public String getFlightNumber() {
        return flightNumber;
    }
    public int getMileage() {
        return mileage;
    }
    public String getPlaneType() {
        return planeType;
    }
    public String getDeparturetime() {
        return departuretime;
    }


    public static void displayDetails(String args)
    {
         
    }

    public abstract void displayDetails();
    
}
