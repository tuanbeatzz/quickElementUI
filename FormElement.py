import re
def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s

TenForm= 'formInput'
allItem =   [['Tên','Tuổi'],
            ['Nơi ở','CMND','Hộ chiếu','Số dân sinh'],
            ['Giới tính','Ngày sinh', 'Tháng sinh'],
            ['Địa chỉ','Quê quán']]

#create Form
form = ' <el-form style="margin: 12px" ref="form" :model="info" label-width="100px" > '
form_end = ' </el-form> '
row = '<el-row> '
row_end = '</el-row> '
# col = '<el-col :span="'+ str(int(24/len(hang)))+'">'
col_end = '</el-col> '
# form_item= '<el-form-item size="mini" label="'+hang +'">'
form_item_end= ' </el-form-item> '
# input_='<el-input style="width: 90%" v-model="'+TenForm+'.'+hang[i]+'" />'

Out=  form 
 # 'a:{c:'', b:'',}'
data = TenForm+ ':{'
for hang in allItem:
    Out +=row
    
    for cot in hang:
        Out +='<el-col :span="'+ str(int(24/len(hang)))+'"> '
        name_item = no_accent_vietnamese(cot.lower().replace(' ', '_'))
        data+= name_item + ":''," 
        Out += '<el-form-item size="mini" label="'+cot +'"> '
        Out += '<el-input style="width: 100%" v-model="'+TenForm+'.'+name_item+'" /> '
        Out += form_item_end
        Out +=col_end
    Out +=row_end    
data += '},'
Out= Out + form_end
print('############ Out ######')
print(Out)
print('############ data ######')
print(data)


# print(col)
# print(no_accent_vietnamese(('Xinhào').lower().replace(' ', '_')))