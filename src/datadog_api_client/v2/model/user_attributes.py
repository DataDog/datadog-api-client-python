# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class UserAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "created_at": (datetime,),
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "modified_at": (datetime,),
            "name": (str, none_type),
            "service_account": (bool,),
            "status": (str,),
            "title": (str, none_type),
            "verified": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "modified_at": "modified_at",
        "name": "name",
        "service_account": "service_account",
        "status": "status",
        "title": "title",
        "verified": "verified",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Attributes of user object returned by the API.

        :param created_at: Creation time of the user.
        :type created_at: datetime, optional

        :param disabled: Whether the user is disabled.
        :type disabled: bool, optional

        :param email: Email of the user.
        :type email: str, optional

        :param handle: Handle of the user.
        :type handle: str, optional

        :param icon: URL of the user's icon.
        :type icon: str, optional

        :param modified_at: Time that the user was last modified.
        :type modified_at: datetime, optional

        :param name: Name of the user.
        :type name: str, none_type, optional

        :param service_account: Whether the user is a service account.
        :type service_account: bool, optional

        :param status: Status of the user.
        :type status: str, optional

        :param title: Title of the user.
        :type title: str, none_type, optional

        :param verified: Whether the user is verified.
        :type verified: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
