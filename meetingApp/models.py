from django.db import models


class TimeSlot(models.Model):
    time = models.CharField(max_length=120, unique=True,
                            choices=[('08.00AM-09.00AM', '08.00AM-09.00AM'),
                                     ('09.00AM-10.00AM', '09.00AM-10.00AM'),
                                     ('10.00AM-11.00AM', '10.00AM-11.00AM'),
                                     ('11.00AM-12.00PM', '11.00AM-12.00PM'),
                                     ('12.00PM-01.00PM', '12.00PM-01.00PM'),
                                     ('01.00PM-02.00PM', '01.00PM-02.00PM'),
                                     ('02.00PM-03.00PM', '02.00PM-03.00PM'),
                                     ('03.00PM-04.00PM', '03.00PM-04.00PM'),
                                     ('04.00PM-05.00PM', '04.00PM-05.00PM'),
                                     ('05.00PM-06.00PM', '05.00PM-06.00PM'),
                                     ('06.00PM-07.00PM', '06.00PM-07.00PM'),
                                     ('07.00PM-08.00PM', '07.00PM-08.00PM'),
                                     ('08.00PM-09.00PM', '08.00PM-09.00PM'),
                                     ])


class Booking(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    timeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
