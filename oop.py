# class variables are variables that are shared among all instances of a class Class
# instance variables can be unique to the instance of the class
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f_handler = logging.FileHandler('class.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
f_handler.setFormatter(formatter)
logger.addHandler(f_handler)
s_handler = logging.StreamHandler()
s_handler.setFormatter(formatter)
logger.addHandler(s_handler)


class Employee:
	raise_amt = 1.04 #class variable
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	# a method can be made an atrribute by placing the property decorator
	# on it
	@property
	def email(self):
		return '{}.{}@company.com'.format(self.first, self.last)
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amt)

	# setting a class method is done using a decorator called classmethod
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	# using a class method as a generator of class object
	@classmethod
	def from_string(cls, emp_str):
		# unpacking the string
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	# static methods are methods that have literary connection to the class
	# but don't take neither the class nor instance as an argument within it
	 # they are like a normal function and are created in the class using the
	 # @staticmethod decorator
	# attributes can also be set from a particular method using the setter decorator
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last


# INHERITANCE: this is creation of a subclass inheriting the attributes of the parent class

class Developer(Employee):
	def __init__(self, first, last, pay, prog_lang):
		# making the parent class handle some of the argumment of the __init__()method
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


# logger.info(help(Developer))
emp_1 = Employee('Matthew', 'Balogun', 3000)
# Employee.raise_amt = 120.89

# # emp_1.apply_raise()
# logger.info(emp_1.email)
# logger.info(emp_1.pay)
# logger.info(emp_1.fullname)
emp_1.fullname = 'James Rodriguez'
logger.info(emp_1.email)
logger.info(emp_1.pay)
logger.info(emp_1.fullname)

# Employee.set_raise_amt(90)
# logger.info(emp_1.raise_amt)

# emp_1_str = 'Joel-Edwards-50000'
# new_emp = Employee.from_string(emp_1_str)
# logger.info(new_emp.email)
# logger.info(new_emp.fullname
