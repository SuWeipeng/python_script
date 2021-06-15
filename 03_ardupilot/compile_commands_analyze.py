import json,re

inc_pattern = r'^-I\.+'
src_pattern = r'.*\.c[xp]*$'
def_pattern = r'^-D.*'
inc_dict    = {}
src_dict    = {}
src_cpp     = []
src_c       = []
define      = []
include     = []
with open('compile_commands.json', 'r') as f:
    data = json.load(f)
    key_list = []
    for i in range(len(data)):
        for j in range(len(data[i].keys())):
            if list(data[i].keys())[j] not in key_list:
                key_list.append(list(data[i].keys())[j])
    if len(key_list) == 3:
        for n in range(len(data)):
            for i in data[n].get(key_list[1]):
                # find inc
                inc_prog = re.compile(inc_pattern)
                if inc_prog.match(i) != None:
                    if i not in include:
                        include.append(i)
                    if(inc_dict.get(i)) == None:
                        inc_dict[i] = 1
                    else:
                        inc_dict[i] = inc_dict.get(i) + 1
                # find src
                src_prog = re.compile(src_pattern)
                if src_prog.match(i) != None:
                    suffix = i.split(".")[-1]
                    if suffix == "cpp":
                        if(src_dict.get("cpp")) == None:
                            src_dict["cpp"] = 1
                        else:
                            src_dict["cpp"] += 1
                        src_cpp.append(i)
                    elif suffix == "c":
                        if(src_dict.get("c")) == None:
                            src_dict["c"] = 1
                        else:
                            src_dict["c"] += 1
                        src_c.append(i)
                # find define
                def_prog = re.compile(def_pattern)
                if def_prog.match(i) != None:
                    if i not in define:
                        define.append(i)

        src_cpp.sort()
        src_c.sort()
        define.sort()
        include.sort()

        file_cpp = "src_cpp.txt"
        file     = open(file_cpp,"w",encoding='utf-8')
        for i in src_cpp:
            file.write(i)
            file.write("\n")
        file.close()

        file_c = "src_c.txt"
        file     = open(file_c,"w",encoding='utf-8')
        for i in src_c:
            file.write(i)
            file.write("\n")
        file.close()

        file_def = "define.txt"
        file     = open(file_def,"w",encoding='utf-8')
        for i in define:
            file.write(i)
            file.write("\n")
        file.close()

        file_inc = "include.txt"
        file     = open(file_inc,"w",encoding='utf-8')
        for i in include:
            file.write(i)
            file.write("\n")
        file.close()

        inc_dict_key_list = list(inc_dict.keys())
        for i in range(len(inc_dict)):
            print("[%d] "%inc_dict.get(inc_dict_key_list[i])
                  + inc_dict_key_list[i])
        print(src_dict)