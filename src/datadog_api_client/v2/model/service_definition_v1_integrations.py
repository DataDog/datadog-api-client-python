# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionV1Integrations(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "pagerduty": (str,),
        }

    attribute_map = {
        "pagerduty": "pagerduty",
    }

    def __init__(self_, *args, **kwargs):
        """
        Third party integrations that Datadog supports.

        :param pagerduty: PagerDuty service URL for the service.
        :type pagerduty: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
