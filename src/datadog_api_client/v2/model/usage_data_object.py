# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageDataObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_attributes_object import UsageAttributesObject
        from datadog_api_client.v2.model.usage_time_series_type import UsageTimeSeriesType

        return {
            "attributes": (UsageAttributesObject,),
            "id": (str,),
            "type": (UsageTimeSeriesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        Usage data.

        :param attributes: Usage attributes data.
        :type attributes: UsageAttributesObject, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of usage data.
        :type type: UsageTimeSeriesType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
