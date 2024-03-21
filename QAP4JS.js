// Create a reasonably complicated Object in JavaScript that contains attributes and methods for the Motelcustomer.  The  customer  attributes  should  include  (and  not be limited  to),  the customer’sname, birth date,  gender,  androompreferences  (as  an  array),  payment method, mailing  address  (as  a  sub-object), phone  number, check-in,and  check-out  date  (as  a  sub-object),  and object methods  to  determine theirage  and  duration  of  stay.  The  JavaScript  code  should  also  create  a  template  literal  string,  or  properly formatted html, that describes the customer. In other words, writes a paragraph describing the customer with many of their personal attributes dynamically embedded in the string / html coming from the above object definition.

 const MotelCustomer = { //could set up as a let to change the values for new customers
    name: "Kyle Hollett",
    birthDate: new Date(1988, 10, 29),
    gender: "Male",
    roomPreference: ["Non-smoking", "Pets Allowed", "Room Size", "Number of Beds", "Price", "Close Amenities", "Safety and Security", "Room Condition", "Check-in/Check-out Times", "Reviews and Ratings", "Additional Services"],
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

const customerDescription = `Name: ${MotelCustomer.name}
Age: ${MotelCustomer.getAge()}
Gender: ${MotelCustomer.gender}
Room Preferences: ${MotelCustomer.roomPreference.join(', ')}
Payment Method: ${MotelCustomer.paymentMethod}
Mailing Address: ${MotelCustomer.mailingAddress.street}, ${MotelCustomer.mailingAddress.city}, ${MotelCustomer.mailingAddress.province}, ${MotelCustomer.mailingAddress.country}, ${MotelCustomer.mailingAddress.postalCode}
Phone Number: ${MotelCustomer.phoneNumber}
Check-In Date: ${MotelCustomer.checkInDate.toDateString()}
Check-Out Date: ${MotelCustomer.checkOutDate.toDateString()}
Duration of Stay: ${MotelCustomer.getDurationOfStay()} days`;


console.log(customerDescription);

let roomPreferenceSentence = `This luxurious hotel offers ${MotelCustomer.roomPreference[0]} with ${MotelCustomer.roomPreference[1]}, spacious ${MotelCustomer.roomPreference[2]}s, with a ${MotelCustomer.roomPreference[3]} options, competitive ${MotelCustomer.roomPreference[4]}s, ${MotelCustomer.roomPreference[5]}, top-notch ${MotelCustomer.roomPreference[6]}, impeccable ${MotelCustomer.roomPreference[7]}s, flexible ${MotelCustomer.roomPreference[8]}, stellar ${MotelCustomer.roomPreference[9]}, and a range of ${MotelCustomer.roomPreference[10]} to enhance your stay.`

console.log(roomPreferenceSentence)

// This luxurious hotel offers non-smoking rooms with pets allowed, spacious room sizes, a variety of bed options, competitive prices, close amenities, top-notch safety and security, impeccable room conditions, flexible check-in/check-out times, stellar reviews and ratings, and a range of additional services to enhance your stay.