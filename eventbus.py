from subscriber import subscriber
from typing import Union, Callable, Any, Iterable
subscriber_t = Union[subscriber, Callable[str, Any]]


class eventbus(object):
    """
    message passer/event bus
    """

    def __init__(self):
        self._channels: dict[str, set] = dict()

    @property
    def channels(self) -> Iterable[str]:
        return self.channels.keys()

    def subscribe(self, to: str, who: subscriber_t) -> None:
        """
        Add a subscriber to be notified of messages on the specified channel.
        """
        if to not in self.subscribers:
            self.subscribers[to] = set()

        self.subscribers[to].add(who)

    def unsubscribe(self, frm: str, who: subscriber_t) -> None:
        """
        Remove a subscriber from the specified channel
        """
        if frm in self.subscribers and who in self.subscribers[frm]:
            self.subscribers[frm].remove(who)

    def send_msg(self, to: str, what: Any) -> None:
        """
        Send a message to all subscribers of a channel.
        """
        if to in self._channels:
            for sub in self._channels[to]:
                if isinstance(sub, subscriber):
                    sub.notify(to, what)

                else:
                    sub(to, what)
