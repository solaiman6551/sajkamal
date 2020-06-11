from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from meetingApp.models import TimeSlot, Booking
import datetime

start_template = """
<html>
    <body>
        <h4 style="text-align:center">Book YourTime Slot</h4>
        <ul style="text-align:center">
        <a href="/">Home</a></li>
        <li style="display: inline;">
        
        </ul>
        <div>
            {}
        </div>
    </body>
</html>
"""

time_slot_list_table = """
<table style="border: 1px solid black; border-collapse: collapse" >
    <thead>
        <tr style="border: 1px solid black; border-collapse: collapse">
            <th style="border: 1px solid black">Time Slot</th>
            <th style="border: 1px solid black">Availability Status For Today</th>
            <th style="border: 1px solid black">Reservation</th>
        </tr>
    </thead>
    <tbody>
        {}
    </tbody>
</table>
"""

today = datetime.date.today()


def view_all(request):
    time_slot_data = TimeSlot.objects.all().order_by("time")
    table_rows = ""
    for time in time_slot_data:

        check_booking = Booking.objects.filter(
            date=today, timeSlot=time
        )
        if check_booking:
            reservation_status = """
            <td style="text-align: center; background-color: #E6B0AA;">Occupied
            </td>"""
        else:
            reservation_status = """
            <td style="text-align: center; background-color: #ABEBC6;">Available
            </td>"""

        table_rows += f"""
        <tr style="border: 1px solid black">
            <td>
                <a href="/time/{time.id}">{time.time}</a>
            </td>
            
            {reservation_status}
            
            <td style="text-align: center;">
                <a href="/time/reservation/{time.id}">Book</a>
            </td>
        </tr>
        """

    return HttpResponse(
        start_template.format(time_slot_list_table.format(table_rows))
    )


def check_time_bookings(time_object):
    time_slot_bookings = Booking.objects.filter(
        timeSlot=time_object, date__gte=today
    ).order_by("date")

    html = ""
    if time_slot_bookings:
        html += "<ul>"
        # Add reserved dates
        for booking in time_slot_bookings:
            html += f"<li>{booking.date} || booked by {booking.name}</li>"
        html += "</ul>"
    else:
        html += "No booking found"
    return html


def show_time_slot(request, id):
    try:
        timeSlot = TimeSlot.objects.get(id=id)
        time_slot_display_html = f"""
        <h2>{timeSlot.time}</h2>

        <p><a href="/time/reservation/{timeSlot.id}">Book</a></p>
        <p>Booking List With Date And Name:</p>
        {check_time_bookings(timeSlot)}
        """

        return HttpResponse(start_template.format(time_slot_display_html))
    except ObjectDoesNotExist:
        return HttpResponse("There is no slot available with this number.")


@csrf_exempt
def reserve_time_slot(request, id):
    try:
        time_slot_data = TimeSlot.objects.get(id=id)
    except:
        return HttpResponse("There is no slot available with this number")

    reservation_response = f"""
        <h2>Time Slot: {time_slot_data.time}</h2>
        <form action="#" method="POST">
            <label>Select Date<br>
            <input type="date" name="reservation_date" required="required" min="{today}">
            </label><br><br>
            <label>Enter Your Name:<br>
            <input type="text" name="name" required="required">
            </label> <br><br>
            <button name="submit">Book</button>
        </form><br>
        <p>Booking List With Date And Name:</p> 
        {check_time_bookings(time_slot_data)}
        """

    if request.method == "GET":
        return HttpResponse(start_template.format(reservation_response))
    elif request.method == "POST":
        # Modify date format, then check
        year, month, day = map(
            int, request.POST.get("reservation_date").split("-")
        )

        # Check existing bookings
        check_bookings = Booking.objects.filter(
            date=datetime.date(year, month, day), timeSlot=time_slot_data
        )
        if check_bookings:
            return HttpResponse(
                "This slot is already booked, Try another slot or select another day"
            )

        # Create a slot booking
        Booking.objects.create(
            date=request.POST.get("reservation_date"),
            name=request.POST.get("name"),
            timeSlot=time_slot_data
        )
        return redirect(reverse("view_all"))
