#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        print ("0 ADC    = %lf V"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC    = %lf V"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC    = %lf V"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC    = %lf V"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC    = %lf V"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC    = %lf V"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC    = %lf V"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC    = %lf V"%(ADC_Value[7]*5.0/0x7fffff))
        print ("diff 0-1 = %lf V"%((ADC_Value[0]-ADC_Value[1])*5.0/0x7fffff))
        print ("diff 2-3 = %lf V"%((ADC_Value[2]-ADC_Value[3])*5.0/0x7fffff))
        print ("\33[11A")

        
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
