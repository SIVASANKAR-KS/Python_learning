txt="95"
#txt="-95"
print(f"price is {int(txt):.2f} rupees")
print(f"price is {txt:<8} rupees")           ##uses 8 space if str < 8 then empty will be there
print(f"price is {txt:>8} rupees")
print(f"price is {txt:^8} rupees")
print(f"price is {int(txt):=8} rupees")      #if negative sign is present, 8 space btwn sign and integer
print(f"price is {int(txt):+} rupees")       # to show positive/negative sign
print(f"price is {int(txt):-} rupees")       #to show only negative