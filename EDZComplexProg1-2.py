# Eric Zarycki - CSC 145A
# The class EDZComplex can be used for carrying out different arithmetic operations on complex numbers.
# Reference 1: http://hplgit.github.io/primer.html/doc/pub/class/._class-solarized005.html 
# Used this reference to better understand __init__, __add__, and __mul__ methods
# Referece 2: https://github.com/NaruBeast/complex-numbers-package/blob/master/ccal.py
# Used this reference for some parts of the main() function, mostly user input

class EDZComplex():

  # Num_of_complex is initially set to 0
  __num_of_complex = 0

  # Init method setting the real and imag values and incrementing __num of complex
  def __init__(self, real, imag=0.0):
    self.real = real
    self.imag = imag
    EDZComplex.__num_of_complex += 1

  # Add method
  def __add__(self, number):
    return EDZComplex(self.real + number.real, self.imag + number.imag)

  # Multiplication method
  def __mul__(self, other):
    return EDZComplex(self.real * other.real - self.imag * other.imag,
    self.imag * other.real + self.real * other.imag)

  # Returns the object representation in string format
  def __repr__(self):
      return (str(self.real) + " + " + str(self.imag) + "i")

  # Decrements __num_complex when a FMCLComplex object is destroyed
  def __del__(self):
    EDZComplex.__num_of_complex -= 1

  # Class method
  def num_of_complex(cls):
    return EDZComplex.__num_of_complex


### Main Function 
def main():

  print("Your input must only contain integers!")
  print("---Enter first number---")

  # Here the user inputs the real and imaginary numbers into the EDZComplex for set 1
  a=int(input("Enter real part: "))
  b=int(input("Enter imaginary part: "))
  complex1 = EDZComplex(a,b)

  # Here the user inputs the real and imaginary numbers into the EDZComplex for set 2
  print("---Enter second number---")
  a=int(input("Enter real part: "))
  b=int(input("Enter imaginary part: "))
  complex2 = EDZComplex(a,b)	

  # Testing out addition method
  print("-----------------------------------")
  print("Addition:")
  print((complex1.__add__(complex2)))
  # Testing out multiplication method
  print("Multiplication:")
  print((complex1.__mul__(complex2)))

  # Shows the total complex numbers created
  print("---Complex numbers created---")
  print("Set 1: ")
  print(complex1.num_of_complex())
  print("Set 2: ")
  print(complex2.num_of_complex())

  # Test out the delete method
  complex2.__del__()
  print("***Complex number 2 was deleted***")

  # After destroying a FMCLComplex object, we call num_of_complex again
  print("Updated Complex numbers: ")
  print(complex1.num_of_complex())

  # Show off the string format
  print("Complex number 1 in final format: ")
  print(complex1.__repr__())

if __name__ == "__main__":
  main()