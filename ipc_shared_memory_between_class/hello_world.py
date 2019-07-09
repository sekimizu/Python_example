import a
import b

def main():
    my_a = a.a()
    logger = my_a.getLogger()

    my_b = b.b()

    print("main > start operation...")
    my_b.operation("123", logger)
    my_b.operation("456", logger)
    my_b.operation("789", logger)

    print("main > start print_log...")
    my_a.print_log()

    print("main > logger size is", len(logger))

if __name__ == '__main__':
    main()
