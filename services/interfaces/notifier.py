from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def can_notify(self, task): pass

    @abstractmethod
    def notify(self, task): pass
