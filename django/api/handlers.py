from piston.handler import BaseHandler
from web.models import Event

class EventHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Event

   def read(self, request, event_id=None):
      base = Event.objects
      
      if blogpost_id:
         return base.get(pk=event_id)
      else:
         return base.all() 
