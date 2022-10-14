# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ConfluentResourceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_resource_response_data import ConfluentResourceResponseData

        return {
            "data": (ConfluentResourceResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response schema when interacting with a Confluent resource.

        :param data: Confluent Cloud resource data.
        :type data: ConfluentResourceResponseData, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
