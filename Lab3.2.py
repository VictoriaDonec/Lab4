import sys
sys.stdout.write('задайте радіус')
bar = sys.stdin.readline()
foo = int(bar) ** 2 * 3.14
sys.stdout.write("площа поверхні = ")
sys.stdout.write(str(foo))
sys.stdout.write("\n" + 'задайте висоту')
bar1 = sys.stdin.readline()
foo1 = float(foo) * int(bar1)
sys.stdout.write("обʼєм циліндра = ")
sys.stdout.write(str(foo1))
