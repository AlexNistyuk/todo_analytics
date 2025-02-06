from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_filters(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        raise NotImplementedError
