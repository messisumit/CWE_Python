class Complaint:
    def directory(self):
        print("Within Directory!")


obj = Complaint()
obj.directory()

obj = None
if obj is not None:
    print(obj.directory())
else:
    print("Object is None")