
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from qovery-ws.api.cluster_status_api import ClusterStatusApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from qovery-ws.api.cluster_status_api import ClusterStatusApi
from qovery-ws.api.deployment_api import DeploymentApi
from qovery-ws.api.logs_api import LogsApi
from qovery-ws.api.service_list_pods_api import ServiceListPodsApi
from qovery-ws.api.service_metrics_api import ServiceMetricsApi
from qovery-ws.api.service_status_api import ServiceStatusApi
