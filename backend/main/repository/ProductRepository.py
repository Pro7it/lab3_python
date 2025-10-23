from main.repository.BaseRepository import BaseRepository
from main.models import *

class ActorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Actor)

class DirectorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Director)

class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)

class TheatreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Theatre)

class ScheduleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Schedule)

class PlayDirectorRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayDirector)

class PlayActorRepository(BaseRepository):
    def __init__(self):
        super().__init__(PlayActor)

class PlayRepository(BaseRepository):
    def __init__(self):
        super().__init__(Play)

class HallRepository(BaseRepository):
    def __init__(self):
        super().__init__(Hall)

class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Genre)

