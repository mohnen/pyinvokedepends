class Template(object):
  """
  A very stupid example class, mainly for showing documentation generation.
  """
  def say_hello(self, name="Christophe"):
    """This function says hello.
    Accepts an optional name and formats a salutation given that name.
    Args:
      name: A optional string as name of some nice person to say hello to.
    Returns:
      A personalized salutation in the form of a string.
    """
    return "hello {0}".format(name)
