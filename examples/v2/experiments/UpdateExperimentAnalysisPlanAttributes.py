"""
Update experiment analysis plan attributes returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request import ExperimentsAnalysisPlanWriteV2Request
from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data import (
    ExperimentsAnalysisPlanWriteV2RequestData,
)
from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_attributes import (
    ExperimentsAnalysisPlanWriteV2RequestDataAttributes,
)
from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_type import (
    ExperimentsAnalysisPlanWriteV2RequestDataType,
)

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

body = ExperimentsAnalysisPlanWriteV2Request(
    data=ExperimentsAnalysisPlanWriteV2RequestData(
        type=ExperimentsAnalysisPlanWriteV2RequestDataType.ANALYSIS_PLANS,
        id=EXPERIMENT_DATA_ID,
        attributes=ExperimentsAnalysisPlanWriteV2RequestDataAttributes(
            confidence_level=0.9,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.update_experiment_analysis_plan_attributes(experiment_id=EXPERIMENT_DATA_ID, body=body)

    print(response)
