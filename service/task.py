from dataclasses import dataclass

from handlers.schema.task import TaskSchema
from repository import TaskRepository, TaskCache


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache


    def get_tasks(self):
        if tasks := self.task_cache.get_tasks():
            return tasks
        else:
            tasks = self.task_repository.get_tasks()
            task_schema = [TaskSchema.model_validate(task) for task in tasks]  # преобразуем в pydantic
            self.task_cache.set_task(task_schema)
            return task_schema