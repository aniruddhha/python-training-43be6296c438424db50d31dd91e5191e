
from inheritance_basics import BadAgeException
from variable_annotations import fn_lg


class ImprovisedMain:
    def inheritance(self):
        age: int = int(input('Enter Age : '))
        
        if(age > 85):
            ex = BadAgeException('Age must be less that 85')
            ex.abc()
            ex.with_traceback(None)
            raise ex

    def variable_annotations(self):
        fn_lg()


if __name__ == '__main__':
    im = ImprovisedMain()
    im.variable_annotations()
