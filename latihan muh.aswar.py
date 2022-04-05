
#Example class
class Example:
    def _init_(self):
        attr1 = 10
#Instance of class
example = Example()
#Dynamic attributes
attributes_to_add = ['attr2', 'attr3', 'attr4']
#Add these attributes dynamically
for x in range(len(attributes_to_add)):
    setattr(example, attributes_to_add[x], x)
