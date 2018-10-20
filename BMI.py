tinggi = input('Masukkan tinggi anda dalam m:  ')
berat = input('Masukkan berat badan anda dalam Kg: ')
height = float (tinggi) * float (tinggi)

BMI = int (berat)/float (height)

if BMI<15:
    print("Anda termasuk dalam kategori Very severely underweight ")
    
elif BMI>=15 and  BMI<=16:
    print ("Anda termasuk dalam kategori Severely underweight ")
    
elif BMI>=16 and BMI<=18.5:
    print("Anda termasuk dalam kategori Underweight ")

elif  BMI>=18.5 and BMI<=25:
    print("Anda termasuk dalam kategori Normal (healthy weight) ")
    
elif BMI>=25 and BMI<=30:
    print("Anda termasuk dalam kategori Overweight")
    
elif BMI>=30 and BMI<=35:
    print("Anda termasuk dalam kategori Moderately obese")
    
elif BMI>=35 and BMI<=40:
    print("Anda termasuk dalam kategori Severely obese")
    
else:
    print("Anda termasuk dalam kategori Very Severely obese")
    
    





