# coding: utf-8

# flake8: noqa

# import all apis into this package
# if you have many ampis here with many many models used in each api this may
# raise a RecursionError
# to avoid this, import only the api that you directly need like:
# from .api.pet_api import PetApi
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

# import apis into api package
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.api.users_api import UsersApi
