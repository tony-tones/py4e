def computepay():
    oth = h - 40
    otr = r * 1.5
    return oth * otr 

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Pay:")
r = float(rate)


if h > 40 :
    computepay()
    p = 40 * r + computepay()
else:    
	p = h * r

print(p)