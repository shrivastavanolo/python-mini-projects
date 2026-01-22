def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def main():
    gen = infinite_sequence()

    for i in gen:
        print(i)  #Continues printing infinite series without memoryError
        if i==100:
            break

    print(next(gen)) #0
    print(next(gen)) #1
    gen.close()

if __name__ =="__main__":
    main()
