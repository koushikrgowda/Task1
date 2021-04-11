XlsxWriter is a Python module for writing files in the XLSX file format. 
It can be used to write text, numbers, and formulas to multiple worksheets.


#import xlsxwriter module
import xlsxwriter



#Workbook() takes one, non-optional, argument,which is the filename that we want to create.
# The workbook object is then used to add new worksheet via the add_worksheet() method.
workbook = xlsxwriter.Workbook('nayan.xlsx')
worksheet = workbook.add_worksheet()


#declaring lists to write into excel,there is 3 lists suchs as filenames,triggers,timestamp.
File_names = ['ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000095',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000093',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000091',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000089',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000089',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000089',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000089',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000088',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000088',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000088',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000087',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000083',
'ADCAM-LOW_BP41328_20200630_054912_PDX-031-084_R-20-06-77-1337011_VBS_000082']

Triggers = ['LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING',
'LCA_LKA_STEERING']

Time_stamp = ['1593499956808946',
'1593499873694710',
'1593499812300334',
'1593499745470935',
'1593499740661040',
'1593499714031008',
'1593499729711416',
'1593499708541053',
'1593499698321242',
'1593499672781432',
'1593499671771773',
'1593499500653066',
'1593499470393507']

#Use the worksheet object to write column headers(filename,triggers,timestamp) via the write() method.

worksheet.write("A1","FileNames")
worksheet.write("B1","Triggers")
worksheet.write("C1","Timestamp")

#iterating through list and write it out row by row.incrementing the value of row by one with each iteratons.

for list in range(len(File_names)):
	worksheet.write(list+1,0,File_names[list])
	worksheet.write(list+1,1,Triggers[list])
	worksheet.write(list+1,2,Time_stamp[list])

#Finally, close the Excel file via the close() method.

workbook.close()