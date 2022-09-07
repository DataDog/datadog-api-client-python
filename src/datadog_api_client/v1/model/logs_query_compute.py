# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsQueryCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "facet": (str,),
            "interval": (int,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "facet": "facet",
        "interval": "interval",
    }

    def __init__(self_, aggregation, *args, **kwargs):
        """
        Define computation for a log query.

        :param aggregation: The aggregation method.
        :type aggregation: str

        :param facet: Facet name.
        :type facet: str, optional

        :param interval: Define a time interval in seconds.
        :type interval: int, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.aggregation = aggregation
