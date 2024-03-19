// Create a reasonably complicated Object in JavaScript that contains attributes and methods for the Motelcustomer.  The  customer  attributes  should  include  (and  not be limited  to),  the customer’sname, birth date,  gender,  androompreferences  (as  an  array),  payment method, mailing  address  (as  a  sub-object), phone  number, check-in,and  check-out  date  (as  a  sub-object),  and object methods  to  determine theirage  and  duration  of  stay.  The  JavaScript  code  should  also  create  a  template  literal  string,  or  properly formatted html, that describes the customer. In other words, writes a paragraph describing the customer with many of their personal attributes dynamically embedded in the string / html coming from the above object definition.

 const MotelCustomer = { //could set up as a let to change the values for new customers
    name: "Kyle Hollett",
    birthDate: new Date(1988, 10, 29),
    gender: "Male",
    roomPreference: ["Non-smoking", "Pets Allowed", "Room Size", "Number of Beds", "Price", "Close Amenities", "Safety and Security", "RoomCondition", "Check-in/Check-out Times", "Reviews and Ratings", "Additional Services"],
    paymentMethod: "Credit Card",
    mailingAddress: {
        street: "200 Little Johns Ave",
        city: "St John's",
        province: "NL",
        country: "Canada",
        postalCode: "A1B1B7"
      },
    phoneNumber: "1-709-555-5555",
    checkInDate: new Date(2024, 5, 11),
    checkOutDate: new Date(2024, 5, 21),

    getAge: function() {
        const today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        return age;
    },

    getDurationOfStay: function() {
        const millisecondsPerDay = 1000 * 60 * 60 * 24;
        const checkInTime = this.checkInDate.getTime();
        const checkOutTime = this.checkOutDate.getTime();
        const durationInMilliseconds = checkOutTime - checkInTime;
        return Math.ceil(durationInMilliseconds / millisecondsPerDay);
  } 
};

