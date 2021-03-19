import time
import mlx90614, oled
from machine import I2C, Pin

i2c = I2C(scl=Pin(14), sda=Pin(12))

i2c_device = i2c.scan()
    
sensor = mlx90614.MLX90614(i2c)

oled_width = 128
oled_height = 32
oled = oled.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    line_1 = ""
    line_2 = ""
    line_3 = ""
    
    i2c_device = i2c.scan()
    print(i2c_device)
    
    t1 = sensor.read_object_temp() + 3.5
    line_2 = "temp : %.1f"%(t1)
        
    if 64 in i2c_device:
        try:
            t2 = si7051.temperature
            line_3 = "tmep : " + "%.1f"%(t2)
            line_1 = "delta: " + "%.1f"%(t2-t1)
        except NameError:
            import si7051
            si7051 = si7051.Si705x(i2c=i2c)
    else:
        if 'si7051' in locals().keys():
            del si7051
     
    if 41 in i2c_device:
        try:
            tof.start()
            tof.read()
            line_1 = "dist: " + "%.1f"%(tof.read()/10) + " cm"
            tof.stop()
        except NameError:
                import VL53L0X
                tof = VL53L0X.VL53L0X(i2c)
    else:
        if 'tof' in locals().keys():
            del tof
        
    oled.fill(0)
    oled.text(line_1, 10, 0)
    oled.text(line_2, 10, 15)
    oled.text(line_3, 10, 25)
    oled.show()
    time.sleep_ms(500)

