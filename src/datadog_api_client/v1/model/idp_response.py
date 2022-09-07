# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IdpResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
        }

    attribute_map = {
        "message": "message",
    }

    def __init__(self_, message, *args, **kwargs):
        """
        The IdP response object.

        :param message: Identity provider response.
        :type message: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.message = message
