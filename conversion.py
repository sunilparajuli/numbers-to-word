# Hello World program in Python
    
number = 1234
no = round(number)
point = round(number - no, 2)*100
hundred = null
digit_1 = len(str(no))
i = 0
str_array = []

words = {'0':'', '1' : 'One', '2': 'Two', '3': 'Three', '4' : 'Four', '5' : 'Five', 
'6' :'Six', '7' : 'Seven', '8' : 'Eight', '9' : 'Nine', '10' : 'Ten', '11' : 'Eleven',
 '12' :'Twelve', '13' : 'Thirteen', '14' : 'Fourteen', '15' : 'Fifteen', '16' : 'Sixteen',
  '17' : 'Seventeen', '18' : 'Eighteen', '19' : 'Nineteen', '20' : 'Twenty', '30' : 'Thirty',
   '40' : 'Forty', '50' : 'Fifty', '60' : 'Sixty', '70' : 'Seventy', '80' : 'Eighty', '90': 'Ninety' }

digits = {'', 'Hundred', 'Thousand', 'Lakh', 'Crore', 'Arab', 'Kharab'}

while i < digit_1:
# 	divider = if(i==2): 10: 100
    if(i==2): 
        divider = 10 
    else:
        divider = 100
    number = math.floor(no % divider)
    no = math.floor(no / divider)
    i += (divider == 10) ? 1 : 2
    if(number):
		plural = ((counter = string.count(str_array)) && number > 9) ? 's' : null
		hundred = (counter ==1 && str_array[0]) ? ' and ' : null
		str_array [] = (number < 21) ? words[number]. " " . digits[counter] . plural . " " . hundred : words[math.floor(number/10) * 10] . " " . words[number % 10]. " ". digits[counter]. plural . " ". hundred
	else:
		str_array[] = null

str_array = list(np.flip(str_array))
result = join('', str_array)
points = (point) ? ". " . words[point/10]. " ". words[point = point % 10] : ' '
print result . "Rupees" . points . " Paisa Only."