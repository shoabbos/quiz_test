import datetime

from rest_framework.throttling import BaseThrottle

from quiz.models import Tenant, Request

from django.conf import settings

	def allow_request(self, request, view):

		now = datetime.datetime.now()
		api_key = request.META.get('HTTP_API_KEY')
		tenant = Tenant.objects.get(api_key=api_key)
		todays_requests = Request.objects.filter(tenant=tenant, requested_on__date=datetime.datetime.today())
		is_allowed = True
		delta = now - datetime.timedelta(seconds=10)

		if len(todays_requests) > settings.TODAY_REQ and todays_requests.filter(requested_on__gte=datetime.datetime.now() - datetime.timedelta(seconds=settings.SEC_REQ)):
			is_allowed = False

		if is_allowed:
			Request.objects.create(tenant=tenant, requested_on=now, requested_by=request.user, url=request.path)
		return is_allowed
