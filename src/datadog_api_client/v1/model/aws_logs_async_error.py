# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsAsyncError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    def __init__(self_, *args, **kwargs):
        """
        Description of errors.

        :param code: Code properties
        :type code: str, optional

        :param message: Message content.
        :type message: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
