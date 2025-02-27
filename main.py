from linked_list import LinkedList

def main():
    llist = LinkedList()

    llist.insert_at_end('a')
    llist.print_linked_list()
    print()
    print()
    print()
    llist.insert_at_end('b')
    llist.insert_at_beginning('c')
    llist.insert_at_end('d')
    llist.insert_at_index('g', 2)

    llist.print_linked_list()

if __name__ == "__main__":
    main()