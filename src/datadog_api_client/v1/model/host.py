# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Host(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_meta import HostMeta
        from datadog_api_client.v1.model.host_metrics import HostMetrics

        return {
            "aliases": ([str],),
            "apps": ([str],),
            "aws_name": (str,),
            "host_name": (str,),
            "id": (int,),
            "is_muted": (bool,),
            "last_reported_time": (int,),
            "meta": (HostMeta,),
            "metrics": (HostMetrics,),
            "mute_timeout": (int,),
            "name": (str,),
            "sources": ([str],),
            "tags_by_source": ({str: ([str],)},),
            "up": (bool,),
        }

    attribute_map = {
        "aliases": "aliases",
        "apps": "apps",
        "aws_name": "aws_name",
        "host_name": "host_name",
        "id": "id",
        "is_muted": "is_muted",
        "last_reported_time": "last_reported_time",
        "meta": "meta",
        "metrics": "metrics",
        "mute_timeout": "mute_timeout",
        "name": "name",
        "sources": "sources",
        "tags_by_source": "tags_by_source",
        "up": "up",
    }

    def __init__(self, *args, **kwargs):
        """
        Object representing a host.

        :param aliases: Host aliases collected by Datadog.
        :type aliases: [str], optional

        :param apps: The Datadog integrations reporting metrics for the host.
        :type apps: [str], optional

        :param aws_name: AWS name of your host.
        :type aws_name: str, optional

        :param host_name: The host name.
        :type host_name: str, optional

        :param id: The host ID.
        :type id: int, optional

        :param is_muted: If a host is muted or unmuted.
        :type is_muted: bool, optional

        :param last_reported_time: Last time the host reported a metric data point.
        :type last_reported_time: int, optional

        :param meta: Metadata associated with your host.
        :type meta: HostMeta, optional

        :param metrics: Host Metrics collected.
        :type metrics: HostMetrics, optional

        :param mute_timeout: Timeout of the mute applied to your host.
        :type mute_timeout: int, optional

        :param name: The host name.
        :type name: str, optional

        :param sources: Source or cloud provider associated with your host.
        :type sources: [str], optional

        :param tags_by_source: List of tags for each source (AWS, Datadog Agent, Chef..).
        :type tags_by_source: {str: ([str],)}, optional

        :param up: Displays UP when the expected metrics are received and displays ``???`` if no metrics are received.
        :type up: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Host, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
