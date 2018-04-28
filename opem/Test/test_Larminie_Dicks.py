# -*- coding: utf-8 -*-
'''
>>> from opem.Static.Larminie_Dicks import *
>>> E0=1.178
>>> A=0.0587
>>> B=0.0517
>>> RM=0.0018
>>> i_0=0.00654
>>> i_L=100
>>> i_n=0.23
>>> N=23
>>> Vcell_Calc(E0=E0, i=1,i_0=i_0,i_n=i_n,i_L=i_L,R_M=RM,A=A,B=B)
0.8677440917797067
>>> Vcell_Calc(E0=None, i=1,i_0=i_0,i_n=i_n,i_L=i_L,R_M=RM,A=A,B=B)
[Error] Vcell Calculation Error (E0:None, i:1, i_0:0.00654, i_n:0.23, i_L:100, R_M:0.0018, A:0.0587, B:0.0517)
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod={}, TestMode=True,PrintMode=False)
>>> Larminie_Dicks_Data["Status"]
False
>>> Test_Vector={"A":0.0587,"E0":1.178,"B":0.0517,"RM":0.0018,"i_0":0.00654,"i_L":100.0,"i_n":0.23,"N":23,"i-start":0.1,"i-stop":4,"i-step":0.1,"Name":"test3"}
>>> Larminie_Dicks_Data=Static_Analysis(InputMethod=Test_Vector, TestMode=True)
###########
Larminie-Dicks-Model Simulation
###########
Analyzing . . .
I : 0.1
PEM Efficiency : 0.6070918465825977
Power : 0.09470632806688527 W
Power-Stack : 2.178245545538361 W
Power-Thermal : 0.650754454461639 W
VStack : 21.78245545538361 V
Vcell : 0.9470632806688526 V
###########
I : 0.2
PEM Efficiency : 0.596983288796134
Power : 0.18625878610439384 W
Power-Stack : 4.2839520804010585 W
Power-Thermal : 1.3740479195989417 W
VStack : 21.41976040200529 V
Vcell : 0.9312939305219692 V
###########
I : 0.3
PEM Efficiency : 0.5889668542476844
Power : 0.27563648778791633 W
Power-Stack : 6.339639219122075 W
Power-Thermal : 2.1473607808779245 W
VStack : 21.132130730406917 V
Vcell : 0.9187882926263877 V
###########
I : 0.4
PEM Efficiency : 0.5823143704480743
Power : 0.3633641671595984 W
Power-Stack : 8.357375844670763 W
Power-Thermal : 2.958624155329237 W
VStack : 20.893439611676907 V
Vcell : 0.908410417898996 V
###########
I : 0.5
PEM Efficiency : 0.576622053314997
Power : 0.4497652015856977 W
Power-Stack : 10.344599636471047 W
Power-Thermal : 3.8004003635289525 W
VStack : 20.689199272942094 V
Vcell : 0.8995304031713954 V
###########
I : 0.6
PEM Efficiency : 0.5716425142657562
Power : 0.5350573933527478 W
Power-Stack : 12.3063200471132 W
Power-Thermal : 4.6676799528867985 W
VStack : 20.510533411855334 V
Vcell : 0.8917623222545797 V
###########
I : 0.7
PEM Efficiency : 0.5672131517182866
Power : 0.6193967616763688 W
Power-Stack : 14.246125518556482 W
Power-Thermal : 5.556874481443514 W
VStack : 20.35160788365212 V
Vcell : 0.884852516680527 V
###########
I : 0.8
PEM Efficiency : 0.5632213484876261
Power : 0.7029002429125574 W
Power-Stack : 16.16670558698882 W
Power-Thermal : 6.465294413011179 W
VStack : 20.208381983736025 V
Vcell : 0.8786253036406967 V
###########
I : 0.9
PEM Efficiency : 0.5595858755325545
Power : 0.7856585692477064 W
Power-Stack : 18.070147092697248 W
Power-Thermal : 7.390852907302754 W
VStack : 20.07794121410805 V
Vcell : 0.8729539658307849 V
###########
I : 1.0
PEM Efficiency : 0.5562462126792992
Power : 0.8677440917797067 W
Power-Stack : 19.958114110933252 W
Power-Thermal : 8.331885889066747 W
VStack : 19.958114110933252 V
Vcell : 0.8677440917797067 V
###########
I : 1.1
PEM Efficiency : 0.5531560572234717
Power : 0.9492157941954775 W
Power-Stack : 21.831963266495983 W
Power-Thermal : 9.287036733504017 W
VStack : 19.847239333178166 V
Vcell : 0.8629234492686159 V
###########
I : 1.2
PEM Efficiency : 0.5502791922121564
Power : 1.0301226478211567 W
Power-Stack : 23.692820899886605 W
Power-Thermal : 10.255179100113395 W
VStack : 19.74401741657217 V
Vcell : 0.858435539850964 V
###########
I : 1.3
PEM Efficiency : 0.5475867544887774
Power : 1.1105059381032407 W
Power-Stack : 25.541636576374536 W
Power-Thermal : 11.235363423625465 W
VStack : 19.647412751057335 V
Vcell : 0.8542353370024928 V
###########
I : 1.4
PEM Efficiency : 0.5450553693735705
Power : 1.190400926711878 W
Power-Stack : 27.379221314373194 W
Power-Thermal : 12.226778685626805 W
VStack : 19.55658665312371 V
Vcell : 0.85028637622277 V
###########
I : 1.5
PEM Efficiency : 0.5426658416714328
Power : 1.2698380695111529 W
Power-Stack : 29.206275598756516 W
Power-Thermal : 13.228724401243484 W
VStack : 19.47085039917101 V
Vcell : 0.8465587130074352 V
###########
I : 1.6
PEM Efficiency : 0.5404022150580957
Power : 1.348843928785007 W
Power-Stack : 31.02341036205516 W
Power-Thermal : 14.24058963794484 W
VStack : 19.389631476284475 V
Vcell : 0.8430274554906293 V
###########
I : 1.7
PEM Efficiency : 0.5382510820424253
Power : 1.427441869576512 W
Power-Stack : 32.83116300025978 W
Power-Thermal : 15.261836999740217 W
VStack : 19.312448823682224 V
Vcell : 0.8396716879861836 V
###########
I : 1.8
PEM Efficiency : 0.536201068437617
Power : 1.5056526001728283 W
Power-Stack : 34.63000980397505 W
Power-Thermal : 16.29199019602495 W
VStack : 19.238894335541694 V
Vcell : 0.8364736667626824 V
###########
I : 1.9
PEM Efficiency : 0.5342424419218519
Power : 1.583494597856369 W
Power-Stack : 36.420375750696486 W
Power-Thermal : 17.330624249303508 W
VStack : 19.168618816156048 V
Vcell : 0.833418209398089 V
###########
I : 2.0
PEM Efficiency : 0.532366810486187
Power : 1.6609844487169034 W
Power-Stack : 38.20264232048878 W
Power-Thermal : 18.37735767951122 W
VStack : 19.10132116024439 V
Vcell : 0.8304922243584517 V
###########
I : 2.1
PEM Efficiency : 0.5305668870842597
Power : 1.738137122088035 W
Power-Stack : 39.97715380802481 W
Power-Thermal : 19.431846191975197 W
VStack : 19.03673990858324 V
Vcell : 0.8276843438514452 V
###########
I : 2.2
PEM Efficiency : 0.5288363037744284
Power : 1.8149661945538385 W
Power-Stack : 41.74422247473829 W
Power-Thermal : 20.49377752526172 W
VStack : 18.97464657942649 V
Vcell : 0.8249846338881083 V
###########
I : 2.3
PEM Efficiency : 0.527169463367337
Power : 1.891484034562005 W
Power-Stack : 43.504132794926115 W
Power-Thermal : 21.562867205073875 W
VStack : 18.914840345620053 V
Vcell : 0.8223843628530457 V
###########
I : 2.4
PEM Efficiency : 0.5255614198480028
Power : 1.9677019559109223 W
Power-Stack : 45.257144985951214 W
Power-Thermal : 22.638855014048787 W
VStack : 18.857143744146338 V
Vcell : 0.8198758149628843 V
###########
I : 2.5
PEM Efficiency : 0.5240077811244296
Power : 2.0436303463852754 W
Power-Stack : 47.00349796686133 W
Power-Thermal : 23.721502033138655 W
VStack : 18.801399186744536 V
Vcell : 0.8174521385541103 V
###########
I : 2.6
PEM Efficiency : 0.5225046292799733
Power : 2.1192787763595717 W
Power-Stack : 48.74341185627015 W
Power-Thermal : 24.810588143729856 W
VStack : 18.74746609856544 V
Vcell : 0.8151072216767583 V
###########
I : 2.7
PEM Efficiency : 0.52104845467996
Power : 2.194656091111992 W
Power-Stack : 50.47709009557581 W
Power-Thermal : 25.905909904424192 W
VStack : 18.695218553916966 V
Vcell : 0.8128355893007376 V
###########
I : 2.8
PEM Efficiency : 0.5196361011410657
Power : 2.269770489784175 W
Power-Stack : 52.20472126503602 W
Power-Thermal : 27.007278734963975 W
VStack : 18.644543308941437 V
Vcell : 0.8106323177800625 V
###########
I : 2.9
PEM Efficiency : 0.5182647200068938
Power : 2.3446295933111876 W
Power-Stack : 53.926480646157316 W
Power-Thermal : 28.11451935384268 W
VStack : 18.59533815384735 V
Vcell : 0.8084929632107544 V
###########
I : 3.0
PEM Efficiency : 0.5169317314482642
Power : 2.4192405031778765 W
Power-Stack : 55.64253157309116 W
Power-Thermal : 29.22746842690884 W
VStack : 18.54751052436372 V
Vcell : 0.8064135010592922 V
###########
I : 3.1
PEM Efficiency : 0.515634791665824
Power : 2.4936098524959247 W
Power-Stack : 57.35302660740627 W
Power-Thermal : 30.345973392593724 W
VStack : 18.500976324969766 V
Vcell : 0.8043902749986854 V
###########
I : 3.2
PEM Efficiency : 0.514371764946645
Power : 2.5677438506136525 W
Power-Stack : 59.05810856411401 W
Power-Thermal : 31.469891435885998 W
VStack : 18.455658926285626 V
Vcell : 0.8024199533167663 V
###########
I : 3.3
PEM Efficiency : 0.5131406997374682
Power : 2.6416483222484866 W
Power-Stack : 60.75791141171519 W
Power-Thermal : 32.5990885882848 W
VStack : 18.411488306580363 V
Vcell : 0.8004994915904505 V
###########
I : 3.4
PEM Efficiency : 0.5119398080610783
Power : 2.7153287419559593 W
Power-Stack : 62.452561064987066 W
Power-Thermal : 33.73343893501293 W
VStack : 18.36840031323149 V
Vcell : 0.7986261005752822 V
###########
I : 3.5
PEM Efficiency : 0.5107674477304784
Power : 2.788790264608412 W
Power-Stack : 64.14217608599348 W
Power-Thermal : 34.872823914006524 W
VStack : 18.326336024569564 V
Vcell : 0.7967972184595463 V
###########
I : 3.6
PEM Efficiency : 0.5096221069165698
Power : 2.862037752443456 W
Power-Stack : 65.82686830619949 W
Power-Thermal : 36.017131693800515 W
VStack : 18.285241196166524 V
Vcell : 0.7950104867898489 V
###########
I : 3.7
PEM Efficiency : 0.5085023907052405
Power : 2.935075799150648 W
Power-Stack : 67.50674338046491 W
Power-Thermal : 37.16625661953508 W
VStack : 18.24506577850403 V
Vcell : 0.7932637295001752 V
###########
I : 3.8
PEM Efficiency : 0.5074070093438323
Power : 3.007908751390238 W
Power-Stack : 69.18190128197547 W
Power-Thermal : 38.32009871802452 W
VStack : 18.205763495256704 V
Vcell : 0.7915549345763785 V
###########
I : 3.9
PEM Efficiency : 0.5063347679284521
Power : 3.080540728076703 W
Power-Stack : 70.85243674576417 W
Power-Thermal : 39.47856325423582 W
VStack : 18.167291473272865 V
Vcell : 0.7898822379683854 V
###########
Done!

'''