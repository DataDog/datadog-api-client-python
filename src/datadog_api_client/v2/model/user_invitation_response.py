# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserInvitationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData

        return {
            "data": (UserInvitationResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        User invitation as returned by the API.

        :param data: Object of a user invitation returned by the API.
        :type data: UserInvitationResponseData, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
