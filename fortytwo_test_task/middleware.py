from hello.models import RequestHistory


class HistoryMiddleware(object):
    def process_request(self, request):
        self.h = RequestHistory()
        self.h.url = request.path
        self.h.post = request.POST
        self.h.get = request.GET
        #self.h.meta = request.META
        self.h.save()
        return None
