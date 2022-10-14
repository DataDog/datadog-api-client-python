# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ConfluentAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_response_data import ConfluentAccountResponseData

        return {
            "data": (ConfluentAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        The expected response schema when getting a Confluent account.

        :param data: An API key and API secret pair that represents a Confluent account.
        :type data: ConfluentAccountResponseData, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
