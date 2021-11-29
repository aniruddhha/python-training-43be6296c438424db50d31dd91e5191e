
from inheritance_basics import BadAgeException


class ImprovisedMain:
    def inheritance(self):
        age = int(input('Enter Age : '))

        if(age > 85):
            raise BadAgeException('Age must be less that 85')


if __name__ == '__main__':
    im = ImprovisedMain()
    im.inheritance()
