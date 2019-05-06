import yaml
def data(filename,keys):
    #pytest 调用时将项目文件下作为当前目录，所以选择路径时注意此时是./
    # 如果是在本.py文件调用函数就是../
    with open("./data/"+filename+".yaml","r",encoding="utf-8")as f:
        data_dict= yaml.load(f,Loader=yaml.FullLoader)[keys]
        data_list=list()
        # b=data.values()
        # print(b)
        data_list.extend(data_dict.values())
        return data_list
#         print(data_list)
# a = data("data","test_add_phone")
# print(a)
