# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLORawErrorBudgetRemaining(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "unit": (str,),
            "value": (float,),
        }

    attribute_map = {
        "unit": "unit",
        "value": "value",
    }

    def __init__(self_, *args, **kwargs):
        """
        Error budget remaining for an SLO.

        :param unit: Error budget remaining unit.
        :type unit: str, optional

        :param value: Error budget remaining value.
        :type value: float, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
