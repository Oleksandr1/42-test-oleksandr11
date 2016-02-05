from hello.models import RequestHistory
class HistoryMiddleware(object):
    def process_request(self, request):
        h = RequestHistory()
        h.url = request.path
        h.post = request.POST
        h.get = request.GET
        h.meta = request.META
        h.save()
        return None
