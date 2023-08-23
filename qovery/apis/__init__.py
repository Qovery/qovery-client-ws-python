
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from qovery.api.deployment_api import DeploymentApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from qovery.api.deployment_api import DeploymentApi
from qovery.api.logs_api import LogsApi
from qovery.api.service_metrics_api import ServiceMetricsApi
from qovery.api.service_status_api import ServiceStatusApi
