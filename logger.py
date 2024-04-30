import queue
import datetime


class Logger:

    class LogItem:
        def __init__(self, name: str, action: str, timestamp: datetime.datetime):
            self.name = name
            self.action = action
            self.timestamp = timestamp

    def __init__(self):
        """
        __log: The log that is displayed to the user
        __state: The current state of the drink_tracker, used to revert decision
        """
        self.__log = queue.LifoQueue()
        self.__state = queue.LifoQueue()

    def __peak_item(self) -> LogItem:
        #A bit ugly but there was no peak operation in queue
        item = self.__log.get()
        self.__log.put(item)
        return item

    def pop(self) -> LogItem:
        return self.__state.get()

    def push(self, item: LogItem) -> None:
        self.__log.put(item)
        self.__state.put(item)

    def log_message(self):
        item = self.__peak_item()
        return f"{item.timestamp}: {item.action} {item.name} \n"