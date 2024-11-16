class ErrorSeat(Exception):
    def __init__(self, seat):
        super().__init__(f"un-available seat number{seat}. It need to be in range from 1-100")

class Ticket:
    def __init__(self, title, seat, price):
        self.title = title
        self.seat = seat
        self.price = price

    def display_info(self):
        return f"Film: {self.title}, Sit: {self.seat}, Price: {self.price} $"

class STicket(Ticket):
    def __init__(self, title, seat, price, discount=0):
        super().__init__(title, seat, price)
        self.discount = discount

    def display_info(self):
        info = super().display_info()
        if self.discount > 0:
            info += f" Discount: {self.discount}%"
        return info

class VIPticket(Ticket):
    def __init__(self, title, seat, price, lounge, drinks):
        super().__init__(title, seat, price)
        self.lounge = lounge
        self.drinks = drinks

    def display_info(self):
        info = super().display_info()
        info += f", VIP-zone: {'Yes' if self.lounge else 'No'}, Free drinks: {self.drinks}"
        return info

class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        try:
            if not (1 <= ticket.seat <= 100):
                raise ErrorSeat(ticket.seat)
            self.tickets.append(ticket)
        except ErrorSeat as e:
            print(e)
        except Exception as e:
            print("Error in ticket creation", e)

    def display_all_tickets(self):
        if not self.tickets:
            print("Don't have this ticket")
        else:
            for ticket in self.tickets:
                print(ticket.display_info())

cinema = Cinema()

ticket1 = STicket("film 1", 50, 120, discount=10)
ticket2 = VIPticket("film 2", 5, 300, lounge=True, drinks=2)
ticket3 = Ticket("film 3", 101, 100) 

cinema.add_ticket(ticket1)
cinema.add_ticket(ticket2)
cinema.add_ticket(ticket3)

cinema.display_all_tickets()
