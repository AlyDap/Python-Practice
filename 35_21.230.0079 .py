# Type Hint
# Type hint digunakan pada function untuk mengetahui tipe data argumen/paramater function

'''
def fungsi1(parameter):
print(parameter)
fungsi1(2)
fungsi1(2.5)
fungsi1("joni")
'''
import string
# menggunakan tye hint untuk mengetahui tipe data yang digunakan dalam fungsi


def fungsi2(parameter: int) -> int:
    output = 2**parameter
    return output


def fungsi3(parameter: string):
    print(parameter)


print(fungsi2(4))
fungsi3("ali")
fungsi3('''
halo guys
        saya siapa
   heheh
        ''')
