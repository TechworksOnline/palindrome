import csv
#changes Made
csvf = 'Palindrome.csv'
with open(csvf, 'r') as f1:
    last_line = f1.readlines()[-1]
    print(last_line)
fn = int(last_line.split(',')[0])
count = 0
itera = 0
nf = 0
csvheader = ['Number', 'Result', 'Result_Length', 'Iterations']
csvfi = open(csvf, 'a', newline='')
csvwriter = csv.DictWriter(csvfi, fieldnames=csvheader)


def send(fn, a, count):
    header = ['Number', 'Result', 'Result_length', 'Iterations']
    with open(csvf, 'a', newline='') as filedata:
        writer = csv.DictWriter(filedata, fieldnames=header)
        writer.writerow({'Number': fn, 'Result': a, 'Result_length': len(a), 'Iterations': count})


# send(1,1,1)
def add(a):
    global count
    rn = int(str(a)[::-1])
    count = count + 1
    return a + rn


def check(a):
    # print("Checking ",a)
    global nf
    global csvwriter
    if a == int(str(a)[::-1]):
        # print ("Found Lychrel",fn,"Has a reults of", a, "and", count,"Iterations")

        if count > 280:
            print("FOUND HIGH LIMIT #########################################", fn)
            csvwriter.writerow({'Number': fn, 'Result': a, 'Result_Length': len(str(a)), 'Iterations': count})
        elif count > 80:
            print("Adding", fn, "to CSV with length of:", len(str(a)), "And", count, "Iterations")
            csvwriter.writerow({'Number': fn, 'Result': a, 'Result_Length': (len(str(a))), 'Iterations': count})
        # send(fn,a,count)
        nf = 0
        csvfi.flush()
        return


def run(fn):
    global nf

    # print(a1)
    # print(a2)
    # print(fn)

    if count > 290:
        # print ("Result Length",len(str(fn)))
        # print ("Iterations", count, "for number",fn)
        # nf = fn # Use this to bypass limit
        nf = 0
        return nf
    # print(str(fn)[len(str(fn))-1], str(fn)[0])
    # print(str(fn)[len(str(fn))-1] == str(fn)[0])
    if str(fn)[len(str(fn)) - 1] == str(fn)[0]:
        a1 = str(fn)[:-20]
        # arev = str(fn)[::-1][:-10]
        a2 = str(fn)[::-1][:-20]
        if a1 == a2:
            # print ("Matching now Checking")
            check(fn)
        else:
            fn = add(fn)
            run(fn)
            # print (fn)
            return
    else:
        fn = add(fn)
        run(fn)
        # print (fn)
        return


while (True):
    # print (fn)
    count = 0

    if nf != 0:
        itera = itera + 1
        run(nf)
    else:
        run(fn)
        fn = fn + 1
