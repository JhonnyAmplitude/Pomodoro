from handlers.tasks import router as tasks_router
from handlers.ping import router as ping_ping_router


routers = [ping_ping_router, tasks_router]