import invoice
#01
No1 = "01"
Pro1 = "Pen"
Qty1 = 20
Un1 = 500
AR1 = invoice.AmountKHR(Qty1, Un1)
AS1 = invoice.AmountUSD(AR1)
RR1 = invoice.RemainKHR(AR1)
print("-"*76)
print(invoice.output("No", "Product", "Qty","Unit", "Amount(KHR)", "Amount(USD)", "Remain(KHR)"))
print("-"*76)
print(invoice.output(No1, Pro1, Qty1, Un1, AR1, AS1, RR1))
print("-"*76)
#02
No2 = "02"
Pro2 = "Book"
Qty2 = 20
Un2 = 1500
AR2 = invoice.AmountKHR(Qty2, Un2)
AS2 = invoice.AmountUSD(AR2)
RR2 = invoice.RemainKHR(AR2)
print(invoice.output(No2, Pro2, Qty2, Un2, AR2, AS2, RR2))
print("-"*76)
#03
No3 = "03"
Pro3 = "Marker"
Qty3 = 15
Un3 = 2500
AR3 = invoice.AmountKHR(Qty3, Un3)
AS3 = invoice.AmountUSD(AR3)
RR3 = invoice.RemainKHR(AR3)
print(invoice.output(No3, Pro3, Qty3, Un3, AR3, AS3, RR3))
print("-"*76)
#04
No4 = "04"
Pro4 = "Phone"
Qty4 = 3
Un4 = 300000
AR4 = invoice.AmountKHR(Qty4, Un4)
AS4 = invoice.AmountUSD(AR4)
RR4 = invoice.RemainKHR(AR4)
print(invoice.output(No4, Pro4, Qty4, Un4, AR4, AS4, RR4))
print("-"*76)
print(invoice.output("", "", "", "Total:", invoice.total(AR1,AR2,AR3,AR4), invoice.total(AS1,AS2,AS3,AS4), invoice.total(RR1,RR2,RR3,RR4)))