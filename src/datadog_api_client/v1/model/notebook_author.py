# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class NotebookAuthor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "created_at": (datetime,),
            "disabled": (bool,),
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "name": (
                str,
                none_type,
            ),
            "status": (str,),
            "title": (
                str,
                none_type,
            ),
            "verified": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "disabled": "disabled",
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "name": "name",
        "status": "status",
        "title": "title",
        "verified": "verified",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """NotebookAuthor - a model defined in OpenAPI

        Keyword Args:
            created_at (datetime): [optional] Creation time of the user.
            disabled (bool): [optional] Whether the user is disabled.
            email (str): [optional] Email of the user.
            handle (str): [optional] Handle of the user.
            icon (str): [optional] URL of the user's icon.
            name (str, none_type): [optional] Name of the user.
            status (str): [optional] Status of the user.
            title (str, none_type): [optional] Title of the user.
            verified (bool): [optional] Whether the user is verified.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookAuthor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
