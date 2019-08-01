class Lls(object):
    no_inst = 0

    #def __int__(self):
    def __init__(self):
        print("hello")
        Lls.no_inst = Lls.no_inst + 1

    #@classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst

ik11 = Lls()
ik13 = Lls()
ik22 = Lls()


print ik11.get_no_of_instance()
print ik22.get_no_of_instance()
print Lls.get_no_of_instance()

class K1ls(object):
    no_inst = 0

    def __init__(self):
        print("hi")
        K1ls.no_inst = K1ls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst


ik1 = K1ls()
ik2 = K1ls()


print ik1.get_no_of_instance()
print ik2.get_no_of_instance()
print K1ls.get_no_of_instance()