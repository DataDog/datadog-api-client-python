# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_metadata_origin import MetricMetadataOrigin
    from datadog_api_client.v2.model.metric_metadata_unit import MetricMetadataUnit


class MetricMetadataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_metadata_origin import MetricMetadataOrigin
        from datadog_api_client.v2.model.metric_metadata_unit import MetricMetadataUnit

        return {
            "description": (str, none_type),
            "historical_metrics_enabled": (bool,),
            "include_percentiles": (bool,),
            "integration": (str, none_type),
            "last_configured_at": (datetime, none_type),
            "metric_type": (str, none_type),
            "origin": (MetricMetadataOrigin,),
            "per_unit": (MetricMetadataUnit,),
            "short_name": (str, none_type),
            "source": (str, none_type),
            "statsd_interval": (int, none_type),
            "unit": (MetricMetadataUnit,),
        }

    attribute_map = {
        "description": "description",
        "historical_metrics_enabled": "historical_metrics_enabled",
        "include_percentiles": "include_percentiles",
        "integration": "integration",
        "last_configured_at": "last_configured_at",
        "metric_type": "metric_type",
        "origin": "origin",
        "per_unit": "per_unit",
        "short_name": "short_name",
        "source": "source",
        "statsd_interval": "statsd_interval",
        "unit": "unit",
    }

    def __init__(
        self_,
        description: Union[str, none_type],
        historical_metrics_enabled: bool,
        include_percentiles: bool,
        integration: Union[str, none_type],
        last_configured_at: Union[datetime, none_type],
        metric_type: Union[str, none_type],
        origin: MetricMetadataOrigin,
        per_unit: Union[MetricMetadataUnit, none_type],
        short_name: Union[str, none_type],
        source: Union[str, none_type],
        statsd_interval: Union[int, none_type],
        unit: Union[MetricMetadataUnit, none_type],
        **kwargs,
    ):
        """
        Metadata for one metric. Every attribute is always present. A value that is unknown or not set is ``null``.

        :param description: Description of the metric, or ``null`` if none is set.
        :type description: str, none_type

        :param historical_metrics_enabled: Whether historical metrics ingestion is enabled for the metric.
        :type historical_metrics_enabled: bool

        :param include_percentiles: Whether percentile aggregations are enabled for the metric. Percentile aggregations are available only for distribution metrics.
        :type include_percentiles: bool

        :param integration: Name of the integration that sent the metric, or ``null`` if none is set. This is always ``null`` for
            out-of-the-box RUM metrics.
        :type integration: str, none_type

        :param last_configured_at: When the metric's tag or percentile configuration was last changed, or ``null`` if it has never been configured.
        :type last_configured_at: datetime, none_type

        :param metric_type: Metric type, or ``null`` if it isn't known. Known values are ``gauge`` , ``count`` , ``rate`` , ``distribution`` ,
            ``explicit_histogram`` , and ``exponential_histogram`` , plus the legacy values ``counter`` and ``hll``. New values may
            be added. For histograms and sketches, this can differ from the type returned by
            ``GET /api/v1/metrics/{metric_name}``.
        :type metric_type: str, none_type

        :param origin: Where the metric comes from. Each value is the display label shown on the Metrics Summary page. The set of labels can grow as Datadog adds products. Each field is ``null`` when it isn't known.
        :type origin: MetricMetadataOrigin

        :param per_unit: A unit of measure from the Datadog unit catalog, or ``null`` when no unit is set.
        :type per_unit: MetricMetadataUnit, none_type

        :param short_name: Short display name of the metric, or ``null`` if none is set.
        :type short_name: str, none_type

        :param source: How the metric reaches Datadog, or ``null`` if it isn't known. Known values are ``intake`` , ``api_default`` , and
            ``intake_serverless`` for submitted metrics, and ``api_logs`` , ``api_processes`` , ``api_apm_spans`` , and ``api_rum``
            for metrics generated from logs, processes, APM spans, and RUM events. New values may be added.
        :type source: str, none_type

        :param statsd_interval: StatsD flush interval of the metric in seconds, or ``null`` if none is set.
        :type statsd_interval: int, none_type

        :param unit: A unit of measure from the Datadog unit catalog, or ``null`` when no unit is set.
        :type unit: MetricMetadataUnit, none_type
        """
        super().__init__(kwargs)

        self_.description = description
        self_.historical_metrics_enabled = historical_metrics_enabled
        self_.include_percentiles = include_percentiles
        self_.integration = integration
        self_.last_configured_at = last_configured_at
        self_.metric_type = metric_type
        self_.origin = origin
        self_.per_unit = per_unit
        self_.short_name = short_name
        self_.source = source
        self_.statsd_interval = statsd_interval
        self_.unit = unit
