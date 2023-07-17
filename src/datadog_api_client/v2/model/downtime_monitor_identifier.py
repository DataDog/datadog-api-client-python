# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DowntimeMonitorIdentifier(ModelComposed):
    def __init__(self, **kwargs):
        """
        Monitor identifier for the downtime.

        :param monitor_id: ID of the monitor to prevent notifications.
        :type monitor_id: int

        :param monitor_tags: A list of monitor tags. For example, tags that are applied directly to monitors,
            not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies.
            The resulting downtime applies to monitors that match **all** provided monitor tags. Setting `monitor_tags`
            to `[*]` configures the downtime to mute all monitors for the given scope.
        :type monitor_tags: [str]
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.downtime_monitor_identifier_id import DowntimeMonitorIdentifierId
        from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags

        return {
            "oneOf": [
                DowntimeMonitorIdentifierId,
                DowntimeMonitorIdentifierTags,
            ],
        }
