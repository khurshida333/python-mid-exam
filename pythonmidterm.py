class Star_Cinema:
    _hall_list = []  
    
    def entry_hall(self):
        Star_Cinema._hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, hall_no, rows, cols) -> None:
        self._seats = {}  
        self._show_list = []  
        self._rows = rows  
        self._cols = cols  
        self._hall_no = hall_no
        self.entry_hall()

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]

    def view_show_list(self):
        print("----------")
        for movie_info in self._show_list:
            print(movie_info)

    def book_seats(self, id, row, col):
        print("----------")
        if id in self._seats:
            if 0 <= row < self._rows and 0 <= col < self._cols:
                if self._seats[id][row-1][col-1] == 0:
                    self._seats[id][row-1][col-1] = 1
                    print(f"Seat ({row}, {col}) booked successfully for show ID {id}.")
                else:
                    print(f"Seat ({row}, {col}) is already booked for show ID {id}.")
            else:
                print(f"Seat ({row}, {col}) is invalid for show ID {id}.")
        else:
            print(f"Show ID {id} not found.")

    def view_available_seats(self, showid):
        print("----------")
        for i in self._show_list:
            if i[0] == showid:
                matrix = self._seats[showid]
                for row in matrix:
                    print(row)
            else:
                print("ID not found")


hall = Hall(1, 5, 5)
hall.entry_show(101, "joler gaan", "10:00 AM")
hall.entry_show(102, "joler gaan", "10:00 AM")

while True:
    print("\n|| Movie Theatre Management System ||")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")

    option = input("ENTER OPTION: ")

    if option == '1':
        hall.view_show_list()
    elif option == '2':
        showID = int(input("ENTER SHOW ID: "))
        hall.view_available_seats(showID)
    elif option == '3':
        showID = int(input("ENTER SHOW ID: "))
        Row = int(input("ENTER SEAT ROW: "))
        Col = int(input("ENTER SEAT COL: "))
        hall.book_seats(showID, Row, Col)
    elif option == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4")
