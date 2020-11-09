from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

### Now we can call the .replace() method on a python string
### to look for a certain value and replace it with another.


##### One way to register (without using decorator above): #####

# register.filter('cut',cut)

## ^ The string is what you're calling the method when it's
## inside a template tag. Second arg is the name of the
## function itself.
