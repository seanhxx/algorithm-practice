x = int(input())
testcase = [int(input()) for i in range(x)]
for i in range(x):
    n = ''
    def generate0(n):
            n1 = ''.join([n,'0'])
            n2 = ''.join([n,'1'])
            if len(n) < testcase[i]:
                generate0(n1)
                generate1(n2)
            else:
                print(n)
    def generate1(n):
            n2 = ''.join([n, '1'])
            n1 = ''.join([n, '0'])
            if len(n) < testcase[i]:
                generate0(n2)
                generate1(n1)
            else:
                print(n)

    generate0(n)
    print('')


