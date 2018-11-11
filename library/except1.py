x=int(input('enter a digit:'))
y=int(input('enter a didgit dt u want to divide by:'))
try:
    print('result:',x/y)
except ValueError as VE:
    print('Please enter a valid divisor:',VE)

except ZeroDivisionError as ZD:
    print('dont enter ZERO as Divisor',ZD)
except TypeError as TE:
    print('enter digits:',TE)
else:
    print('exception didnt ran')
finally:
    print('program Ended finally')
