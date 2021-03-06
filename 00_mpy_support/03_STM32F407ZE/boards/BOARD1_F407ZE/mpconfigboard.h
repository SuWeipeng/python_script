#define MICROPY_HW_BOARD_NAME       "SUGAR-PYB"
#define MICROPY_HW_MCU_NAME         "STM32F407"

#define MICROPY_HW_HAS_SWITCH       (1)
#define MICROPY_HW_ENABLE_SDCARD    (1)
#define MICROPY_HW_HAS_FLASH        (1)
#define MICROPY_HW_ENABLE_RNG       (1)
#define MICROPY_HW_ENABLE_RTC       (1)
#define MICROPY_HW_ENABLE_DAC       (1)
#define MICROPY_HW_ENABLE_USB       (1)

// HSE is 8MHz
#define MICROPY_HW_CLK_PLLM (4)
#define MICROPY_HW_CLK_PLLN (168)
#define MICROPY_HW_CLK_PLLP (RCC_PLLP_DIV2)
#define MICROPY_HW_CLK_PLLQ (7)

// UART config
#define MICROPY_HW_UART1_TX     (pin_A9)
#define MICROPY_HW_UART1_RX     (pin_A10)
#define MICROPY_HW_UART2_TX     (pin_A2)
#define MICROPY_HW_UART2_RX     (pin_A3)

// I2C busses
#define MICROPY_HW_I2C2_SCL (pin_F1)
#define MICROPY_HW_I2C2_SDA (pin_F0)

// SPI busses
#define MICROPY_HW_SPI1_NSS  (pin_G7)
#define MICROPY_HW_SPI1_SCK  (pin_B3)
#define MICROPY_HW_SPI1_MISO (pin_B4)
#define MICROPY_HW_SPI1_MOSI (pin_B5)
#define MICROPY_HW_SPI2_NSS  (pin_C1)
#define MICROPY_HW_SPI2_SCK  (pin_B10)
#define MICROPY_HW_SPI2_MISO (pin_C2)
#define MICROPY_HW_SPI2_MOSI (pin_C3)

// CAN busses
//#define MICROPY_HW_CAN1_TX (pin_D1)
//#define MICROPY_HW_CAN1_RX (pin_D0)

// USRSW is pulled low. Pressing the button makes the input go high.
#define MICROPY_HW_USRSW_PIN        (pin_A0)
#define MICROPY_HW_USRSW_PULL       (GPIO_NOPULL)
#define MICROPY_HW_USRSW_EXTI_MODE  (GPIO_MODE_IT_RISING)
#define MICROPY_HW_USRSW_PRESSED    (1)

// LEDs
#define MICROPY_HW_LED1             (pin_F10) // red
#define MICROPY_HW_LED2             (pin_F10) // green
#define MICROPY_HW_LED3             (pin_F9) // orange
#define MICROPY_HW_LED4             (pin_F9) // blue
#define MICROPY_HW_LED_ON(pin)      (mp_hal_pin_low(pin))
#define MICROPY_HW_LED_OFF(pin)     (mp_hal_pin_high(pin))

// USB config
#define MICROPY_HW_USB_FS              (1)
