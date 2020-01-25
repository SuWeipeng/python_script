from machine import I2C
import time

# Si705x default address.
Si705x_I2CADDR = 0x40

# Command
CMD_MEASURE_TEMPERATURE_HOLD    = 0xE3
CMD_MEASURE_TEMPERATURE_NO_HOLD = 0xF3
CMD_RESET                       = 0xFE
CMD_WRITE_REGISTER              = 0xE6
CMD_READ_REGISTER               = 0xE7
CMD_READ_FIRMWARE_LSB           = 0X84
CMD_READ_FIRMWARE_HSB           = 0XB8

class Device:
  """Class for communicating with an I2C device.

  Allows reading and writing 8-bit, 16-bit, and byte array values to
  registers on the device."""

  def __init__(self, address, i2c):
    """Create an instance of the I2C device at the specified address using
    the specified I2C interface object."""
    self._address = address
    self._i2c = i2c

  def writeRaw8(self, value):
    """Write an 8-bit value on the bus (without register)."""
    b=bytearray(1)
    b[0] = value & 0xFF
    self._i2c.writeto(self._address, b)

  def write8(self, register, value):
    """Write an 8-bit value to the specified register."""
    b=bytearray(1)
    b[0]=value & 0xFF
    self._i2c.writeto_mem(self._address, register, b)

  def write16(self, register, value):
    """Write a 16-bit value to the specified register."""
    value = value & 0xFFFF
    b=bytearray(2)
    b[0]= value & 0xFF
    b[1]= (value>>8) & 0xFF
    self.i2c.writeto_mem(self._address, register, b)

  def readRaw8(self):
    """Read an 8-bit value on the bus (without register)."""
    return int.from_bytes(self._i2c.readfrom(self._address, 1),'little') & 0xFF

  def readU8(self, register):
    """Read an unsigned byte from the specified register."""
    return int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 1),'little') & 0xFF

  def readS8(self, register):
    """Read a signed byte from the specified register."""
    result = self.readU8(register)
    if result > 127:
      result -= 256
    return result

  def readU16(self, register, little_endian=True):
    """Read an unsigned 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = int.from_bytes(
        self._i2c.readfrom_mem(self._address, register, 2),'little') & 0xFFFF
    if not little_endian:
      result = ((result << 8) & 0xFF00) + (result >> 8)
    return result

  def readS16(self, register, little_endian=True):
    """Read a signed 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = self.readU16(register, little_endian)
    if result > 32767:
      result -= 65536
    return result

  def readU16LE(self, register):
    """Read an unsigned 16-bit value from the specified register, in little
    endian byte order."""
    return self.readU16(register, little_endian=True)

  def readU16BE(self, register):
    """Read an unsigned 16-bit value from the specified register, in big
    endian byte order."""
    return self.readU16(register, little_endian=False)

  def readS16LE(self, register):
    """Read a signed 16-bit value from the specified register, in little
    endian byte order."""
    return self.readS16(register, little_endian=True)

  def readS16BE(self, register):
    """Read a signed 16-bit value from the specified register, in big
    endian byte order."""
    return self.readS16(register, little_endian=False)


class Si705x:
  def __init__(self, address=Si705x_I2CADDR, i2c=None):
    # Create I2C device.
    if i2c is None:
      raise ValueError('An I2C object is required.')
    self._device = Device(address, i2c)
    # Set resolution.
    self._set_resolution(14)

  def _set_resolution(self, resolution):
    if resolution == 11:
      self._device.write8(CMD_WRITE_REGISTER, 0x81)
    if resolution == 12:
      self._device.write8(CMD_WRITE_REGISTER, 0x01)
    if resolution == 13:
      self._device.write8(CMD_WRITE_REGISTER, 0x80)
    if resolution == 14:
      self._device.write8(CMD_WRITE_REGISTER, 0x00)

  def read_raw_temp(self):
    """Reads the raw temperature from the sensor."""
    self._device.writeRaw8(CMD_MEASURE_TEMPERATURE_NO_HOLD)
    time.sleep_us(10000)  # Wait the required time
    msb = self._device.readRaw8()
    lsb = self._device.readRaw8()
    raw = (msb << 8) | lsb
    return raw

  def read_temperature(self):
    """Convert the raw temperature into a value that humans can read."""
    raw_temp = self.read_raw_temp()
    return (raw_temp * 175.72) / 65536 - 46.85

  @property
  def temperature(self):
    "Return the temperature in degrees."
    t = self.read_temperature()
    return "{:.2f}".format(t)
