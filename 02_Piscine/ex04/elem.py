#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace('\n', '\n<br />\n').replace("'",'"')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        if None == content:
            self.content = []
        elif False == self.check_type(content):
            raise Elem.ValidationError
        elif type(content) != list:
            self.content = [content]
        else:
            self.content = []
            self.add_content(content)
        

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            self.result = '<'+self.tag
            if len(self.attr) > 0:
                self.result += self.__make_attr()
                self.result += '>'
            else:
                self.result += '>'
            if None != self.content and [''] != self.content:
                self.result += self.__make_content()
            self.result += '</'+self.tag+'>'
        elif self.tag_type == 'simple':
            self.result = '<'+self.tag
            if len(self.attr) > 0:
                self.result += self.__make_attr()
            self.result += '>'
        return self.result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            #separa por linhas
            if(len(str(elem)) != 0):
                result += str(elem) + '\n'
        # Adiciona espaços a cada linha e junta de novo
        result = "  ".join(content_formatted for content_formatted in result.splitlines(True))
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def run():
    print(Elem('html',{},[Elem('head',{},Elem('title',{},Text("'Hello ground!'"))),Elem('body',{},[Elem('h1',{},Text("'Oh no, not again!'")),Elem('img',{'src':"http://i.imgur.com/pfp3T.jpg"},None,'simple')])],'double'))

if __name__ == '__main__':
    run()
    