#ifndef __MODULE_RS232_H
#define __MODULE_RS232_H

typedef struct {
	char ch;
} serial_msg;

typedef struct {
	char(*getc)(void);
	void (*putc)(char str);
	int (*puts)(const char *msg);
	int (*gets)(void);
	int (*printf)(const char *format, ...);
} SERIAL;

extern SERIAL serial;
extern SERIAL serial2;
void putc_base(char str);
void Ultrasonic_putc_base(char str);
char getc_base(void);
char Ultrasonic_getc_base(void);
int puts_base(const char *msg);
int Ultrasonic_puts_base(const char *msg);
int gets_base(void);
int Ultrasonic_gets_base(void);
int printf_base(const char *format, ...);
void Serial_Config(int buadrate);
void Ultrasonic_Serial_Config(int buadrate);
void USART2_IRQHandler();

#endif
