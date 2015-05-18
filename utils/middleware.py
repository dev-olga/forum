import logging


class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        logging.exception('Exception handling request for ' + request.path)
        # logging.error('Exception handling request for ' + request.path)