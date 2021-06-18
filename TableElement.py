
# <el-table :data="tableData" style="width: 100%">
#         <el-table-column prop="health_code" label="" width="130"/>
#         </el-table-column>

tableData ='tableData'
allItem =   {"ten":'Tên',"tuoi":'Tuổi',"stt":'STT'}            
          
print(allItem)
Out='<el-table :data="'+tableData+'" style="width: 100%"> '
data = tableData+ ':{'
for item in allItem.keys():
    data+= allItem[item] + ":''," 
    Out += '<el-table-column prop="health_code" label=" '+allItem[item] +' " width="130"/> '
data += '},'
Out += '</el-table> '
print('############ Out ######')
print(Out)

print('############ data ######')
print(data)
