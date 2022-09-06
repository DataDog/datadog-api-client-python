# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        Metric resource.

        :param name: The name of the resource.
        :type name: str, optional

        :param type: The type of the resource.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
