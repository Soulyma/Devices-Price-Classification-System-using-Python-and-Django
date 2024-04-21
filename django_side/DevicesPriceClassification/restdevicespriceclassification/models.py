from django.db import models
from .apps import RestdevicespriceclassificationConfig

class Device(models.Model):
    #dev_id = models.FloatField()
    battery_power = models.IntegerField()
    blue = models.BooleanField()
    clock_speed = models.FloatField()
    dual_sim = models.BooleanField()
    fc = models.IntegerField()
    four_g = models.BooleanField()
    int_memory = models.IntegerField()
    m_dep = models.FloatField()
    mobile_wt = models.IntegerField()
    n_cores = models.IntegerField()
    pc = models.IntegerField()
    px_height = models.IntegerField()
    px_width = models.IntegerField()
    ram = models.IntegerField()
    sc_h = models.IntegerField()
    sc_w = models.IntegerField()
    talk_time = models.IntegerField()
    three_g = models.BooleanField()
    touch_screen = models.BooleanField()
    wifi = models.BooleanField()

def __str__(self):
    return self.touch_screen
        
        

