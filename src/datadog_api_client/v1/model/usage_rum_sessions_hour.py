# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageRumSessionsHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
            "replay_session_count": (int,),
            "session_count": (int,),
            "session_count_android": (int,),
            "session_count_ios": (int,),
        }

    attribute_map = {
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
        "replay_session_count": "replay_session_count",
        "session_count": "session_count",
        "session_count_android": "session_count_android",
        "session_count_ios": "session_count_ios",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageRumSessionsHour - a model defined in OpenAPI

        Keyword Args:
            hour (datetime): [optional] The hour for the usage.
            org_name (str): [optional] The organization name.
            public_id (str): [optional] The organization public ID.
            replay_session_count (int): [optional] Contains the number of RUM Replay Sessions (data available beginning November 1, 2021).
            session_count (int): [optional] Contains the number of browser RUM Lite Sessions.
            session_count_android (int): [optional] Contains the number of mobile RUM Sessions on Android (data available beginning December 1, 2020).
            session_count_ios (int): [optional] Contains the number of mobile RUM Sessions on iOS (data available beginning December 1, 2020).
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageRumSessionsHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
