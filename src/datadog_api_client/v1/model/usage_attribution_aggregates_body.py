# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageAttributionAggregatesBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agg_type": (str,),
            "field": (str,),
            "value": (float,),
        }

    attribute_map = {
        "agg_type": "agg_type",
        "field": "field",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        The object containing the aggregates.

        :param agg_type: The aggregate type.
        :type agg_type: str, optional

        :param field: The field.
        :type field: str, optional

        :param value: The value for a given field.
        :type value: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionAggregatesBody, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
