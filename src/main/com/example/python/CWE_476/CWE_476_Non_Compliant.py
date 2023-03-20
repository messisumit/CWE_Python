class NonComplaint:
    def directory(self):
        print("Within directory!")


obj = NonComplaint()
obj.directory()

obj = None
print(obj.directory())