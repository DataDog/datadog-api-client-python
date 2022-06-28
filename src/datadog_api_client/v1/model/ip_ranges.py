# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IPRanges(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.ip_prefixes_agents import IPPrefixesAgents
        from datadog_api_client.v1.model.ip_prefixes_api import IPPrefixesAPI
        from datadog_api_client.v1.model.ip_prefixes_apm import IPPrefixesAPM
        from datadog_api_client.v1.model.ip_prefixes_logs import IPPrefixesLogs
        from datadog_api_client.v1.model.ip_prefixes_process import IPPrefixesProcess
        from datadog_api_client.v1.model.ip_prefixes_synthetics import IPPrefixesSynthetics
        from datadog_api_client.v1.model.ip_prefixes_synthetics_private_locations import (
            IPPrefixesSyntheticsPrivateLocations,
        )
        from datadog_api_client.v1.model.ip_prefixes_webhooks import IPPrefixesWebhooks

        return {
            "agents": (IPPrefixesAgents,),
            "api": (IPPrefixesAPI,),
            "apm": (IPPrefixesAPM,),
            "logs": (IPPrefixesLogs,),
            "modified": (str,),
            "process": (IPPrefixesProcess,),
            "synthetics": (IPPrefixesSynthetics,),
            "synthetics_private_locations": (IPPrefixesSyntheticsPrivateLocations,),
            "version": (int,),
            "webhooks": (IPPrefixesWebhooks,),
        }

    attribute_map = {
        "agents": "agents",
        "api": "api",
        "apm": "apm",
        "logs": "logs",
        "modified": "modified",
        "process": "process",
        "synthetics": "synthetics",
        "synthetics_private_locations": "synthetics-private-locations",
        "version": "version",
        "webhooks": "webhooks",
    }

    def __init__(self, *args, **kwargs):
        """
        IP ranges.

        :param agents: Available prefix information for the Agent endpoints.
        :type agents: IPPrefixesAgents, optional

        :param api: Available prefix information for the API endpoints.
        :type api: IPPrefixesAPI, optional

        :param apm: Available prefix information for the APM endpoints.
        :type apm: IPPrefixesAPM, optional

        :param logs: Available prefix information for the Logs endpoints.
        :type logs: IPPrefixesLogs, optional

        :param modified: Date when last updated, in the form ``YYYY-MM-DD-hh-mm-ss``.
        :type modified: str, optional

        :param process: Available prefix information for the Process endpoints.
        :type process: IPPrefixesProcess, optional

        :param synthetics: Available prefix information for the Synthetics endpoints.
        :type synthetics: IPPrefixesSynthetics, optional

        :param synthetics_private_locations: Available prefix information for the Synthetics Private Locations endpoints.
        :type synthetics_private_locations: IPPrefixesSyntheticsPrivateLocations, optional

        :param version: Version of the IP list.
        :type version: int, optional

        :param webhooks: Available prefix information for the Webhook endpoints.
        :type webhooks: IPPrefixesWebhooks, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IPRanges, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
