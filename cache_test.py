from dogpile.cache import make_region
from dogpile.cache.proxy import ProxyBackend

import logging
log = logging.getLogger(__name__)

class LoggingProxy(ProxyBackend):
	def set(self, key, value):
		log.debug('setting cache key: %s' % key)
		print 'setting cache key: %s' % key
		self.proxied.set(key, value)

	def get(self, key):
		log.debug('getting cache key: %s' % key)
		print 'getting cache key: %s' % key
		return self.proxied.get(key)	

region = make_region().configure(
	'dogpile.cache.memory',
	expiration_time = 3600, wrap = [LoggingProxy])

@region.cache_on_arguments()
def add(a):
	return a+2

print add(3)
for i in [1,2,3]:
	print add(3)
import pdb; pdb.set_trace()
region.invalidate()
print "invalidated"
print add(3)			
