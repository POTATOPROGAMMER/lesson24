student_data={'id1':{"name":["sarah"],'class':['V'], 'subject_integration':['math','english','science']},
'id2':{"name":["david"],'class':['V'], 'subject_integration':['math','english','science']},
'id3':{"name":["sara"],'class':['V'], 'subject_integration':['math','english','science']},
'id4':{"name":["surya"],'class':['V'], 'subject_integration':['math','english','science']}}
result={}
for key,value in student_data.items():
    if value not in result.values():
     result[key]=value
print(result)