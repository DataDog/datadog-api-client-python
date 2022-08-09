# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class UserInvitationsType(ModelSimple):
    """
    User invitations type.

    :param value: If omitted defaults to "user_invitations". Must be one of ["user_invitations"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "USER_INVITATIONS": "user_invitations",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
