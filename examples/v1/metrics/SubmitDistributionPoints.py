"""
Submit distribution points returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.distribution_point import DistributionPoint
from datadog_api_client.v1.model.distribution_points_payload import DistributionPointsPayload
from datadog_api_client.v1.model.distribution_points_series import DistributionPointsSeries

body = DistributionPointsPayload(
    series=[
        DistributionPointsSeries(
            metric="system.load.1.dist",
            points=[
                DistributionPoint(
                    [
                        datetime.now().timestamp(),
                        [1.0, 2.0],
                    ]
                ),
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_distribution_points(body=body)

    print(response)
