# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SuccessfulSignalUpdateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "status": (str,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, *args, **kwargs):
        """
        Updated signal data following a successfully performed update.

        :param status: Status of the response.
        :type status: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
