import os


def logger(ff):
    def fu():
        print("This is a Logger,修饰器！")
        ff()

    return fu


@logger
def tes1():
    print("This is the test1")


@logger
def test2():
    print("This is the test2")


pathnow=os.path

print('5555555555555555', pathnow)
tes1()

tes1()

test2()
