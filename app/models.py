from django.db import models


class Client(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    series_of_passport = models.IntegerField()
    passport_number = models.IntegerField()
    birthday_date = models.DateField(blank=True)
    adress = models.CharField(max_length=250)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class Contract(models.Model):
    client = models.ForeignKey(Client)
    date = models.DateField(blank=True)
    storage_life = models.IntegerField()
    cell_number = models.IntegerField()
    payment = models.FloatField()
    contract_number = models.IntegerField()

    def __str__(self):
        return 'Договор №'+str(self.contract_number)


class Worth(models.Model):
    contract = models.ForeignKey(Contract)
    evidence = models.CharField(max_length=500)
    cost = models.FloatField()

    def __str__(self):
        return self.evidence
