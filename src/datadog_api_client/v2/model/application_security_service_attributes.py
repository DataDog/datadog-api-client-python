# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationSecurityServiceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_versions": ([str],),
            "app_type": (str,),
            "asm_threat_compatible": (bool,),
            "backend_waf_event_count": (int,),
            "business_logic": ([str],),
            "color": (str,),
            "env": (str,),
            "event_count": (int,),
            "event_trend": ([int],),
            "has_appsec_enabled": (bool,),
            "hits": (int,),
            "iast_product_activation": (bool,),
            "iast_product_compatibility": (str,),
            "iast_product_compatibility_reasons": ([str],),
            "languages": ([str],),
            "last_ingested_spans": (int,),
            "rc_capabilities": ([str],),
            "recommended_business_logic": ([str],),
            "risk_product_activation": (bool,),
            "risk_product_compatibility": (str,),
            "risk_product_compatibility_reasons": ([str],),
            "rules_version": ([str],),
            "service": (str,),
            "signal_count": (int,),
            "signal_trend": ([int],),
            "source": ([str],),
            "teams": ([str],),
            "tracer_versions": ([str],),
            "vm_activation": (str,),
            "vuln_critical_count": (int,),
            "vuln_high_count": (int,),
            "without_filter_services": (int,),
        }

    attribute_map = {
        "agent_versions": "agent_versions",
        "app_type": "app_type",
        "asm_threat_compatible": "asm_threat_compatible",
        "backend_waf_event_count": "backend_waf_event_count",
        "business_logic": "business_logic",
        "color": "color",
        "env": "env",
        "event_count": "event_count",
        "event_trend": "event_trend",
        "has_appsec_enabled": "has_appsec_enabled",
        "hits": "hits",
        "iast_product_activation": "iast_product_activation",
        "iast_product_compatibility": "iast_product_compatibility",
        "iast_product_compatibility_reasons": "iast_product_compatibility_reasons",
        "languages": "languages",
        "last_ingested_spans": "last_ingested_spans",
        "rc_capabilities": "rc_capabilities",
        "recommended_business_logic": "recommended_business_logic",
        "risk_product_activation": "risk_product_activation",
        "risk_product_compatibility": "risk_product_compatibility",
        "risk_product_compatibility_reasons": "risk_product_compatibility_reasons",
        "rules_version": "rules_version",
        "service": "service",
        "signal_count": "signal_count",
        "signal_trend": "signal_trend",
        "source": "source",
        "teams": "teams",
        "tracer_versions": "tracer_versions",
        "vm_activation": "vm-activation",
        "vuln_critical_count": "vuln_critical_count",
        "vuln_high_count": "vuln_high_count",
        "without_filter_services": "without_filter_services",
    }

    def __init__(
        self_,
        agent_versions: List[str],
        app_type: str,
        asm_threat_compatible: bool,
        backend_waf_event_count: int,
        business_logic: List[str],
        color: str,
        env: str,
        event_count: int,
        event_trend: List[int],
        has_appsec_enabled: bool,
        hits: int,
        iast_product_activation: bool,
        iast_product_compatibility: str,
        iast_product_compatibility_reasons: List[str],
        languages: List[str],
        last_ingested_spans: int,
        rc_capabilities: List[str],
        recommended_business_logic: List[str],
        risk_product_activation: bool,
        risk_product_compatibility: str,
        risk_product_compatibility_reasons: List[str],
        rules_version: List[str],
        service: str,
        signal_count: int,
        signal_trend: List[int],
        source: List[str],
        teams: List[str],
        tracer_versions: List[str],
        vm_activation: str,
        vuln_critical_count: int,
        vuln_high_count: int,
        without_filter_services: int,
        **kwargs,
    ):
        """
        Application Security details describing a service in a given environment.

        :param agent_versions: The Datadog Agent versions reporting for the service.
        :type agent_versions: [str]

        :param app_type: The application type of the service, such as ``web`` or ``serverless``.
        :type app_type: str

        :param asm_threat_compatible: Whether the service is compatible with Application Security Management (Threats).
        :type asm_threat_compatible: bool

        :param backend_waf_event_count: The number of backend WAF events detected for the service.
        :type backend_waf_event_count: int

        :param business_logic: The enabled business logic detection rules for the service.
        :type business_logic: [str]

        :param color: Deprecated: a display color associated with the service in the UI. **Deprecated**.
        :type color: str

        :param env: The environment the service runs in.
        :type env: str

        :param event_count: The number of Application Security events detected for the service.
        :type event_count: int

        :param event_trend: Deprecated: the trend of Application Security events over time. **Deprecated**.
        :type event_trend: [int]

        :param has_appsec_enabled: Whether Application Security Management (Threats) is enabled for the service.
        :type has_appsec_enabled: bool

        :param hits: Deprecated: the number of hits for the service. **Deprecated**.
        :type hits: int

        :param iast_product_activation: Whether Interactive Application Security Testing (IAST) is enabled for the service.
        :type iast_product_activation: bool

        :param iast_product_compatibility: The Interactive Application Security Testing (IAST) compatibility status of the service.
        :type iast_product_compatibility: str

        :param iast_product_compatibility_reasons: The reasons explaining the Interactive Application Security Testing (IAST) compatibility status.
        :type iast_product_compatibility_reasons: [str]

        :param languages: The programming languages detected for the service.
        :type languages: [str]

        :param last_ingested_spans: The Unix timestamp, in seconds, of the last ingested span for the service.
        :type last_ingested_spans: int

        :param rc_capabilities: The Remote Configuration capabilities reported by the service.
        :type rc_capabilities: [str]

        :param recommended_business_logic: The recommended business logic detection rules for the service.
        :type recommended_business_logic: [str]

        :param risk_product_activation: Whether Software Composition Analysis (SCA) is enabled for the service.
        :type risk_product_activation: bool

        :param risk_product_compatibility: The Software Composition Analysis (SCA) compatibility status of the service.
        :type risk_product_compatibility: str

        :param risk_product_compatibility_reasons: The reasons explaining the Software Composition Analysis (SCA) compatibility status.
        :type risk_product_compatibility_reasons: [str]

        :param rules_version: The WAF rules versions applied to the service.
        :type rules_version: [str]

        :param service: The name of the service.
        :type service: str

        :param signal_count: Deprecated: the number of security signals for the service. **Deprecated**.
        :type signal_count: int

        :param signal_trend: Deprecated: the trend of security signals over time. **Deprecated**.
        :type signal_trend: [int]

        :param source: The data sources that contributed information about the service.
        :type source: [str]

        :param teams: The teams that own the service.
        :type teams: [str]

        :param tracer_versions: The Datadog tracing library versions reporting for the service.
        :type tracer_versions: [str]

        :param vm_activation: The Vulnerability Management activation status of the service.
        :type vm_activation: str

        :param vuln_critical_count: Deprecated: the number of critical-severity vulnerabilities for the service. **Deprecated**.
        :type vuln_critical_count: int

        :param vuln_high_count: Deprecated: the number of high-severity vulnerabilities for the service. **Deprecated**.
        :type vuln_high_count: int

        :param without_filter_services: The total number of services available without applying the service filter.
        :type without_filter_services: int
        """
        super().__init__(kwargs)

        self_.agent_versions = agent_versions
        self_.app_type = app_type
        self_.asm_threat_compatible = asm_threat_compatible
        self_.backend_waf_event_count = backend_waf_event_count
        self_.business_logic = business_logic
        self_.color = color
        self_.env = env
        self_.event_count = event_count
        self_.event_trend = event_trend
        self_.has_appsec_enabled = has_appsec_enabled
        self_.hits = hits
        self_.iast_product_activation = iast_product_activation
        self_.iast_product_compatibility = iast_product_compatibility
        self_.iast_product_compatibility_reasons = iast_product_compatibility_reasons
        self_.languages = languages
        self_.last_ingested_spans = last_ingested_spans
        self_.rc_capabilities = rc_capabilities
        self_.recommended_business_logic = recommended_business_logic
        self_.risk_product_activation = risk_product_activation
        self_.risk_product_compatibility = risk_product_compatibility
        self_.risk_product_compatibility_reasons = risk_product_compatibility_reasons
        self_.rules_version = rules_version
        self_.service = service
        self_.signal_count = signal_count
        self_.signal_trend = signal_trend
        self_.source = source
        self_.teams = teams
        self_.tracer_versions = tracer_versions
        self_.vm_activation = vm_activation
        self_.vuln_critical_count = vuln_critical_count
        self_.vuln_high_count = vuln_high_count
        self_.without_filter_services = without_filter_services
