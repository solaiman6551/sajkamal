# sajkamal

A Simple Appointment Booking Management Using Django

There are mainly 2 users in here; 

User1: Creating Time Slots
User2: Booking A Available Time Slot

User1: In order to create new timeSlot, you need to create django super user. Then log in to the http://127.0.0.1:5000/admin and create your time slot from the "Time slots" table. Also, from this admin panel, you can edit or delete any time slot you want.
If you want to delete or edit any booked meeting, you can also do this from the admin panel. 
You cannot add same slot second time. So there is no chance to get conflicted.

User2: If you want to book a time slot, just run the project. In the Home Page you will see all the available and occupied time slots for present day.
You can book any available slot by clicking on "Book" button. Also, you will see all the booking list from booking page and Time Slot detail page as well.
Select the date from calender and provide your name in order to Book a time slot.

For UI, I just used very basic html.
