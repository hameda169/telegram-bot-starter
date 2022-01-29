from telegram.ext import Updater
from threading import Lock


class CustomUpdater(Updater):
    def __init__(self, *args, **kwargs):
        self.__lock = Lock()
        super(CustomUpdater, self).__init__(*args, **kwargs)

    def custom_start_webhook(self):
        with self.__lock:
            if not self.running:
                self.running = True

                self.logger.debug('Updater thread started (webhook)')

                # Return the update queue so the main thread can insert updates
                return self.update_queue

    def handle_update(self, update):
        if not self.running:
            self.logger.debug('Updates ignored and will be pulled again on restart')
        else:
            self.dispatcher.process_update(update)
            self.last_update_id = update.update_id + 1
        return True
