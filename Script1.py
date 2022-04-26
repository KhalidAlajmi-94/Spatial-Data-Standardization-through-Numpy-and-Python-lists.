import arcpy,numpy

arcpy.env.workspace=r"C:\Khalid\Exam_05\Exam_05.gdb"
aFC = "LandParcels"
aQuery= '"Zone" = \'Zone D\''

arr06 = arcpy.da.FeatureClassToNumPyArray(aFC,['TaxValue06'],aQuery)
aSQR = [numpy.square(anitem) for anitem in arr06["TaxValue06"]]
aSum= numpy.sum(aSQR)
Asqrt= numpy.sqrt(aSum)
print [anitem/Asqrt for anitem in arr06["TaxValue06"]]


