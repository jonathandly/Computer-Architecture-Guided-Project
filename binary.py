# bitwise operations
# if val1 is True and val2 is False:

#   AND ( & )
#   0 is False and 1 is True
#   A   B   A AND B
#   0   0      0
#   0   1      0
#   1   0      0
#   1   1      1

#   OR ( | )
#   A   B   A OR B
#   0   0      0
#   0   1      1
#   1   0      1
#   1   1      1

#   XOR ( ^ ) exclusive OR
#   A   B   A X-OR
#   0   0     0
#   0   1     1
#   1   0     1
#   1   1     0

#   NOT ( ~ )
#   A   NOT A
#   0   1
#   1   0

# SHIFTING
# A << some_number # Shift all bits in A by some amount to the left
# B >> some_number # Shift all bitns in B by some amount to the right

# examples
# 0b1110 >> 1 == 0b0111 # this is almost the same as dividing by 2 
# 0b1110 << 2 == 0b111000

# MASKING
#       vv extract these bits 0b01 == 1
x = 0b01001100
# SHIFT x by 3 to the right
y = x >> 3 # 0b00001001

# mask y with 0b00000011

z = y & 0b00000011

# given 0b10100010
# give me the first two bits