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


class LogAttributes(ModelNormal):
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
            "host": (str,),
            "message": (str,),
            "service": (str,),
            "status": (str,),
            "tags": ([str],),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "host": "host",
        "message": "message",
        "service": "service",
        "status": "status",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(self, *args, **kwargs):
        """
        JSON object containing all log attributes and their associated values.

        :param attributes: JSON object of attributes from your log.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, none_type,)}, optional

        :param host: Name of the machine from where the logs are being sent.
        :type host: str, optional

        :param message: The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes)
            of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry.
            That value is then highlighted and displayed in the Logstream, where it is indexed for full text search.
        :type message: str, optional

        :param service: The name of the application or service generating the log events.
            It is used to switch from Logs to APM, so make sure you define the same
            value when you use both products.
        :type service: str, optional

        :param status: Status of the message associated with your log.
        :type status: str, optional

        :param tags: Array of tags associated with your log.
        :type tags: [str], optional

        :param timestamp: Timestamp of your log.
        :type timestamp: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
