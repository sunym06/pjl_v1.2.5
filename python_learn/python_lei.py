class A(object):  #定义一个类        
	name='python' #类属性        
	def __init__(self): #实例属性                
		self.age=18
	def a_print(self): #实例方法            
		print('aaa')

	@classmethod  #类方法   
	def b_print(cls): #cls指代当前的类           
		print(cls.__name__)  #获取当前类名   

	@staticmethod  #静态方法   
	def c_print():
		print('static')

print(A.name) #调用类属性
A.b_print() #调用类方法
# print(A.age) 不可以调用实例属性
print(A().age) #匿名实例对象可以调用实例属性
a_obj=A() # 类对象　可以调用这个类中所有方法和属性
print(a_obj.age)
print(a_obj.name)
a_obj=A()  #在外部生成一个对象
a_obj.num=1000  #对 对象增加一个额外属性,并赋值
def func(a_obj): #再把这个对象传递到另一个方法中       
	print(a_obj.num) #这个方法中我就可以拿到这个对象，并用这个对象获取到这个对象额外添加       的数据
func(a_obj)

#可以在方法中传递数据
#一个类想要调用另一个类的方法和属性，有两种形式
# １.继承# 2.把另外一个对象传递到这个类中，在这个类中调用实例对象
#  把一个类当做是另一个类的属性，通过属性调用的方式调用另一个类的方法
class B(object):
	def __init__(self):
		self.a_obj=A() #把A对象直接作为Ｂ的属性       
	def func(self,a_obj):
		print(a_obj.num)
		a_obj.a_print()
b_obj=B()
b_obj.a_obj.a_print()
b_obj.a_obj.b_print
b_obj=B()
b_obj.func(a_obj)

