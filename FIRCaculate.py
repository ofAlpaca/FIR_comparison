import math

a = ['0.8984375', '0.40625', '0.90625', '0.1953125', '0.6796875', '-0.1171875', '0.671875', '0.03125', '-0.9609375', '-0.25', '0.7968750', '-0.1484375', '-0.6015625', '-0.3984375', '0.0703125', '0.8203125', '0.046875', '-0.3906250', '-0.9375', '0.4296875', '0.53125', '-0.8828125', '0.25', '-0.4765625', '-0.3828125', '0.0390625', '-0.1875', '0.78125', '0.140625', '0.1328125', '-0.21875', '0.3828125']
c = ['0.1328125', '-0.3203125', '0.1875', '-0.453125', '-0.90625', '0.671875', '-0.796875', '0.453125', '-0.125', '0.9921875', '0.1171875', '-0.0703125', '-0.1640625', '-0.578125', '-0.53125', '-0.375']
y = [] # float with quantization
Y = [] # float without quantization
f = [] # float with quantization except quantized to [6:10]

sum_1, sum_2, sum_3, sum_4, k = 0, 0, 0, 0, 0
print('\n{0:-^79}\n'.format('The output in [6:10] quantized size'))

for i in range(0,17):
    for j in a[i:i+4]:
        #print(j + ' x ' + c[k])
        j_f = math.floor(float(j)*(2**7))/(2**7)     # quantized to [1:7]
        c_f = math.floor(float(c[k])*(2**7))/(2**7)  # quantized to [1:7]
        mul = j_f * c_f
        mul_f = math.floor(mul*(2**12)) / 2**12      # quantized to [2:12]
        sum_1 += mul_f
        k += 1
    sum_1_f = math.floor(sum_1*(2**12))/2**12      # quantized to [4:12]

    for j in a[i+4:i+8]:
        #print(j + ' x ' + c[k])
        j_f = math.floor(float(j)*(2**7))/(2**7)     # quantized to [1:7]
        c_f = math.floor(float(c[k])*(2**7))/(2**7)  # quantized to [1:7]
        mul = j_f * c_f
        mul_f = math.floor(mul*(2**12)) / 2**12      # quantized to [2:12]
        sum_2 += mul_f
        k += 1
    sum_2_f = math.floor(sum_2*(2**12))/2**12      # quantized to [4:12]

    for j in a[i+8:i+12]:
       # print(j + ' x ' + c[k])
        j_f = math.floor(float(j)*(2**7))/(2**7)     # quantized to [1:7]
        c_f = math.floor(float(c[k])*(2**7))/(2**7)  # quantized to [1:7]
        mul = j_f * c_f
        mul_f = math.floor(mul*(2**12)) / 2**12      # quantized to [2:12]
        sum_3 += mul_f
        k += 1
    sum_3_f = math.floor(sum_3*(2**12))/2**12      # quantized to [4:12]

    for j in a[i+12:i+16]:
       # print(j + ' x ' + c[k])
        j_f = math.floor(float(j)*(2**7))/(2**7)     # quantized to [1:7]
        c_f = math.floor(float(c[k])*(2**7))/(2**7)  # quantized to [1:7]
        mul = j_f * c_f
        mul_f = math.floor(mul*(2**12)) / 2**12      # quantized to [2:12]
        sum_4 += mul_f
        k += 1
    sum_4_f = math.floor(sum_4*(2**12))/2**12      # quantized to [4:12]

    sum = sum_1_f + sum_2_f + sum_3_f + sum_4_f
    sum_f = math.floor(sum*(2**12)) / 2**12        # quantized to [6:12]
    sum_f_out = math.floor(sum_f*(2**10)) / 2**10  # quantized to [6:10]

    print('A{0}~A{1}:'.format(i, i+15) + '{0:>15} x 2^10 = {1}'.format(sum_f_out, sum_f_out*2**10) )

    sum_1, sum_2, sum_3, sum_4, k = 0, 0, 0, 0, 0
    y.append(sum_f_out)
    f.append(sum_f)
    sum_orgin, n = 0, 0


print('\n{0:-^79}\n'.format('Floating points operation for comparison'))

for i in range(0,17):
    for j in a[i:i+16]:
        sum_orgin += math.floor(float(j)*(2**7))/(2**7) * math.floor(float(c[n])*(2**7))/(2**7)
        n += 1
    print('A{0}~A{1}:'.format(i, i+15) + '{0:>20}'.format(sum_orgin) )
    Y.append(sum_orgin)
    sum_orgin, n = 0, 0
    
print('\n{0:-^79}\n'.format('SQNR'))

for i in range(0,17):
    idok = math.pow(Y[i],2) / math.pow((Y[i]-y[i]),2)
    sqnr = 10 * math.log10(idok)
    print('SQNR ==> ' + str(sqnr))

input()