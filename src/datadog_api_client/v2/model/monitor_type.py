# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorType(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (int,),
            "group_status": (int,),
            "groups": ([str],),
            "id": (int,),
            "message": (str,),
            "modified": (int,),
            "name": (str,),
            "query": (str,),
            "tags": ([str],),
            "templated_name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "group_status": "group_status",
        "groups": "groups",
        "id": "id",
        "message": "message",
        "modified": "modified",
        "name": "name",
        "query": "query",
        "tags": "tags",
        "templated_name": "templated_name",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes from the monitor that triggered the event.

        :param created_at: The POSIX timestamp of the monitor's creation in nanoseconds.
        :type created_at: int, optional

        :param group_status: Monitor group status used when there is no ``result_groups``.
        :type group_status: int, optional

        :param groups: Groups to which the monitor belongs.
        :type groups: [str], optional

        :param id: The monitor ID.
        :type id: int, optional

        :param message: The monitor message.
        :type message: str, optional

        :param modified: The monitor's last-modified timestamp.
        :type modified: int, optional

        :param name: The monitor name.
        :type name: str, optional

        :param query: The query that triggers the alert.
        :type query: str, optional

        :param tags: A list of tags attached to the monitor.
        :type tags: [str], optional

        :param templated_name: The templated name of the monitor before resolving any template variables.
        :type templated_name: str, optional

        :param type: The monitor type.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorType, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
