from main.repository.ProductRepository import *

class MainPoint:
    def __init__(self):
        self.actors = ActorRepository()
        self.directors = DirectorRepository()
        self.tickets = TicketRepository()
        self.theaters = TheatreRepository()
        self.schedules = ScheduleRepository()
        self.play_directors = PlayDirectorRepository()
        self.play_actors = PlayActorRepository()
        self.plays = PlayRepository()
        self.genres = GenreRepository()
        self.halls = HallRepository()