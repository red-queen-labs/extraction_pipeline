import pickle
'''
sample_dicts = [{"headers": ["aa", "bb", "cc"]}, 
                {"headers": ["dd", "ee", "ff"]},
                {"headers": ["gg", "hh", "ii"]}]
'''
labelhelper_instance_filename = "labelhelper_instance.pickle"

class Label_Helper:
    def load_Data(self, labelhelper_instance_filename):
        instance_filehandler = open(labelhelper_instance_filename, "rb")
        self = pickle.load(instance_filehandler)
        instance_filehandler.close()
        return self

    def save_Data(self, labelhelper_instance_filename):
        instance_filehandler = open(labelhelper_instance_filename, "wb")
        pickle.dump(self, instance_filehandler)
        instance_filehandler.close()

    def __init__(self, labelhelper_instance_filename, tables_dict, index = 0):
        if tables_dict == None or index == None:
            #self.tables_dict = []
            #self.index = 0
            self = self.load_Data(labelhelper_instance_filename)
        else:
            self.tables_dict = tables_dict
            self.index = index

    def label_tables(self):
        retried = False
        error = False
        if self.index == len(self.tables_dict):
            self.index = 0
        while self.index < len(self.tables_dict) and not error:
            print(self.tables_dict[self.index]["headers"])
            validity_value = input()
            
            # 1 == True
            if validity_value == "1":
                self.tables_dict[self.index]["label"] = "True"
                retried = False
            # 2 == False
            elif validity_value == "2":
                self.tables_dict[self.index]["label"] = "False"
                retried = False
            # 3 == Undo
            elif validity_value == "3" and not retried:
                self.index -= 1
                retried = True
            # 4 == Skip
            elif validity_value == "4" or retried:
                retried = False
            else:
                self.save_Data(labelhelper_instance_filename)
                break
            self.index += 1

sample_dicts = None
index = None
'''
data_labeler = Label_Helper(labelhelper_instance_filename, sample_dicts, index)
print(data_labeler.index)
print(data_labeler.tables_dict)
data_labeler.label_tables()
'''
data_labeler = Label_Helper(labelhelper_instance_filename, sample_dicts, index)
data_labeler = data_labeler.load_Data(labelhelper_instance_filename)
print(data_labeler.index)
print(data_labeler.tables_dict)
data_labeler.label_tables()


