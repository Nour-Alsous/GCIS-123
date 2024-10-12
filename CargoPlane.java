package Assigement1_Group1;

public class CargoPlane extends Airplane implements Cargo 
{

    private double weight;

    public CargoPlane(String make, String flightNumber, int mileage, String flightDuration, String departuretime,
            String landingtime, int weight) 
    {
        super(make, flightNumber, mileage, flightDuration, departuretime, landingtime);

        this.weight=weight;
        
    }


    @Override
    public double getCargoWeight() 
    {
        return weight;

    }

    @Override
    public void setCargoWeight(double weight) 
    {
        this.weight=weight;
  
    }
    @Override
    public void displayDetails() {
    
        System.out.println("Flight type" + getMake() + "Flight number:" + getFlightNumber() + 
        "Miles traveled by the plane:" + getMileage() + "Flight Duration:" + getFlightduration()
        + "Departure time:" + getDeparturetime() + "Landing time:" + getLandingtime() + 
        "Weight of cargo:" + getCargoWeight() );
      
    }

}

