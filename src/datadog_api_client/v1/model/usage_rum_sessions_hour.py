# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class UsageRumSessionsHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
            "replay_session_count": (int,),
            "session_count": (int, none_type),
            "session_count_android": (int, none_type),
            "session_count_ios": (int, none_type),
            "session_count_reactnative": (int, none_type),
        }

    attribute_map = {
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
        "replay_session_count": "replay_session_count",
        "session_count": "session_count",
        "session_count_android": "session_count_android",
        "session_count_ios": "session_count_ios",
        "session_count_reactnative": "session_count_reactnative",
    }

    def __init__(self, *args, **kwargs):
        """
        Number of RUM Sessions recorded for each hour for a given organization.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param replay_session_count: Contains the number of RUM Replay Sessions (data available beginning November 1, 2021).
        :type replay_session_count: int, optional

        :param session_count: Contains the number of browser RUM Lite Sessions.
        :type session_count: int, none_type, optional

        :param session_count_android: Contains the number of mobile RUM Sessions on Android (data available beginning December 1, 2020).
        :type session_count_android: int, none_type, optional

        :param session_count_ios: Contains the number of mobile RUM Sessions on iOS (data available beginning December 1, 2020).
        :type session_count_ios: int, none_type, optional

        :param session_count_reactnative: Contains the number of mobile RUM Sessions on React Native (data available beginning May 1, 2022).
        :type session_count_reactnative: int, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageRumSessionsHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
