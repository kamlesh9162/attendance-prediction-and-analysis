# attendence-prediction-and-analysis
Here you can analys the attendce of students in graphical format which has the all records. You can predict the attendence for next upcoming classes that how much classes you should attend to get a certain attendence target.
The code file and excel file should be in the same folder.

att = np.array([round(df.at[n-1,'Jan \n%'],2),round(df.at[n-1,'Feb %'],2),round(df.at[n-1,'March %'],2),round(df.at[n-1,'April %'],2),round(df.at[n-1,'May%'],2),round(df.at[n-1,'Total'],2)])

In this above line, { 'jan \n%', 'Feb %', 'March %', 'April %',  'May %', 'Total' } are for precentage attendence of the months respectively.
You can change this according to your excel sheet.

For help, have a look to the 'attendence.xlsx'.
