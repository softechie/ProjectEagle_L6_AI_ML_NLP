import csv

with open('weather.csv','w') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
    filewriter.writerow(['Jan',58,42,74,22.2,95])
    filewriter.writerow(['Feb',61,45,78,26,3.02])
    filewriter.writerow(['Mar',65,48,84,25,2.34])
    filewriter.writerow(['Apr',67,50,92,28,1.02])
    filewriter.writerow(['May',71,53,98,35,0.48])
    filewriter.writerow(['Jun',75,56,107,41,0.11])
    filewriter.writerow(['Jul',77,58,105,44,0.0])
    filewriter.writerow(['Aug',77,59,102,43,0.03])
    filewriter.writerow(['Sep',77,57,103,40,0.17])
    filewriter.writerow(['Oct',73,54,96,34,0.81])
    filewriter.writerow(['Nov',64,48,84,30,1.7])
    filewriter.writerow(['Dec',58,42,73,21,2.56])
	 
	 
	                           