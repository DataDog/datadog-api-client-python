# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
)


class SecurityMonitoringSignalAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        none_type,
                    )
                },
            ),
            "message": (str,),
            "tags": ([str],),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "message": "message",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(self, *args, **kwargs):
        """
        The object containing all signal attributes and their
        associated values.

        :param attributes: A JSON object of attributes in the security signal.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, none_type,)}, optional

        :param message: The message in the security signal defined by the rule that generated the signal.
        :type message: str, optional

        :param tags: An array of tags associated with the security signal.
        :type tags: [str], optional

        :param timestamp: The timestamp of the security signal.
        :type timestamp: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
